"""Main Sanic application code."""

from domonic.html import body, comment, h1, head, html, meta, p, style, title
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.request import Request
from sanic.response import HTTPResponse, html as response_html

from .helpers import configure_static_assets, page
from .strings import (
    NOT_FOUND_COMMENT,
    NOT_FOUND_MESSAGE,
    NOT_FOUND_STYLE,
    NOT_FOUND_TITLE,
    UTF8,
    VIEWPORT,
    VIEWPORT_CONTENT,
)

app = Sanic("sanic_domonic_h5bp")
configure_static_assets(app)


@app.route("/")
@app.route("/index.html")
async def index(req: Request) -> HTTPResponse:
    return page(
        req,
        title="",
        desc="",
        content=(
            # TODO Add your site or application content here.
            p("Hello world! This is HTML5 Boilerplate."),
        ),
    )


@app.route("/404.html")
async def not_found(req: Request) -> HTTPResponse:
    four_oh_four = html(
        head(
            meta(_charset=UTF8),
            title(NOT_FOUND_TITLE),
            meta(_name=VIEWPORT, _content=VIEWPORT_CONTENT),
            style(NOT_FOUND_STYLE),
        ),
        body(
            h1(NOT_FOUND_TITLE),
            p(NOT_FOUND_MESSAGE),
        ),
        comment(NOT_FOUND_COMMENT),
        _lang="en",
    )
    return response_html(f"{four_oh_four}")


@app.exception(NotFound)
async def redirect_to_not_found(req: Request, _exc: Exception):
    return await not_found(req)
