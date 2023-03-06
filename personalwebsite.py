from flask import Flask,render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'e338fbef50b0c3'
app.config['MAIL_PASSWORD'] = 'fee78b2af26253'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

def sendContactForm(result):
   msg = Message('Contact Form from Marabelu Website' , sender = result['email'], recipients=['test@gmail.com'])
   msg.body = """
      You just received a Contact Form.

      Name : {}
      Email : {}
      Subject : {}
      Message : {}
   """.format(result['name'],result['email'],result['subject'],result['message'])

   mail.send(msg)


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
   if request.method == 'POST':
      result = {}
      
      result['name'] = request.form["inputName"]
      result['email'] = request.form["inputEmail"].replace(' ', '')
      result['subject'] = request.form["inputSubject"]
      result['message'] = request.form["inputMessage"]

      sendContactForm(result)

      return render_template("contact.html")
   
   return render_template("contact.html")



if __name__ == '__main__':
    app.run(debug = True)