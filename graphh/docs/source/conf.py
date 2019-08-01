# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))
import graphh
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'graphh'
copyright = '2019, Maëlle Cosson, Pauline Hamon-Giraud, Clément Caillard and Romain Tavenard'
author = 'Maëlle Cosson, Pauline Hamon-Giraud, Clément Caillard and Romain Tavenard'

# The full version, including alpha/beta/rc tags
release = graphh.__version__

# The master toctree document.
master_doc = 'index'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
# autodoc_default_flags = ['members', 'inherited-members']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
