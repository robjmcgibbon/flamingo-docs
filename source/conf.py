# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from docutils import nodes
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FLAMINGO Data Release'
copyright = '2025, John Helly'
author = 'John Helly'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design", "sphinxcontrib.mermaid"]

templates_path = ['_templates']
exclude_patterns = []

html_sidebars = {
    "**": [
        "globaltoc.html",  # Site contents
        "localtoc.html",   # Page contents
    ]
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_title = 'FLAMINGO Data Release'

# The piccolo theme doesn't have an option to have a logo AND text in the nav bar, hence this hack
html_short_title = '<image src="/flamingo/_static/FLAMINGO_navbar_brand_stroke.png" class="flamingo_logo"> FLAMINGO Data Release'

#
# Theme selection
#
# Read the Docs
#html_theme = 'sphinx_rtd_theme'

# Piccolo
html_theme = 'piccolo_theme'
# Don't collapse toc when using Piccolo theme
#html_theme_options = {
#    "globaltoc_collapse": False
#}

# # Scheduled Cosma down times
# import datetime as dt
# downtimes = (
#     dt.date(2026, 6,  1),
#     dt.date(2026, 10, 5),
#     dt.date(2027, 2,  1),
# )
# next_downtime = None
# for downtime in downtimes:
#     nr_days = (downtime - dt.date.today()).days
#     if nr_days < 21 and nr_days > -4:
#         next_downtime = downtime
#         break
# if next_downtime:
#     start_date = downtime.strftime("%d %B")
#     end_date   = (downtime+dt.timedelta(days=4)).strftime("%d %B %Y")
#     banner = "This service will be at risk from "+start_date+" to "+end_date+" due to COSMA <a href='/flamingo/support/at_risk.html'>scheduled down time</a>"
# else:
#     banner = None

# html_theme_options = {
#     "banner_text": banner,
# }

html_theme_options = {
    "banner_text": "This service will be at risk (likely down at times) from 1st to 5th June due to COSMA <a href='/flamingo/support/at_risk.html'>scheduled down time</a>",
}

# Immaterial
#extensions = ["sphinx_immaterial"]
#html_theme = 'sphinx_immaterial'

#
# Additional files needed for the file browser: msgpack library for decoding
# responses, highlight.js syntax highlighter, dompurify and some CSS
# customization.
#
html_css_files = [
    'custom.css',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/styles/default.min.css',
]
html_js_files = [
    'https://unpkg.com/@msgpack/msgpack@2.8.0',
    'https://unpkg.com/dompurify@3.2.3/dist/purify.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/highlight.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/languages/python.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/languages/yaml.min.js',
]


# Coloured inline roles for the SOAP property table.
def _highlight_role(background):
    """Return a docutils role function that wraps text in a highlighted <span>."""

    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        style = (
            f"background-color: {background};"
            " color: black;"
            " padding: 1px 4px;"
            " border-radius: 3px;"
            " font-family: monospace;"
        )
        html = f'<span style="{style}">{text}</span>'
        # raw() node so the HTML passes through unchanged; latex() node is a
        # plain-text fallback for PDF builds.
        node = nodes.raw("", html, format="html")
        latex_node = nodes.raw("", text, format="latex")
        return [node, latex_node], []

    return role


def setup(app: Sphinx):
    app.add_role("avail", _highlight_role("#c8e6c9"))     # light green
    app.add_role("snaponly", _highlight_role("#bbdefb"))  # light blue
    app.add_role("unavail", _highlight_role("#ffcdd2"))   # light red
