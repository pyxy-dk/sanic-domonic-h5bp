"""Sanic/Domonic helper functions."""

from __future__ import annotations

from glob import glob
from typing import Sequence

from domonic.html import Element, body, head, html, link, meta, script, title
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, html as response_html

from .strings import DESCRIPTION, UTF8, VIEWPORT, VIEWPORT_CONTENT, WEBSITE

BASEURL = "./src/sanic_domonic_h5bp"


def configure_static_assets(app: Sanic) -> None:
    """Configure the static file path for `path`."""
    static_dir = f"{BASEURL}/static"
    asset_paths = glob(f"{static_dir}/**/*.*", recursive=True)
    for path in asset_paths:
        route = path[len(static_dir) :]
        app.static(route, path)


def page(req: Request, title: str, desc: str, content: Sequence[Element]) -> HTTPResponse:
    """Construct and return an HTML string representing an entire page."""
    return response_html(f"{_html(req, title, desc, content)}")


def _body(content: Sequence) -> Element:
    """Construct and return the HTML5 <body> element."""
    return body(
        *content,
        script(_src="js/vendor/modernizr-3.11.2.min.js"),
        script(_src="js/plugins.js"),
        script(_src="js/main.js"),
        # TODO Google Analytics: change UA-XXXXX-Y to be your site's ID.
        *_google_analytics("UA-XXXXX-Y"),
    )


def _google_analytics(site_id: str) -> Sequence[Element]:
    """Return Google Analytics snippet."""
    return (
        script(
            f"""
            window.ga = function () {{ ga.q.push(arguments) }}; ga.q = []; ga.l = +new Date;
            ga('create', '{site_id}', 'auto'); ga('set', 'anonymizeIp', true); ga('set', 'transport', 'beacon'); ga('send', 'pageview')"""
        ),
        script(_src="https://www.google-analytics.com/analytics.js", _async="async"),
    )


def _head(req: Request, title_: str, desc: str) -> Element:
    """Construct and return the HTML5 <head> element."""
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
