# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CIDS-Sim'
copyright = '2025, Aulia Arif Wardana, GNU GPL v3.0'
author = 'Aulia Arif Wardana'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "resource/logo-cids.jpg"
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
