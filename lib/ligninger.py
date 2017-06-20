import os
import sympy
import random
from lib.misc import var,gen_koef,gengiv

def opg_linear_ligning(x="", rhs = None, var_coeffs=True):

    if not x:
        x = random.choice(var)
    elif isinstance(x, list):
        x = random.choice(x)

    fjern = [x.upper(), x.lower()]
    x = sympy.Symbol(x)
    c1, c2, c3, c4 = gen_koef(4, var_coeffs=var_coeffs, reduce=False, exclude = fjern)
    lhs = c1*x + c2
    rhs = c3*x + c4
    e = sympy.Eq(lhs, rhs)
    loes = [gengiv(ex, x) for ex in sympy.solve(e, x)]
    return "Løs for $%s$ : %s" % (x, gengiv(e)), loes


def opg_andengradsligning(x="", rhs = None, var_coeffs=True):
    return 'opg','loes'


def opg_redurcer(x="", rhs = None, var_coeffs=True):
    return 'opg','loes'
