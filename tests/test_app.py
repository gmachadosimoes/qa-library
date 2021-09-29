import pytest
import app
import requests


url_index = 'http://localhost:5500/templates/index.html'
url_about = 'http://localhost:5500/templates/about.html'
url_page_not_found = 'http://localhost:5500/templates/page_not_found.html'


def test_route_index():
    assert 'index.html'

