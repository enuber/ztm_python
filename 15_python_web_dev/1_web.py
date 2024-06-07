# For web python can write the server. Doesn't matter what langauge the server is written in, but this is where python can come in.

# http.server can be used to build a server but, it isn't for production, it has only basic security.

# FLASK - a tool that can be used to create a server. lean and small to do things fast (django - another one. It is a really big framework)

# To start you do the following...(this is the standard way to do it.)

# mkdir myproject
# cd myproject
# python3 -m venv .venv

# this would also work where you place the venv into your actual project folder instead of creating a separate folder called venv to be the virtual environment.

# mkdir myproject
# python3 -m venv myproject
# cd myproject

# then to actually run it you have to activate it with...

# . venv/bin/activate
# or depending on the way you installed venv you may need to do the below from outside the folder
# . myproject/bin/activate or . bin/activate from within the folder itself


# this will allow you to install packages and have them be project based rather than global

# then you need to install flask
# pip3 install Flask

# don't call your server flask.py as it's a conflict

# to run the server where filename is the server.py file or whatever .py file you want to run as the server
# flask --app filename run


# Note command shift p then search for python select interpreter. Choose the virtual environment you created to run as interpreter.

# remember to add your .venv or files to the gitignore file so they don't get copied over.

# debug mode - allows you to work in realtime without having to cancel things and restart. If you refresh your changes show instead of starting/stopping server.
#  flask --app filename run --debug


# quick hit of what is above

# mkdir myproject
# cd myproject
# python3 -m venv .venv
# . venv/bin/activate
# pip3 install Flask
# flask --app filename run

# .gitignore
# venv/
