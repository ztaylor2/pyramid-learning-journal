from pyramid import testing
from pyramid.response import Response


def test_home_view_returns_response():
    """Home view returns a Response object."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)

def test_home_view_is_good():
    """Home view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200

def test_home_view_returns_proper_content():
    """Home view response has file content."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert "<main class=\"article-list\">" in response.text

def test_detail_view_returns_response():
    """Detail view returns a Response object."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    assert isinstance(response, Response)

def test_detail_view_is_good():
    """Detail view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    assert response.status_code == 200

def test_detail_view_returns_proper_content():
    """Detail view response has file content."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    assert "<main class=\"article-content\">" in response.text

def test_create_view_returns_response():
    """Detail view returns a Response object."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert isinstance(response, Response)

def test_create_view_is_good():
    """Detail view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.status_code == 200

def test_create_view_returns_proper_content():
    """Detail view response has file content."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert "<label for=\"exampleFormControlTextarea1\">Article Body</label>" in response.text

def test_update_view_returns_response():
    """Detail view returns a Response object."""
    from pyramid_learning_journal.views.default import update_view
    request = testing.DummyRequest()
    response = update_view(request)
    assert isinstance(response, Response)

def test_update_view_is_good():
    """Detail view response has a status 200 OK."""
    from pyramid_learning_journal.views.default import update_view
    request = testing.DummyRequest()
    response = update_view(request)
    assert response.status_code == 200

def test_update_view_returns_proper_content():
    """Detail view response has file content."""
    from pyramid_learning_journal.views.default import update_view
    request = testing.DummyRequest()
    response = update_view(request)
    assert "<label for=\"exampleFormControlTextarea1\">Article Body</label>" in response.text