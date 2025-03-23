from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Deploying Flask App at Vercel foor MLOps"

if __name__ == "__main__":
    app.run(debug=True)
