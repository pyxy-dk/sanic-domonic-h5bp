"""Main Sanic application code."""

from domonic.dom import Comment
from domonic.html import *
from sanic import Sanic, request, response
from sanic.exceptions import NotFound

from .helpers import configure_static_assets, page
from .strings import NOT_FOUND_COMMENT, NOT_FOUND_MESSAGE, NOT_FOUND_STYLE, NOT_FOUND_TITLE

app = Sanic("sanic-domonic-h5bp")
app.update_config("./.env")
configure_static_assets(app)


@app.route("/")
@app.route("/index.html")
async def index(req: request.Request) -> response.HTTPResponse:
    return page(req)


@app.route("/404.html")
async def not_found(req: request.Request) -> response.HTTPResponse:
    four_oh_four = html(
        head(
            meta(_charset="utf-8"),
            title(NOT_FOUND_TITLE),
            meta(_name="viewport", _content="width=device-width, initial-scale=1"),
            style(NOT_FOUND_STYLE),
        ),
        body(
            h1(NOT_FOUND_TITLE),
            p(NOT_FOUND_MESSAGE),
        ),
        comment(NOT_FOUND_COMMENT),
        _lang="en"
    )
    return response.html(f"{four_oh_four}")


@app.exception(NotFound)
async def redirect_to_not_found(req, _exc):
    return await not_found(req)
