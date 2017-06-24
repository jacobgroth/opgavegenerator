import sympy
import random
from string import ascii_lowercase
from string import ascii_uppercase
from copy import copy

var = [i for i in ascii_uppercase + ascii_lowercase]
var.remove("l")
var.remove("o")
var.remove("O")
var.remove("I")
var.remove("i")

cifre = list(range(-26,26))
cifre_nozero = cifre
cifre_nozero.remove(0)


def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

def gen_koef(n, exclude=["x", "X"], first_nonzero=True, var_coeffs=False,
                        reduce=True):
    if var_coeffs:
        selection = copy(cifre_nozero + var)
        for i in exclude:
            selection.remove(i)
    else:
        selection = cifre_nozero
    coeffs = []
    for i in iter(range(n)):
        c = random.choice(selection)
        if isinstance(c, str):
            c = sympy.Symbol(c)
        if reduce and random.randint(0,1):
            c = 0
        coeffs.append(c)
    if first_nonzero and coeffs[0] == 0:
        coeffs[0] = random.choice(selection)
    return coeffs


def poly1(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(gen_koef(2)))])
    return vals

def poly2(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(gen_koef(3)))])
    return vals

def poly3(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(gen_koef(4)))])
    return vals


_funktioner = [sympy.sin, sympy.cos, sympy.tan, sympy.ln, sympy.sqrt, sympy.exp,
              lambda a: a, poly1, poly2, poly3]

_polynomier= [lambda a: a, poly1, poly2, poly3]


def gengiv(udtryk, lhs=""):

    venstre = "$$"
    if lhs:
        venstre = "$$%s =" % lhs
    return ''.join([venstre, sympy.latex(udtryk), "$$"])