"""Views for the pyramid learning journal app."""
from pyramid.view import view_config
from pyramid_learning_journal.data.data import ENTRIES

# import io
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/list_view.jinja2')
def list_view(request):
    """View config for list view."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail_view.jinja2')
def detail_view(request):
    """View config for detail view."""
    the_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            return {"entry": entry}


@view_config(route_name='create', renderer='../templates/create_view.jinja2')
def create_view(request):
    """View config for create view."""
    return {}


@view_config(route_name='update', renderer='../templates/update_view.jinja2')
def update_view(request):
    """View config for update view."""
    the_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            return {"entry": entry}
