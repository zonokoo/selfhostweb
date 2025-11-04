import re

# Read your HTML file
with open('templates/social1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS paths
content = re.sub(r'\./DIScord_files/([^"]+\.css)', r"{{ url_for('static', filename='css/\1') }}", content)

# Replace JS paths (and remove .download extension)
content = re.sub(r'\./DIScord_files/([^"]+)\.js\.download', r"{{ url_for('static', filename='js/\1.js') }}", content)

# Replace image paths
content = re.sub(r'\./DIScord_files/([^"]+\.(png|jpg|jpeg|gif|svg))', r"{{ url_for('static', filename='images/\1') }}", content)

# Write back
with open('templates/social1_fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed HTML saved as social1_fixed.html")