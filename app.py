from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "Post":
        note = request.args.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route("/thankyou", methods=['GET'])
def thankyou_fun():
    return render_template("thankyou.html")

@app.route("/Delete", methods=['GET'])
def Delete_fun():
    return render_template("Delete.html")

if __name__ == '__main__':
    app.run(debug=True)
    