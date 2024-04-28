import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with a database)
users = {'john': {'password': 'password', 'id': 1, 'points': 0},
         'mary': {'password': '12345', 'id': 2, 'points': 0}}

# User data for testing
user_data = {'username': 'john', 'user_id': 1}  # Example user data

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/about')
def about():
    return 'This is the About Page.'

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user_profile.html', username=username)

@app.route('/jj')
def index():
    title = "Flask Jinja Example"
    greeting = "Hello, World!"
    items = ["Apple", "Banana", "Orange"]
    return render_template('jinja.html', title=title, greeting=greeting, items=items)

@app.route('/post/<string:post_id>')
def show_post(post_id):
    return render_template('post.html', post_id=post_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user_data['username'] = username
            user_data['user_id'] = users[username]['id']
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = len(users) + 1  # Generate user ID
        users[username] = {'password': password, 'id': user_id, 'points': 0}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    username = user_data['username']
    user_id = user_data['user_id']
    bg_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))  # Random background color
    return render_template('dashboard.html', username=username, user_id=user_id, bg_color=bg_color)

@app.route('/farm')
def farm():
    user_id = user_data['user_id']
    return render_template('farm.html', user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)
