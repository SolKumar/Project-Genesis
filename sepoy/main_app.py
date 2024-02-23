from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def root_page():
    return "<h3>Hello World again!</h3>"

@app.route("/home",methods=['GET','POST'])
def home_page():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


