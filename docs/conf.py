# -*- coding: utf-8 -*-
#

import unittest
import doctest
import sys
import os

curdir = os.getcwd()
sys.path.insert(0, curdir + os.sep)
sys.path.insert(0, curdir + os.sep + '..' + os.sep)
sys.path.insert(0, curdir + os.sep + '..' + os.sep + ".." + os.sep)

from rssbot import __version__

needs_sphinx='1.1'
nitpick_ignore=[
                ('py:class', 'builtins.BaseException'),
               ]

extensions=[
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]
autosummary_generate=True
#autodoc_default_flags=['members', 'undoc-members', 'private-members', 'special-members', 'inherited-members', 'show-inheritance', 'ignore-module-all', 'exclude-members']
autodoc_default_flags=['members', 'undoc-members', 'private-members', "imported-members", 'show-inheritance', 'ignore-module-all']
autodoc_member_order='alphabetical'
autodoc_member_order='groupwise'
autodoc_docstring_signature=True
autoclass_content="class"
doctest_global_setup=""
doctest_global_cleanup=""
doctest_test_doctest_blocks="default"
trim_doctest_flags=True
doctest_flags=doctest.REPORT_UDIFF
templates_path=['_templates',]
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
project = "RSSBOT"
version = '%s' % __version__
release = '%s' % __version__
language = ''
today = ''
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build', "_sources", "_templates"]
default_role = ''
add_function_parentheses = True
add_module_names = False
show_authors = True
pygments_style = 'sphinx'
modindex_common_prefix = [""]
keep_warnings = True
html_theme = "haiku"
html_theme_path = []
html_short_title = "RSSBOT %s" % __version__
html_favicon = "rssbotsmile.png"
html_static_path = []
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = True
html_use_index = True
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = True
html_use_opensearch = 'http://rssbot.rtfd.io/'
html_file_suffix = '.html'
rst_prolog = """.. image:: rssbotline2.png
    :height: 2.7cm
    :width: 100%

.. title:: no copyright, no LICENSE, placed in the public domain
"""


htmlhelp_basename = 'pydoc'
intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', None),
                      }
intersphinx_cache_limit=2
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}
