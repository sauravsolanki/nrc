from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.htm')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/studio')
def studio():
    return render_template('studio.htm')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)
