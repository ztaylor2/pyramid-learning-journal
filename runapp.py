import os

from paste.deploy import loadapp
from waitress import serve


# from urllib import parse
# import psycopg2

# parse.uses_netloc.append("postgres")
# url = parse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )


settings = {}
if os.environ.get('DATABASE_URL', ''):
    settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
settings['pyramid.includes'] = ['pyramid_tm']

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:production.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)