# from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
# from app.forms import RegistrationForm, LoginForm
#
# app = Flask(__name__, template_folder='templates')
# app.config['SECRET_KEY'] = 'Backrow'
# posts = [
#     {
#         'author': 'Thee Mike',
#         'title': ' Pitch 1',
#         'content': 'First pitch content',
#         'date_posted': 'May 6,2020'
#     },
#     {
#         'author': 'Mary Jane',
#         'title': 'pitch 2',
#         'content': 'Second pitch content',
#         'date_posted': 'May 6, 2020'
#     }
# ]
#
#
# @app.route("/")
# def home():
#     return render_template('/home.html', posts=posts)
#
#
# @app.route("/about")
# def about():
#     return render_template('/about.html', title='about')
#
#
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template("/Register.html", title='Register', form=form)
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm
#     if form.validate_on_submit():
#         # dummy data
#         if form.email.data == admin@pitch.com and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for(home))
#         else:
#             flash('Login Unsuccessfull. Check username and password', 'success')
#             # dummy data
#     return render_template('/Login.html', title='Login', form=form)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)