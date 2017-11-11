"""Fixtures for pyramid learning journal app."""

from pyramid import testing
import pytest
import transaction
from faker import Faker
from pyramid_learning_journal.models import (
    Entry,
    get_tm_session,
)
from pyramid_learning_journal.models.meta import Base


FAKE = Faker()
ENTRY_LIST = []
for i in range(10):
    entry = Entry(
        id=i,
        title=FAKE.file_name(),
        body=FAKE.paragraph(),
        creation_date=FAKE.date_time()
    )
    ENTRY_LIST.append(entry)


@pytest.fixture(scope="session")
def configuration(request):
    """Set up pointer to test database.  Import models.  Session scope for entire test session."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://zt@localhost:5432/test_entries'
    })
    config.include("pyramid_learning_journal.models")
    config.include("pyramid_learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """New HTTP request, results in new dbsession."""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def add_models(dummy_request):
    """Add model instances to DB."""
    dummy_request.dbsession.add_all(ENTRY_LIST)


# @pytest.fixture(scope="session")
# def testapp(request):
#     """Build a test app to test."""
#     from webtest import TestApp
#     from pyramid_learning_journal import main

#     app = main({}, **{"sqlalchemy.url": "postgres:///test_entries"})
#     testapp = TestApp(app)

#     SessionFactory = app.registry["dbsession_factory"]
#     engine = SessionFactory().bind
#     Base.metadata.create_all(bind=engine)

#     def tearDown():
#         Base.metadata.drop_all(bind=engine)

#     request.addfinalizer(tearDown)

#     return testapp

@pytest.fixture(scope="session")
def testapp(request):
    """Initialte teh test app."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        settings = {
            'sqlalchemy.url': 'postgres://zt@localhost:5432/test_entries'
        }  # points to a database
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('pyramid_learning_journal.routes')
        config.include('pyramid_learning_journal.models')
        config.include('pyramid_learning_journal.security')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)  # builds the tables

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)
    return TestApp(app)


@pytest.fixture
def fill_the_db(testapp):
    """Fill the database."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(ENTRY_LIST)
    # return dbsession
