"""Views for the pyramid learning journal app."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid_learning_journal.models.entries import Entry
import datetime

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


# @view_config(route_name='create', renderer='pyramid_learning_journal:/templates/create_view.jinja2')
# def create_view(request):
#     """View config for create view."""
#     if request.method == "POST" and request.POST:
#         new_id = request.dbsession.query(Entry).count() + 1
#         form_data = request.POST
#         new_entry = Entry(
#             title=form_data['title'],
#             body=form_data['body'],
#             creation_date=datetime.datetime.now(),
#             id=new_id,
#         )
#         request.dbsession.add(new_entry)
#         return HTTPFound(location=request.route_url('home'))

#     return {
#         "title": "Zach\'s Blog - New Post",
#     }


@view_config(route_name='create_view', renderer="pyramid_learning_journal:/templates/create_view.jinja2")
def create_view(request):
    """Create a new journal entry, validate it first before putting into db, return home pg."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        if not all(field in request.POST for field in ['title', 'body']):
            raise HTTPBadRequest
        count = request.dbsession.query(Entry).count()
        new_entry = Entry(
            id=count + 1,
            title=request.POST['title'],
            body=request.POST['body'],
            creation_date=datetime.datetime.now(),
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('list_view'))


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
