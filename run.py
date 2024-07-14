from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Главная')


@app.route('/parks')
def parks():
    return render_template("parks.html")


@app.route('/nature_reserves')
def nature_reserves():
    return render_template("nature_reserves.html")


@app.route('/recycling_points')
def recycling_points():
    return render_template("recycling_points.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
