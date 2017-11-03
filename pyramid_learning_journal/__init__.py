import os

from pyramid.config import Configurator

# from urllib import parse


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # url = parse.urlparse(os.environ["DATABASE_URL"])

    # settings = {}
    # if os.environ.get('DATABASE_URL', ''):
    #     settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
