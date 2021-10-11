"""Main Sanic application code."""

from domonic.html import p
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.request import Request
from sanic.response import HTTPResponse

from .helpers import configure_static_assets, not_found, page

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
async def four_oh_four(_req: Request) -> HTTPResponse:
    return not_found()


@app.exception(NotFound)
async def redirect_to_not_found(req: Request, _exc: Exception):
    return await four_oh_four(req)
