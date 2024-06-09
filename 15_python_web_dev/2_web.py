# Routing

# can route in this way using the @app.route() decorator to tell us the route of the page and if we want to render an existing html page, we use render_template()
# pages need to be in a templates folder

from markupsafe import escape


@app.route("/")
def index():
    return render_template('./index.html')

# Static files - js and css
# pages need to be in a static folder

# then in the html files, just need to add the correct route with static/filename.css(js)


# FAVICON
# can youse the below code to add in the favicon. The image itself has to be in the static folder

# <link
#   rel="shortcut icon"
#   href="{{ url_for('static', filename='favicon.png') }}"
# />

# {{}} - this holds a python expression that needs to be evaluated. It is from "jinja" which is built into flask.


# variable rules
# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.


# https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules


@app.route("/<username>")
def index1(username=None):
    return render_template('./index.html', name=username)


# in index.html
{{name}}

# now when you go to any route with /wordshere the index.html will show wordshere


# MIME Types
# Multipurpose internet mail extension
# Browsers use the MIME type, not the file extension, to determine how to process a URL, so it's important that web servers send the correct MIME type in the response's Content-Type header. If this is not correctly configured, browsers are likely to misinterpret the contents of files, sites will not work correctly, and downloaded files may be mishandled.

# this gets put into the "Content-Type" where we place application/javascript or image/png. Something that tells the browser how to interpret the file being sent.


# FREE WEB TEMPLATE SITES
# https://themewagon.com/author/mashuptemplate/
# https://html5up.net/
# https://www.creative-tim.com/bootstrap-themes/free
