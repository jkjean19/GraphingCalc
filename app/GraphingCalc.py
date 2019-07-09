# -*- coding: utf-8 -*-
"""
Graphing Calculator
For a given math function, the program:
    Graphs
    Differentiates
    Integrates
"""


def preprocess(function):
    """
    Converts a given function from type str to a Sympy object.
    
    Keyword arguments:
    function -- a string type representation of the user's math function
    """
    import sympy    

    expr = function

    while True:
        if '^' in expr:
            expr = expr[:expr.index('^')] + '**' + expr[expr.index('^')+1:]
        else:
            break

    expr = sympy.sympify(expr)
    return expr


def postprocess(function):
    """
    Converts a given function from a Sympy object to a string type.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    expr = str(function)
    
    while True:    
        if '**' in expr:
            expr = expr[:expr.index('**')] + '^' + expr[expr.index('**')+2:]
        else:
            break
    
    return expr    


def graph_2d(function, file="./static/images/graph.png"):
    """
    Graphs a math function on a 2 dimensional space.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    file -- a filename to save the matplotlib figure
    """
    import matplotlib.pyplot as plt
    import numpy as np

    expr = preprocess(function)
    x_axis = np.array(range(-10,11))
    y_axis = np.ones((1,len(range(-10,11))))[0]
    
    for i in range(len(x_axis)):
        y_axis[i] = expr.subs('x', x_axis[i])
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_axis, y_axis)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.savefig(file)
    plt.close()


def diff(function):
    """
    Differentiates a math function.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    import sympy
    
    x = sympy.symbols('x')

    if type(function) == str:
        expr = preprocess(function)
    else:
        expr = function

    return sympy.diff(expr, x)

    
def integral(function):
    """
    Integrates a single variable math function.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    from sympy import symbols, Integral
    
    x = symbols('x')

    if type(function) == str:
        expr = preprocess(function)
    else:
        expr = function

    return Integral(expr, (x))


def single_var(function):
    """
    Calls the diff, integral, and graph_2d functions.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    first_deriv = diff(function)
    second_deriv = diff(first_deriv)
    third_deriv = diff(second_deriv)
    integ = integral(function)
    graph_2d(function)
    
    return [postprocess(first_deriv), postprocess(second_deriv), postprocess(third_deriv), integ, postprocess(integ.doit())]


def graph_3d(function, file="./static/images/graph.png"):
    """
    Graphs a math function on a 3 dimensional space.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    file -- a filename to save the matplotlib figure
    """
    from sympy import symbols
    import numpy as np
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    
    expr = preprocess(function)
    x,y = symbols('x'), symbols('y')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    X, Y = np.mgrid[-5:5, -5:5]
    Z = np.zeros((10,10))
    
    for i in range(len(X)):
        for j in range(len(Y)):
            Z[i][j] = expr.subs([(x, X[i][j]), (y, Y[i][j])])
    
    ax.plot_surface(X, Y, Z, cmap='coolwarm_r')
    plt.savefig(file)
    plt.close()

def partial_diff(function):
    """
    Differentiates a math function of two variables (x and y)
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    from sympy import symbols, diff
    
    x,y = symbols('x'), symbols('y')
    
    if type(function) == str:
        expr = preprocess(function)
    else:
        expr = function
    
    partial_X = diff(expr, x)
    partial_Y = diff(expr, y)
    return partial_X, partial_Y


def dbl_integral(function):
    """
    Evaluates a double integral of a math function with variables x and y.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    from sympy import symbols, Integral
    
    x,y = symbols('x'), symbols('y')

    if type(function) == str:
        expr = preprocess(function)
    else:
        expr = function
    
    return Integral(expr, (x, y))
    

def multi_var(function):
    """
    Calls the partial_diff, dbl_integral, and graph_3d functions.
    
    Keyword arguments:
    function -- a Sympy object representation of the user's math function
    """
    partial_X, partial_Y = partial_diff(function)
    partial_XX, partial_XY = partial_diff(partial_X)
    partial_YX, partial_YY = partial_diff(partial_Y)
    dbl_integ = dbl_integral(function)    
    graph_3d(function)
    
    return [postprocess(partial_X), postprocess(partial_Y), postprocess(partial_XX), 
            postprocess(partial_XY), postprocess(partial_YY), dbl_integ, postprocess(dbl_integ.doit())]
