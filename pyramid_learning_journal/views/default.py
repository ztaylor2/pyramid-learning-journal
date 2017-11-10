"""Views for the pyramid learning journal app."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid_learning_journal.models.entries import Entry
import datetime

from pyramid.security import remember, forget
from pyramid_learning_journal.security import check_credentials

import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='pyramid_learning_journal:templates/list_view.jinja2')
def list_view(request):
    """View for listing journal entries."""
    entries = request.dbsession.query(Entry).all()
    sorted_entries = sorted(entries, key=lambda entry: entry.id, reverse=True)
    return {
        "entries": sorted_entries,
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


@view_config(route_name='create', renderer="pyramid_learning_journal:/templates/create_view.jinja2", permission='secret')
def create_view(request):
    """Create a new journal entry, validate it first before putting into db, return home pg."""
    # import pdb; pdb.set_trace()
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
        return HTTPFound(request.route_url('home'))


@view_config(route_name='update', renderer='pyramid_learning_journal:/templates/update_view.jinja2', permission='secret')
def update_view(request):
    """View config for update view."""
    # import pdb; pdb.set_trace()
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)
    if not entry:
        return HTTPNotFound
    if request.method == 'GET':
        if entry:
            title = "Zach\'s Blog - {}".format(entry.title)
            return {
                "entry": entry,
                "title": title,
            }
    if request.method == 'POST':
        if not all(field in request.POST for field in ['title', 'body']):
            raise HTTPBadRequest
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=the_id))


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    if request.method == 'POST':
        username = request.params.get('username', '')
        password = request.params.get('password', '')
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
    return {}
