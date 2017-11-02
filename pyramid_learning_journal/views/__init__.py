from .default import list_view
from .default import detail_view
from .default import create_view
from .default import update_view


# def includeme(config):
#     """List of views to include for the configurator object."""
#     config.add_view(list_view, route_name='home', renderer='string')
#     config.add_view(detail_view, route_name='detail', renderer='string')
#     config.add_view(create_view, route_name='create', renderer='string')
#     config.add_view(update_view, route_name='update', renderer='string')