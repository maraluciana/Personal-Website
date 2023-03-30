from flask import Flask,render_template,request,flash,redirect,url_for
import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, Optional
from flask_recaptcha import ReCaptcha


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app = Flask(__name__)

app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('RECAPTCHA_PRIVATE_KEY')
app.secret_key = os.environ.get('FLASK_SECRET_KEY')


class ContactForm(FlaskForm):
   inputName = StringField('name', validators=[InputRequired(), Length(max=50)])
   inputSubject = StringField('subject', validators=[InputRequired(), Length(max=50)])
   inputEmail = StringField('email', validators=[InputRequired(), Length(max=100)])
   inputMessage = TextAreaField('message', validators = [InputRequired(), Length(max=5000)])
   recaptcha = RecaptchaField()


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
   

def automatedMessage(result):
   try:
      email_sender = os.getenv('MAIL_USERNAME_SENDER')
      email_receiver = result['email']
      password = os.getenv('MAIL_PASSWORD')
      mail_server = os.getenv('MAIL_SERVER')
      mail_port = os.getenv('MAIL_PORT')

      message = """
         Thank you for your message. This is an automated response to let you know that I have received your message via marabelu.ro and will respond as soon as possible.
         If your matter is urgent, please don't hesitate to call me at 0722618765. Otherwise, I will get back to you as soon as I can.

         You can find below a summary of the information you provided in the contact form:
         
         Name : {}
         Email : {}
      
         Message : {}
         
         Best regards,
         Mara-Luciana Belu
         """.format(result['name'],result['email'],result['message'])

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = result['subject']
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
   form = ContactForm()

   alert_code = 'waiting'
   logging = os.getenv('LOGGING')

   if request.method == 'POST':
      if form.validate_on_submit():
         recaptcha = ReCaptcha()
         if not recaptcha.verify():
            flash('Invalid reCAPTCHA. Please try again.')
            return redirect(url_for('contact'))
         
         result = {}
         
         result['name'] = request.form["inputName"]
         result['email'] = request.form["inputEmail"].replace(' ', '')
         result['subject'] = request.form["inputSubject"]
         result['message'] = request.form["inputMessage"]


         alert_code = sendContactForm(result)
         automatedMessage(result)

         return render_template("contact.html", alert = alert_code, logging = logging, form=form)
   
   return render_template("contact.html", alert = alert_code, logging = logging, form=form)



if __name__ == '__main__':
    app.run(debug = True)
