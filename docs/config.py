# Configuration file for the Sphinx documentation builder.

from pathlib import Path
import sys

# ---------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------

project = "HippoGenes"
author = "Alexander Ngo"
copyright = "2026, Alexander Ngo"

# ---------------------------------------------------------------------
# General configuration
# ---------------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "nbsphinx",
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
]

# Don't execute notebooks during the documentation build
nbsphinx_execute = "never"

# ---------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Show only the logo (optional)
html_logo = "logo.png"
html_theme_options = {
    "logo_only": True,
}