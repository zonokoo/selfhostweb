import re

# Read your HTML file
with open('templates/index1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS references
html = re.sub(
    r'href="\./index_files/([^"]+\.css)"',
    r'href="{{ url_for(\'static\', filename=\'css/\1\') }}"',
    html
)

# Replace JS references (remove .download extension)
html = re.sub(
    r'src="\./index_files/([^"]+)\.js\.download"',
    r'src="{{ url_for(\'static\', filename=\'js/\1.js\') }}"',
    html
)

# Replace image references
html = re.sub(
    r'src="\./index_files/([^"]+\.(jpg|png))"',
    r'src="{{ url_for(\'static\', filename=\'images/\1\') }}"',
    html
)

# Replace font references in CSS URLs
html = re.sub(
    r'url\("_assets/fonts/([^"]+)"\)',
    r'url("{{ url_for(\'static\', filename=\'fonts/\1\') }}")',
    html
)

# Write updated HTML
with open('templates/index_fixed.html', 'w', encoding='utf-8') as f:
    f.write(html)