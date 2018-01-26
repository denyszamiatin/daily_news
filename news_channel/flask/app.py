from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '1234567890qwerty'

@app.route('/')
def index():
    message = session.pop('message', '')
    return render_template('index.html', message=message)

@app.route('/search')
def search():
    message = website = keywords = ''
    website = request.args.get('website', '')
    keywords = request.args.get('keywords', '')
    return render_template(
        'search.html',
        website=website,
        keywords=keywords,
        message=message
    )

@app.route('/result')
def result():
    result = request.args
    return render_template("result.html",result = result)


if __name__ == '__main__':
    app.run(debug=True)

