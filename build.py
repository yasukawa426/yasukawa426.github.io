import os
import shutil
import re

# Paths
CONTENT_DIR = "content"
RAW_DIR = "raw"
DIST_DIR = "dist"
LAYOUT_FILE = "layout.html"

# Load layout
with open(LAYOUT_FILE, "r", encoding="utf-8") as f:
    layout = f.read()

# Clear and recreate dist
if os.path.exists(DIST_DIR):
    shutil.rmtree(DIST_DIR)
os.makedirs(DIST_DIR, exist_ok=True)

# Helper to create output folder
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# Process content folder
for root, dirs, files in os.walk(CONTENT_DIR):
    # Skip templates folder
    if "templates" in dirs:
        dirs.remove("templates")
    
    for file in files:
        if file.endswith(".html"):
            content_path = os.path.join(root, file)
            with open(content_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract title if exists
            title = "My Site"
            m = re.search(r'<!--\s*title:\s*(.*?)\s*-->', content)
            if m:
                title = m.group(1)
                # Remove the comment from content
                content = re.sub(r'<!--\s*title:.*?-->', '', content, count=1)

            # Inject content and title into layout
            page_html = layout.replace("{{content}}", content).replace("{{title}}", title)

            # Determine relative path in dist
            rel_path = os.path.relpath(root, CONTENT_DIR)
            out_dir = os.path.join(DIST_DIR, rel_path)
            ensure_dir(out_dir)

            # Write output
            out_file = os.path.join(out_dir, file)
            with open(out_file, "w", encoding="utf-8") as out:
                out.write(page_html)

# Copy raw folder as-is
if os.path.exists(RAW_DIR):
    shutil.copytree(RAW_DIR, os.path.join(DIST_DIR, RAW_DIR))
    
print(f"✅ Build complete! Files are in the '{DIST_DIR}' directory.")
