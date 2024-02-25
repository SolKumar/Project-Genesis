from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route("/")
def root_page():
    return render_template("layout.html")

@app.route("/home",methods=["GET","POST"])
def home_page():
    return render_template("home.html")

@app.route("/about",methods=["GET","POST"])
def about_page():
    return render_template("about.html")

                 
if __name__ == "__main__":
    app.run(debug=True) # Set to True for debugging


