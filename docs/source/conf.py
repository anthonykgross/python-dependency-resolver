# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

import python_dependency_resolver


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'python-dependency-resolver'
copyright = '2024, Anthony K GROSS'
author = 'Anthony K GROSS'

version = python_dependency_resolver.get_version()

pygments_style = "sphinx"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
}

# https://www.sphinx-doc.org/fr/master/usage/extensions/autodoc.html
autodoc_default_options = {
    'members': True,
    'inherited-members': False,
    'show-inheritance': True,
    'special-members': '__init__'
}

html_context = {
    "display_github": True,
    "github_user": "anthonykgross",
    "github_repo": "python-dependency-resolver",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}
