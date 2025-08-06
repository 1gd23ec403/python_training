from flask import Flask,render_template
app = Flask(__name__)
@app.route('/home')
def loadhome():
    return render_template('home.html')

@app.route('/contact')
def loadconact():
    return render_template('contact.html')

    @app.route('/about')
def loadabout():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
    