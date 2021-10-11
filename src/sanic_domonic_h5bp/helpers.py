"""Sanic/Domonic helper functions."""

from __future__ import annotations

from functools import lru_cache
from glob import glob
from typing import Sequence

from domonic.html import (
    Element,
    body,
    comment,
    h1,
    head,
    html,
    link,
    meta,
    p,
    script,
    style,
    title,
)
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, html as response_html

from .strings import (
    DESCRIPTION,
    NOT_FOUND_COMMENT,
    NOT_FOUND_MESSAGE,
    NOT_FOUND_STYLE,
    NOT_FOUND_TITLE,
    UTF8,
    VIEWPORT,
    VIEWPORT_CONTENT,
    WEBSITE,
)

BASEURL = "./src/sanic_domonic_h5bp"


def configure_static_assets(app: Sanic) -> None:
    """Configure routes for all files under the `static` dir."""
    static_dir = f"{BASEURL}/static"
    asset_paths = glob(f"{static_dir}/**/*.*", recursive=True)
    for path in asset_paths:
        route = path[len(static_dir) :]
        app.static(route, path)


@lru_cache(maxsize=None)
def not_found() -> HTTPResponse:
    """Construct and return the content of a 404 page."""
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


def page(req: Request, title: str, desc: str, content: Sequence[Element]) -> HTTPResponse:
    """Construct and return an entire page."""
    return response_html(f"{_html(req, title, desc, content)}")


def _body(content: Sequence) -> Element:
    """Return a <body> element with the given `content`."""
    return body(
        *content,
        script(_src="js/vendor/modernizr-3.11.2.min.js"),
        script(_src="js/plugins.js"),
        script(_src="js/main.js"),
        # TODO Google Analytics: change UA-XXXXX-Y to be your site's ID.
        *_google_analytics("UA-XXXXX-Y"),
    )


def _google_analytics(site_id: str) -> Sequence[Element]:
    """Return a Google Analytics snippet."""
    return (
        script(
            f"""
            window.ga = function () {{ ga.q.push(arguments) }}; ga.q = []; ga.l = +new Date;
            ga('create', '{site_id}', 'auto'); ga('set', 'anonymizeIp', true); ga('set', 'transport', 'beacon'); ga('send', 'pageview')"""
        ),
        script(_src="https://www.google-analytics.com/analytics.js", _async="async"),
    )


def _head(req: Request, title_: str, desc: str) -> Element:
    """Return a <head> element with `title` and `desc`."""
    return head(
        meta(_charset=UTF8),
        title(title_),
        meta(_name=DESCRIPTION, _content=desc),
        meta(_name=VIEWPORT, _content=VIEWPORT_CONTENT),
        meta(_property="og:title", _content=title_),
        meta(_property="og:type", _content=WEBSITE),
        meta(_property="og:url", _content=req.url),
        meta(_property="og:image", _content=""),
        link(_rel="manifest", _href="site.webmanifest"),
        link(_rel="apple-touch-icon", _href="icon.png"),
        link(_rel="stylesheet", _href="css/normalize.css"),
        link(_rel="stylesheet", _href="css/main.css"),
        meta(_name="theme-color", _content="#fafafa"),
    )


def _html(req: Request, title_: str, desc: str, content: Sequence) -> Element:
    """Construct and return the HTML element."""
    return html(
        _head(req, title_, desc),
        _body(content),
        _class="no-js",
        _lang="",
    )
