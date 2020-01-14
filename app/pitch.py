from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

posts = [
    {
        'author': 'Thee Mike',
        'title': ' Pitch 1',
        'content': 'First pitch content',
        'date_posted': 'May 6,2020'
    },
    {
        'author': 'Mary Jane',
        'title': 'pitch 2',
        'content': 'Second pitch content',
        'date_posted': 'May 6, 2020'
    }
]


@app.route("/")
# @app.route("/home.html")
def home():
    return render_template('/home.html', posts=posts)


@app.route("/about.html")
def about():
    return render_template('/about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)
