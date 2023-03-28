from flask import Flask,render_template,request
import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app = Flask(__name__)

def sendContactForm(result):
   try:
      email_sender = os.getenv('MAIL_USERNAME_SENDER')
      email_receiver = os.getenv('MAIL_USERNAME_RECEIVER')
      password = os.getenv('MAIL_PASSWORD')
      mail_server = os.getenv('MAIL_SERVER')
      mail_port = os.getenv('MAIL_PORT')

      message = """
         You just received a Contact Form.

         Name : {}
         Email : {}
      
         Message : {}
         """.format(result['name'],result['email'],result['message'])

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = result['subject']
      em['Reply-To'] = result['email']
      em.set_content(message)
      
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL(mail_server, mail_port, context=context) as smtp:
         smtp.login(email_sender, password)
         smtp.sendmail(email_sender, email_receiver, em.as_string())
   except Exception as e:
      return e
   else:
      return 'success'


@app.errorhandler(404)
def not_found(e):
   return render_template("404.html")

@app.route('/')
def home():
   return render_template("homepage.html")

@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/resume')
def resume():
   return render_template("resume.html")

@app.route('/portfolio')
def portfolio():
   return render_template("portfolio.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
   alert_code = 'waiting'
   logging = os.getenv('LOGGING')

   if request.method == 'POST':
      result = {}
      
      result['name'] = request.form["inputName"]
      result['email'] = request.form["inputEmail"].replace(' ', '')
      result['subject'] = request.form["inputSubject"]
      result['message'] = request.form["inputMessage"]


      alert_code = sendContactForm(result)

      return render_template("contact.html", alert = alert_code, logging = logging)
   
   return render_template("contact.html", alert = alert_code, logging = logging)



if __name__ == '__main__':
    app.run(debug = True)
