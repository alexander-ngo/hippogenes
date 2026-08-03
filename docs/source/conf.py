# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

import hippogenes

# -- Project information ----------------------------------------------------

project = "hippogenes"
copyright = "2026, Ngo"
author = "Ngo"

release = hippogenes.__version__
version = hippogenes.__version__

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",       # parse NumPy/Google-style docstrings
    "sphinx.ext.viewcode",       # add "[source]" links next to autodoc entries
    "sphinx.ext.intersphinx",
    "sphinx_design",             # tabs, grids, cards for nicer layout
    "sphinx_copybutton",         # copy-to-clipboard button on code blocks
    "nbsphinx",                  # render Jupyter notebooks as tutorial pages
]

# -- Autodoc / autosummary ----------------------------------------------------

autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"

# -- Napoleon (NumPy-style docstrings) ---------------------------------------

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_rtype = False

# -- Intersphinx --------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}
intersphinx_disabled_domains = ["std"]

# -- nbsphinx -----------------------------------------------------------------

# Notebooks are pre-run and committed with their outputs, so don't
# re-execute them during the docs build (keeps builds fast and reliable
# on ReadTheDocs, where heavy downloads/compute aren't available).
nbsphinx_execute = "never"
nbsphinx_allow_errors = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints", "Thumbs.db", ".DS_Store"]

# The master toctree document.
root_doc = "index"

# -- Options for HTML output --------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_logo = "logo.png"
html_favicon = "logo.png"

html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "collapse_navigation": False,
    "navigation_depth": 3,
    "style_external_links": True,
}

html_context = {
    "display_github": True,
    "github_user": "alexander-ngo",
    "github_repo": "hippogenes",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# -- Options for EPUB output --------------------------------------------------

epub_show_urls = "footnote"