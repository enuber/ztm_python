# send emails using python
# there is a new email package for 3.6 python and later...so this is current latest way to do this.
# note that this does not actually work. it is the basic setup but restrictions have changed, have to

# https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps


# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
# article above is why use pathlib vs os.path

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path - very similar

html = Template(Path('email.html').read_text())

email = EmailMessage()
email['from'] = 'Erik'
email['to'] = 'hz14000@aol.com'
email['subject'] = 'testing our app'
email.set_content(html.substitute(name='anyname'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('enuber@gmail.com', '87FE&te32')
    smtp.send_message(email)
    print('email sent')
