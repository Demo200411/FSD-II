from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result": a + b}

if __name__ == "__main__":
    app.run(debug=True)