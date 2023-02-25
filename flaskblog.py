# save this as app.py
from flask import Flask, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e8d1ea0a5619e99a538df1ffe1ade916'

posts = [
        
    {
    'author': 'Ndallah Njongmeta',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'February 23, 2023'
    },
    {
    'author': 'Nuria Asad',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'February 24, 2023'
    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger') 
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)