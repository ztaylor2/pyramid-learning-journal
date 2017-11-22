"""Tests for pyramid app."""

import datetime
from pyramid_learning_journal.models import (
    Entry,
)
import pytest


def test_model_gets_added(db_session):
    """Test that a model is added to the fake database."""
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


def test_list_view_returns_proper_amount_of_content(dummy_request, add_models):
    """Home view response has file content."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(Entry)
    assert len(response['entries']) == query.count()


def test_detail_view(dummy_request, add_models):
    """Test that what's returned by the view is a dictionary of values."""
    from pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 5
    info = detail_view(dummy_request)
    assert isinstance(info, dict)


def test_detail_view_returns_correct_entry_id(dummy_request, add_models):
    """Test that what's returned by detail view is a model in test database."""
    from pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 5
    info = detail_view(dummy_request)
    assert info['entry'].id == 5


def test_home_route_has_table(testapp):
    """Test route has table."""
    response = testapp.get("/")
    assert len(response.html.find_all('body')) == 1
    assert len(response.html.find_all('p')) == 0


def test_home_route_has_tables_when_using_filldb_fixture(testapp, fill_the_db):
    """Test route has table."""
    response = testapp.get("/")
    assert len(response.html.find_all('body')) == 1
    assert len(response.html.find_all('p')) == 10


def test_detail_route_with_entry_detail(testapp, fill_the_db, dummy_request):
    """Test if detail page has proper response to specific entry."""
    response = testapp.get("/entry/5")
    query = dummy_request.dbsession.query(Entry)[5].title.split(".")[0]
    assert query in response.ubody


# def test_create_view_successful_post_redirects_home(testapp, journal_info, login, csrf_token):
#     """Test create view directs to same loc."""
#     # journal_info['csrf_token'] = csrf_token
#     with pytest.raises(AppError):
#         testapp.post("/create", journal_info)
#     #     testapp.post('/journal/new-entry', {})
#     # assert response.location == 'http://localhost/'


# def test_detail_view_response_contains_expense_attrs():
#     """Test that what's returned by the view contains one expense object."""
#     from pyramid_learning_journal.views.default import detail_view
#     request = testing.DummyRequest()
#     request.matchdict['id'] = 5
#     info = detail_view(request)
#     for key in ["id", "title", "body", "creation_date"]:
#         assert key in info["entry"]


# def test_update_view_requires_authentication(dummy_request):
#     """Test that what's returned by the view is a 403 page when no authentication."""
#     from pyramid_learning_journal.views.default import update_view
#     dummy_request.matchdict['id'] = 5
#     info = update_view(dummy_request)
#     import pdb; pdb.set_trace()
#     assert info is 403


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
