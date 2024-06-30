from flask import Flask, render_template, request, Response
import numpy as np
import matplotlib.pyplot as plt
import io

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

def plot_hist_mod():
    fig_mod = create_figure_mod()
    fig_mod.savefig('static/histogram_mod.png')

def plot_hist_med():
    fig_med = create_figure_med()
    fig_med.savefig('static/histogram_med.png')

def create_figure_med():
    oceny = [2, 3, 3.5, 3.5, 3.5, 4.5, 4, 4, 4.5, 5, 5, 5.5, 5] 
    fig_med, ax = plt.subplots()
    ax.hist(oceny, bins=15, alpha=0.75, color='blue')
    ax.set_title('Histogram')
    ax.set_xlabel('Wartości')
    ax.set_ylabel('Częstotliwość')
    return fig_med

def create_figure_mod():
    oceny = [2, 3, 3.5, 3.5, 3.5, 4.5, 4, 4.5, 5, 5, 5.5, 5] 
    fig_mod, ax = plt.subplots()
    ax.hist(oceny, bins=15, alpha=0.75, color='blue')
    ax.set_title('Histogram')
    ax.set_xlabel('Wartości')
    ax.set_ylabel('Częstotliwość')
    return fig_mod    

@app.route('/kalkulator', methods=['GET', 'POST'])
def calculate():
    weighted_average = None
    error_message = None
    if request.method == 'POST':
        
        values = request.form['values']
        weights = request.form['weights']
            
        values = [float(v) for v in values.split(',')]
        weights = [float(w) for w in weights.split(',')]
            
        if len(values) != len(weights):
            raise ValueError("Liczba wartości i wag musi być taka sama.")
            
        weighted_average = sum(v * w for v, w in zip(values, weights)) / sum(weights)
        

    return render_template('kalkulator.html', weighted_average=weighted_average, error_message=error_message)

if __name__ == '__main__':
    plot_hist_mod()
    plot_hist_med()
    app.run(debug=True)
    

