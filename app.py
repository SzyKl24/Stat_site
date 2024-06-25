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

@app.route('/wprowadzenie')
def temat2():
    return render_template('topics/wprowadzenie.html')

@app.route('/średnia-arytmetyczna')
def temat1():
    return render_template('topics/sr_aryt.html')

@app.route('/średnia-ważona')
def temat3():
    return render_template('topics/sr_wag.html')

@app.route('/błędy-pomiaru')
def temat4():
    return render_template('topics/bledy.html')

@app.route('/wariacje')
def temat5():
    return render_template('topics/wariacje.html')

@app.route('/odchylenia')
def temat6():
    return render_template('topics/odchylenia.html')    

@app.route('/mediana')  
def temat7():
    return render_template('topics/mediana.html')    

@app.route('/moda')   
def temat8():
    return render_template('topics/moda.html')    

@app.route('/kalkulator')
def kalkulator():
    return render_template('kalkulator.html')

if __name__ == '__main__':
    app.run(debug=True)

