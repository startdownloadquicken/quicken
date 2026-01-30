project = 'Quicken Desktop Guide'
author = 'Quicken Desktop Team'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

# Normal Sphinx static (CSS/JS)
html_static_path = ['_static']

# 🔥 ULTRA-ADVANCED: Copy ROOT files (including index.html) to final HTML output
html_extra_path = ['.']
