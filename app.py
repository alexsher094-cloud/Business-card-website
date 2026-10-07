import os
from flask import Flask, render_template

app = Flask(__name__)

PROJECTS_DIR = os.path.join("static", "projects")
AWARDS_DIR   = os.path.join("static", "awards")
ALLOWED_EXT  = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}


def list_images(folder):
    """Возвращает список картинок в папке (отсортированный)."""
    result = []
    if os.path.isdir(folder):
        for name in sorted(os.listdir(folder)):
            ext = os.path.splitext(name)[1].lower()
            if ext in ALLOWED_EXT:
                result.append(name)
    return result


@app.route("/")
def index():
    return render_template(
        "index.html",
        project_files=list_images(PROJECTS_DIR),
        award_files=list_images(AWARDS_DIR),
    )


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)