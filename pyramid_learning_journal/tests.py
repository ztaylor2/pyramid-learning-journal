"""Tests for pyramid app."""
from pyramid import testing
import pytest
import transaction
import datetime
from faker import Faker
import random
from pyramid_learning_journal.models import (
    Entry,
    get_tm_session,
)
from pyramid_learning_journal.models.meta import Base


FAKE_FACTORY = Faker()
CATEGORIES = ["day1", "day2", "day3", "day4"]
ENTRY_LIST = [Entry(
    title=random.choice(CATEGORIES),
    id=random.random() * random.randint(0, 1000),
    creation_date=datetime.datetime.now(),
    body=FAKE_FACTORY.text(100)
) for i in range(20)]


@pytest.fixture(scope="session")
def configuration(request):
    """Set up pointer to test database.  Import models.  Session scope for entire test session."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_entries'
    })
    config.include("pyramid_learning_journal.models")

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


def test_model_gets_added(db_session):
    assert len(db_session.query(Entry).all()) == 0
    model = Entry(
        title="Fake title",
        id=5,
        creation_date=datetime.datetime.now(),
        body="fake body text."
    )
    db_session.add(model)
    assert len(db_session.query(Entry).all()) == 1


def test_list_view_returns_dict(dummy_request):
    """Home view returns a Response object."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_empty_when_database_empty(dummy_request):
    """List view returns nothing when there is no data."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entries']) == 0


def test_list_view_returns_proper_amount_of_content(dummy_request):
    """Home view response has file content."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(Entry)
    assert len(response['entries']) == query.count()


# def test_detail_view(dummy_request):
#     """Test that what's returned by the view is a dictionary of values."""
#     from pyramid_learning_journal.views.default import detail_view
#     dummy_request.matchdict['id'] = 5
#     info = detail_view(dummy_request)
#     assert isinstance(info, dict)


# def test_detail_view_response_contains_expense_attrs():
#     """Test that what's returned by the view contains one expense object."""
#     from pyramid_learning_journal.views.default import detail_view
#     request = testing.DummyRequest()
#     request.matchdict['id'] = 5
#     info = detail_view(request)
#     for key in ["id", "title", "body", "creation_date"]:
#         assert key in info["entry"]



@pytest.fixture(scope="session")
def testapp(request):
    from webtest import TestApp
    from pyramid_learning_journal import main

    app = main({}, **{"sqlalchemy.url": "postgres:///test_entries"})
    testapp = TestApp(app)

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return testapp


@pytest.fixture
def fill_the_db(testapp):
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(ENTRY_LIST)

    return dbsession


# @pytest.fixture()
# def testapp():
#     """Create an instance of our app for testing."""
#     from pyramid_learning_journal import main
#     app = main({})
#     from webtest import TestApp
#     return TestApp(app)


# def test_layout_root(testapp):
#     """Test that the contents of the root page contains <article>."""
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert 'Today we learned about a binary heap.' in html.find("section").text


# def test_root_contents(testapp):
#     """Test that the contents of the root page contains as many <p> tags as entires."""
#     from pyramid_learning_journal.data.data import ENTRIES
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert len(ENTRIES) == len(html.findAll("p"))
