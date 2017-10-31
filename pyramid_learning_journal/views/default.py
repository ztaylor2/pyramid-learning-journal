"""Views for the pyramid learning journal app."""
from pyramid.response import Response

import io
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    imported_text = io.open(os.path.join(HERE, '../templates/index.html')).read()
    return Response(imported_text)


def detail_view(request):
    imported_text = io.open(os.path.join(HERE, '../templates/article.html')).read()
    return Response(imported_text)


def create_view(request):
    imported_text = io.open(os.path.join(HERE, '../templates/new-article.html')).read()
    return Response(imported_text)


def update_view(request):
    imported_text = io.open(os.path.join(HERE, '../templates/edit-article.html')).read()
    return Response(imported_text)
