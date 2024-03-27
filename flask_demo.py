from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/next_poem')
def next_poem():
    return render_template('next_poem.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)