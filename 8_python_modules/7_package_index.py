# pypi.org allows you to search for projects that have already been created so you can do something easier.

# first should check in standard library

# may google...like read csv python3 builtin and if its not in the builtin library then read csv python3 pypi

# to install a pypi file
# pip3 install pyjokes
# pip3 install pyjokes==0.4.0 - to install specific version

import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)


# pip3 list  - gives you a list of packages you have installed
# this also gives you a version list.
# pip3 uninstall pyjokes to remove

# can use pipenv to install specific packages for specific projects
