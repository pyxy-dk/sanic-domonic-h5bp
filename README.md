# sanic-domonic-h5bp

![Pipenv - Python version][pipenv-badge-img]
[![Imports: isort][isort-badge-img]][isort-badge-href]
[![Code style: black][black-badge-img]][black-badge-href]

A template repository implementing HTML5 Boilerplate 8.0 in Sanic using the
Domonic framework.

If you need frontend interactivity, this template goes well with e.g.
[HTMX][htmx] and [HyperScript][hyperscript] rather than your run-of-the-mill
bloated JS framework *du jour*.

## π Requirements

* `python-3.8`
* `pipenv`

## π Running

```text
git clone git@github.com:pyxy-dk/sanic-domonic-h5bp.git

cd sanic-domonic-h5bp

pipenv install --dev

pipenv shell

sanic src.sanic_domonic_h5bp.app
```

Note that Sanic does not officially support running on Windows.

## πΊοΈ File mapping from H5BP

The files from a standard download of H5BP 8.0 maps to the following files in
this template project:

```text
h5bp
β
βββ css
β   βββ main.css                      β ./src/sanic_domonic_h5bp/static/css/
β   βββ normalize.css                 β ./src/sanic_domonic_h5bp/static/css/
β
βββ doc                               Β¬ Not included
β
βββ img                               β ./src/sanic_domonic_h5bp/static/img/
β
βββ js
β   βββ vendor
β   β   βββ modernizer-3.11.2.min.js  β ./src/sanic_domonic_h5bp/static/js/vendor/
β   βββ main.js                       β ./src/sanic_domonic_h5bp/static/js/
β   βββ plugins.js                    β ./src/sanic_domonic_h5bp/static/js/
β
βββ .editorconfig                     β expanded in ./.editorconfig
βββ .gitattributes                    β expanded in ./.gitattributes
βββ .gitignore                        β expanded in ./.gitignore
βββ .htaccess                         Β¬ Not included
βββ 404.html                          β Implemented in domonic
βββ browserconfig.xml                 β ./src/sanic_domonic_h5bp/static/
βββ favicon.ico                       β ./src/sanic_domonic_h5bp/static/
βββ humans.txt                        β ./src/sanic_domonic_h5bp/static/
βββ icon.png                          β ./src/sanic_domonic_h5bp/static/
βββ index.html                        β Implemented in domonic
βββ LICENSE.txt                       β ./LICENSE
βββ package.json                      Β¬ Not included
βββ package-lock.json                 Β¬ Not included
βββ robots.txt                        β ./src/sanic_domonic_h5bp/static/
βββ site.webmanifest                  β ./src/sanic_domonic_h5bp/static/
βββ tile.png                          β ./src/sanic_domonic_h5bp/static/
βββ tile-wide.png                     β ./src/sanic_domonic_h5bp/static/
```

## π Thanks to

* The [Sanic][sanic] web server and framework.
* [domonic], the fiendishly good HTML generator library.
* Good old [HTML5 Boilerplate][h5bp].


[black-badge-href]: https://github.com/psf/black
[black-badge-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[domonic]: https://domonic.readthedocs.io/
[h5bp]: https://html5boilerplate.com/
[htmx]: https://htmx.org/
[hyperscript]: https://hyperscript.org/
[isort-badge-href]: https://pycqa.github.io/isort/
[isort-badge-img]: https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336
[pipenv-badge-img]: https://img.shields.io/github/pipenv/locked/python-version/pyxy-dk/sanic-domonic-h5bp
[sanic]: https://sanicframework.org/
