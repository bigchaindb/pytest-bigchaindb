# -*- coding: utf-8 -*-

import sphinx_rtd_theme


extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'pytest-bigchaindb'
copyright = u'2016, BigchainDB'
author = u'BigchainDB'
version = '0.1.0'
release = '0.1.0'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'pytest-bigchaindb_namedoc'
intersphinx_mapping = {'https://docs.python.org/3': None}
