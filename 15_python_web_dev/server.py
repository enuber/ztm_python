from flask import Flask, render_template

app = Flask(__name__)
# print(app) # <Flask 'server'>
# ∏print(__name__)  # __main__

# @app.route is a decorator. when we hit '/'


@app.route("/")
def index():
    return render_template('./index.html')


@app.route("/<username>")
def index1(username=None):
    return render_template('./index.html', name=username)

# int means has to be an integer


@app.route("/<username>/<int:post_id>")
def index2(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)


@app.route("/about.html")
def about():
    return render_template('./about.html')


@app.route('/blog')
def blog():
    return "<p>My Blog Thoughts</p>"


@app.route('/')
def blog2():
    return "<p>This is my dog</p>"
