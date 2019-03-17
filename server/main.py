from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/cinema')
def index_cinema():
    return render_template("cinema.html")

@app.route('/theatre')
def index_theatre():
    return render_template("theatre.html")

@app.route('/most-popular')
def index_most_popular():
    return render_template("most-popular.html")

@app.route('/theatre-tab')
def index_theatre_tab():
    return render_template("theatre-tab.html")


@app.route('/cinema_data')
def cinema_data():
    return send_from_directory('static', 'kino_arena.json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)