# sanic-domonic-h5bp

![Pipenv - Python version][pipenv-badge-img]
[![Code style: black][black-badge-img]][black-badge-href]

A template repository implementing HTML5 Boilerplate 8.0 in Sanic using the
Domonic framework.

If you need frontend interactivity, this template goes well with e.g.
[HTMX](htmx) and [HyperScript](hyperscript) rather than your run-of-the-mill
bloated JS framework *du jour*.

## Requirements

* `python-3.8`
* `pipenv`

## Running

```text
git clone git@github.com:pyxy-dk/sanic-domonic-h5bp.git

cd sanic-domonic-h5bp

pipenv install --dev

pipenv shell

sanic src.sanic-domonic-h5bp.app
```

Note that Sanic does not officially support running on Windows.

## File mapping from H5BP

The files from a standard download of H5BP 8.0 maps to the following files in
this template project:

```text
h5bp
│
├── css
│   ├── main.css                      ⇒ ./src/sanic-domonic-h5bp/static/css/
│   └── normalize.css                 ⇒ ./src/sanic-domonic-h5bp/static/css/
│
├── doc                               ¬ Not included
│
├── img                               ⇒ ./src/sanic-domonic-h5bp/static/img/
│
├── js
│   ├── vendor
│   │   └── modernizer-3.11.2.min.js  ⇒ ./src/sanic-domonic-h5bp/static/js/vendor/
│   ├── main.js                       ⇒ ./src/sanic-domonic-h5bp/static/js/
│   └── plugins.js                    ⇒ ./src/sanic-domonic-h5bp/static/js/
│
├── .editorconfig                     ⇒ expanded in ./.editorconfig
├── .gitattributes                    ⇒ expanded in ./.gitattributes
├── .gitignore                        ⇒ expanded in ./.gitignore
├── .htaccess                         ¬ Not included
├── 404.html                          ⇏ Implemented in domonic
├── browserconfig.xml                 ⇒ ./src/sanic-domonic-h5bp/static/
├── favicon.ico                       ⇒ ./src/sanic-domonic-h5bp/static/
├── humans.txt                        ⇒ ./src/sanic-domonic-h5bp/static/
├── icon.png                          ⇒ ./src/sanic-domonic-h5bp/static/
├── index.html                        ⇏ Implemented in domonic
├── LICENSE.txt                       ⇒ ./LICENSE
├── package.json                      ¬ Not included
├── package-lock.json                 ¬ Not included
├── robots.txt                        ⇒ ./src/sanic-domonic-h5bp/static/
├── site.webmanifest                  ⇒ ./src/sanic-domonic-h5bp/static/
├── tile.png                          ⇒ ./src/sanic-domonic-h5bp/static/
└── tile-wide.png                     ⇒ ./src/sanic-domonic-h5bp/static/
```

## Thanks to

* The [Sanic](sanic) web server and framework.
* [domonic], the fiendishly good HTML generator library.
* Good old [HTML5 Boilerplate](h5bp).

[black-badge-href]: https://github.com/psf/black
[black-badge-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[domonic]: https://domonic.readthedocs.io/
[h5bp]: https://html5boilerplate.com/
[htmx]: https://htmx.org/
[hyperscript]: https://hyperscript.org/
[pipenv-badge-img]: https://img.shields.io/github/pipenv/locked/python-version/pyxy-dk/sanic-domonic-h5bp
[sanic]: https://sanicframework.org/
