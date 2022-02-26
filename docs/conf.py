# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../labtools'))


project = 'labtools'
copyright = '2020, wehr lab'
author = 'wehr lab'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',     # automatically document packages
    'sphinx.ext.autosummary', # create summary tables on api doc pages
    'sphinx.ext.intersphinx', # include documentation from other projects
    'sphinx.ext.todo',        # todo directive
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon', # parse google style docstrings
    'sphinx.ext.graphviz',
    "myst_parser"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#####
# Napoleon
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config
napoleon_google_docstring = True
# napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
# napoleon_include_special_with_doc = False
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True
# napoleon_use_keyword = True
# napoleon_custom_sections = None

###
# Autodoc

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'member-order': 'bysource',
    'autosummary': True
}
autoclass_content = "both"
autosummary_generate = True

autodoc_mock_imports = ['pigpio']

# autogenerate anchors for markdown headers
myst_heading_anchors = 3

graphviz_output_format = "svg"

######
# Todo extension

todo_include_todos = True

########
# Intersphinx

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('https://numpy.readthedocs.io/en/latest/', None),
                       'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
                       #'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
                       'prey_capture_python': ('https://preycap.readthedocs.io/en/latest/', None)}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']