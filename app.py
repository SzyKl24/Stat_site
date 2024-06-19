from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/contact')
def contact_us():
    return render_template('contact.html')

@app.route('/spis')
def spis():
    return render_template('spis.html')

@app.route('/temat2')
def temat2():
    return render_template('topics/temat2.html')

@app.route('/temat1')
def temat1():
    return render_template('topics/temat1.html')

@app.route('/temat3')
def temat3():
    return render_template('topics/temat3.html')

@app.route('/temat4')
def temat4():
    return render_template('topics/temat4.html')

@app.route('/temat5')
def temat5():
    return render_template('topics/temat5.html')

@app.route('/temat6')
def temat6():
    return render_template('topics/temat6.html')    

@app.route('/temat7')  
def temat7():
    return render_template('topics/temat7.html')    

@app.route('/temat8')   
def temat8():
    return render_template('topics/temat8.html')    

if __name__ == '__main__':
    app.run(debug=True)

