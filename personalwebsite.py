from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def home():
   return render_template("homepage.html")

@app.route('/about')
def about():
   return "About"

@app.route('/resume')
def resume():
   return "Resume"

@app.route('/portofolio')
def portofolio():
   return "Portofolio"

@app.route('/contact')
def contact():
   return "Contact"

if __name__ == '__main__':
    app.run(debug = True)