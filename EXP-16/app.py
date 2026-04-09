from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running"

@app.route("/add")
def add():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        return {"result": a + b}
    except:
        return {"error": "Invalid input"}, 400

if __name__ == "__main__":
    app.run(debug=True)