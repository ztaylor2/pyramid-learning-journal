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

import os

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


@pytest.fixture
def journal_info():
    """Create a info dictionary for edit or create later."""
    info = {
        'title': 'testing',
        'body': 'testing_body',
        'creation_date': '2017-11-02'
    }
    return info


@pytest.fixture
def edit_info():
    """Create a dict for simulating editing."""
    info = {
        'title': 'edited journal',
        'body': 'I just changed the journal created in above test',
        'creation_date': ''
    }
    return info


@pytest.fixture
def login(testapp):
    """Log in with credentials."""
    AUTH_PASSWORD = os.environ.get('AUTH_USERNAME', '')
    AUTH_USERNAME = os.environ.get('AUTH_PASSWORD', '')
    secret = {
        'username': AUTH_PASSWORD,
        'password': AUTH_USERNAME
    }
    testapp.post('/login', secret)


@pytest.fixture
def logout(testapp):
    """Log out route."""
    testapp.get('/logout')


@pytest.fixture
def csrf_token(testapp):
    """Will get the csrf token."""
    get_tk = testapp.get('/create')
    token = get_tk.html.find('input', {'name': 'csrf_token'})['value']
    return token
