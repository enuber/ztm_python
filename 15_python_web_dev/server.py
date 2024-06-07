from flask import Flask

app = Flask(__name__)
# print(app) # <Flask 'server'>
# ∏print(__name__)  # __main__

# @app.route is a decorator. when we hit '/'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


print(hello_world())  # Hello, World!
