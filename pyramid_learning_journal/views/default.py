"""Views for the pyramid learning journal app."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid_learning_journal.models.entries import Entry

import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='pyramid_learning_journal:templates/list_view.jinja2')
def list_view(request):
    """View for listing journal entries."""
    entries = request.dbsession.query(Entry).all()
    return {
        "entries": entries,
        "title": "Zach\'s Blog",
    }


@view_config(route_name='detail', renderer='pyramid_learning_journal:/templates/detail_view.jinja2')
def detail_view(request):
    """View for detail view, sends entry data with id matching the request."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)
    if entry:
        title = "Zach\'s Blog - {}".format(entry.title)
        return {
            "entry": entry,
            "title": title,
        }
    else:
        raise HTTPNotFound


@view_config(route_name='create', renderer='pyramid_learning_journal:/templates/create_view.jinja2')
def create_view(request):
    """View config for create view."""
    # make it so that on submit a new model instance is created..... 
    
    return {
        "title": "Zach\'s Blog - New Post",
    }


@view_config(route_name='update', renderer='pyramid_learning_journal:/templates/update_view.jinja2')
def update_view(request):
    """View config for update view."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)
    if entry:
        title = "Zach\'s Blog - {}".format(entry.title)
        return {
            "entry": entry,
            "title": title,
        }
    else:
        raise HTTPNotFound
