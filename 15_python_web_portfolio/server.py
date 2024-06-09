from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('./index.html')

# can do this instead of list each page separately


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)


# @app.route('/about.html')
# def about():
#     return render_template('./about.html')


# @app.route('/works.html')
# def work():
#     return render_template('./works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

    # first is file to write too, in our case database2 is what we just opened.
    # delimiter, quotechar and quoting are options we can give to tell how we want it to write
    # what is below is fairly standard for these fields but can read more on what options are available and what they do. https://docs.python.org/3/library/csv.html


def write_to_csv(data):
    with open('db.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

    # in the contact.html we adjusted the form to have submit_form be the action and method be POST
    # because we gave name attributes to the form elements we also get back the email, subject and message in the form data.
    # note that to use these methods we have to bring in from flask request and redirect which are up on top line.


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # gives us the information in a dictionary. could do request.form['email'] to get one attribute
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong please try again.'
