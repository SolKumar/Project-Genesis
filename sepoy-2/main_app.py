from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

posts = [
    {
        'author': 'Kumar',
        'title': 'Creating your first flask application',
        'content': 'Follow the steps here : https://github.com/SolKumar/Project-Genesis/tree/main/volunteer',
        'date_posted': '25 Feb, 2024'
    },
    {
        'author': 'Teja',
        'title': 'Adding HTML templates to your first flask application',
        'content': 'Follow the steps here : https://github.com/SolKumar/Project-Genesis/tree/main/sepoy',
        'date_posted': '26 Feb, 2024'
    },
    {
        'author': 'Kumar',
        'title': 'Using bootstrap for UI and turning simple flask app into blog app',
        'content': 'Follow the steps here : https://github.com/SolKumar/Project-Genesis/tree/main/sepoy-2',
        'date_posted': '13 April, 2024'
    }
]


@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home_page():
    return render_template("home.html",posts=posts,title="Home")

@app.route("/about",methods=["GET","POST"])
def about_page():
    return render_template("about.html",title="About")

                 
if __name__ == "__main__":
    app.run(debug=True) # Set to True for debugging


