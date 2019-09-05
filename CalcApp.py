# -*- coding: utf-8 -*-
"""
A web application that utilizes the GraphingCalc.py functions.
"""

from flask import Flask, render_template, request
from urllib.parse import quote
import app.GraphingCalc as GC
from app.models import db, PostSingle, PostMulti

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/calc_app'
db.init_app(app)

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
    file = './images/' + quote(subject + '&' + function) + '.png'
    
    if subject == 'single':
        try:
            result = GC.single_var(function, './static/'+file)

            if not db.session.query(PostSingle).filter(PostSingle.func == function).count():
                db_post = PostSingle(function, file)
                db.session.add(db_post)
                db.session.commit()

            return render_template('results.html',
                                   subject = subject,
                                   function=function, 
                                   first_deriv = result[0],
                                   second_deriv = result[1],
                                   third_deriv = result[2],
                                   integ_sol = result[-1],
                                   img_file = file)
        except:
            return render_template('index.html')

    else:
        try:
            result = GC.multi_var(function, './static/'+file)

            if not db.session.query(PostMulti).filter(PostMulti.func == function).count():
                db_post = PostMulti(function, file)
                db.session.add(db_post)
                db.session.commit()

            return render_template('results.html', 
                                   subject = subject,
                                   function=function, 
                                   partial_X = result[0],
                                   partial_Y = result[1],
                                   partial_XX = result[2],
                                   partial_XY = result[3],
                                   partial_YY = result[4],
                                   integ_sol = result[-1],
                                   img_file = file)
        except:
            return render_template('index.html')

if __name__ == "__main__":
    app.run(threaded=True)
