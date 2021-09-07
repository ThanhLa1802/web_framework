#create by:thanh.la - 07-09- 2021
from flask import Flask, render_template, flash, url_for
from werkzeug.utils import redirect
from forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Thanh deptrai',
        'title': 'Blog Post 1',
        'content': "It is first post!",
        'date_posted': 'September 7, 2021'
    }
]
app = Flask(__name__)
app.secret_key = "0dcea6a90267ed0040313a4616b3a15e"
@app.route("/")

#decorator
@app.route("/home")
def home():
    return render_template('home.html', posts  = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")
@app.route("/register", methods = ["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.user_name.data}', 'success' )
        return redirect(url_for('home'))
        
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = "Login", form = form)
if __name__ == '__main__':
    app.run(debug=True) 