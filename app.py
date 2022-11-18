from flask import Flask, render_template, request, flash
from main import st


app = Flask(__name__)
app.secret_key = "FlaskIsTheSuper"

@app.route("/")
def index():
	flash("Киньте ссылку на видео")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	s = (str(request.form['name_input']))
	st(s)
	path = "text.txt"
	return render_template("output.html", path=path)



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)