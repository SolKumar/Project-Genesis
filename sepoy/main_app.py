from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_page():
    return "<h3>Hello World again!</h3>"

if __name__ == "__main__":
    app.run(debug=False)


