from flask import Flask, abort, render_template
from jinja2 import TemplateNotFound


app = Flask(__name__)
app.url_map.merge_slashes = False

@app.route("/<path:name>") 
def serve(name):
    for symbol in ("~", "//", ".."): #checks for any forbidden symbol, stops it with a 403
        if symbol in name:
            abort(403)

    if not (name.endswith(".html") or name.endswith(".css")): # only .htl and .css are served
        abort(404)

    try:
        return render_template(name) #tries to load file from templates, if it exists it sends its contents with a 200 OK statys
    except TemplateNotFound:
        abort(404) # if not abort

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
