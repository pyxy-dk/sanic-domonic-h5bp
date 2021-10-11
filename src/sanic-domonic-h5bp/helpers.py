"""Sanic/Domonic helper functions."""

from glob import glob

from domonic.html import Element, body, div, head, html, span
from sanic import Sanic, request, response

BASEURL = "./src/sanic-domonic-h5bp"


def configure_static_assets(app: Sanic) -> None:
    """Configure the static file path for `path`."""
    static_dir = f"{BASEURL}/static"
    asset_paths = glob(f"{static_dir}/**/*.*", recursive=True)
    for path in asset_paths:
        route = path[len(static_dir) :]
        app.static(route, path)


def page(req: request.Request, **kwargs) -> response.HTTPResponse:
    """Construct and return an HTML string representing an entire page."""
    return response.html(f"{_html()}")


def _body() -> Element:
    """Construct and return the HTML5 <body> element."""
    return body(div(span("Hello world!")))


def _head() -> Element:
    """Construct and return the HTML5 <head> element."""
    return head()


def _html() -> Element:
    """Construct and return the HTML element."""
    return html(
        _head(),
        _body(),
    )
