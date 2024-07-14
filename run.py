from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Создание подключения к базе данных
conn = sqlite3.connect('posts.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы, если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
''')

# Закрытие соединения
conn.close()


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


@app.route('/posts')
def posts():
    # Получение данных из базы данных
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return render_template('posts.html', posts=posts)


@app.route('/creature', methods=['GET', 'POST'])
def creature():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Сохранение данных в базу данных
        conn = sqlite3.connect('posts.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('creature.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
