# -*- coding: utf-8 -*-
"""
A web application that utilizes the GraphingCalc.py functions.
"""

from flask import Flask, render_template, request
import app.GraphingCalc as GC

app = Flask(__name__)

@app.route('/')
def home():
    """
    The home page that asks for user input.
    """
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
    """
    The results page with the integrated/differentiated function and a graph.
    """
    subject = request.form['calc']
    function = request.form['function']
    #file = "F:/GraphingCalc/static/images/graph0.jpg"
    file = "./static/images/graph.jpg"
    
    if subject == 'single':
        result = GC.single_var(function)
        GC.graph_2d(function, file)
        return render_template('results.html',
                               subject = subject,
                               function=function, 
                               first_deriv = result[0],
                               second_deriv = result[1],
                               third_deriv = result[2],
                               integ = result[-2],
                               integ_sol = result[-1],
                               url = file)
    else:
        result = GC.multi_var(function)
        GC.graph_3d(function, file)
        return render_template('results.html', 
                               subject = subject,
                               function=function, 
                               partial_X = result[0],
                               partial_Y = result[1],
                               partial_XX = result[2],
                               partial_XY = result[3],
                               partial_YY = result[4],
                               integ = result[-2],
                               integ_sol = result[-1],
                               url = file)

if __name__ == "__main__":
    app.run(threaded=True)