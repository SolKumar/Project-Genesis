from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_page():
    return "<h1>This is my first application</h1>"

                 
if __name__ == "__main__":
    app.run(debug=False) # Set to True for debugging


