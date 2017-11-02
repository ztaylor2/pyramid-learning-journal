"""Tests for pyramid app."""
from pyramid import testing
from pyramid_learning_journal.data.data import ENTRIES
import pytest


def test_list_view_returns_dict():
    """Home view returns a Response object."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, dict)


def test_list_view_returns_proper_amount_of_content():
    """Home view response has file content."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert len(response['entries']) == len(ENTRIES)


def test_detail_view():
    """Test that what's returned by the view is a dictionary of values."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    request.matchdict['id'] = 5
    info = detail_view(request)
    assert isinstance(info, dict)


def test_detail_view_response_contains_expense_attrs():
    """Test that what's returned by the view contains one expense object."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    request.matchdict['id'] = 5
    info = detail_view(request)
    for key in ["id", "title", "body", "creation_date"]:
        assert key in info["entry"]


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from pyramid_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Today we learned about a binary heap.' in html.find("p").text


def test_root_contents(testapp):
    """Test that the contents of the root page contains as many <p> tags as expenses."""
    from pyramid_learning_journal.data.data import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("p"))
