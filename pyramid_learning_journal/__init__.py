import os

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    if os.environ.get('DATABASE_URL', ''):
        settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
    engine = engine_from_config(settings, 'sqlalchemy.')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
