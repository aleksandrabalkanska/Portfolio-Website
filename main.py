from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from Project import Project
import secrets
import requests

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
Bootstrap5(app)

projects = requests.get("https://api.npoint.io/f4984877ce0243630b82").json()

project_objects = []
for project in projects:
    project_obj = Project(project["title"], project["link"], project['description'], project["image_path"],
                          project["image_alt"])
    project_objects.append(project_obj)


@app.route("/")
def home():
    return render_template("index.html", projects=project_objects)


@app.route("/surprise")
def surprise():
    return render_template("surprise.html")

if __name__ == '__main__':
    app.run(debug=True)
