import os
import sympy
import random
from lib.misc import var,gen_koef,gengiv,cifre_nozero,_polynomier

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


def opg_andengradsligning(uafvar="x", rhs = None, integer=[0, 1]):

    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))
    if isinstance(integer, list):
        integer = random.choice(integer)
    if integer:
        r1 = random.choice(cifre_nozero)
        r2 = random.choice(cifre_nozero)
        lhs = (uafvar - r1) * (uafvar - r2)
        lhs = lhs.expand()
        rhs = 0
    else:
        c1, c2, c3 = gen_koef(3)
        lhs = c1 * uafvar ** 2 + c2 * uafvar + c3

    if rhs == None:
        c4, c5, c6 = gen_koef(3, first_nonzero=False)
        rhs = c4 * uafvar ** 2 + c5 * uafvar + c6

    e = sympy.Eq(lhs, rhs)
    puafvar = str(uafvar)
    sols = ', '.join([puafvar + " = " + sympy.latex(ex) for ex in sympy.solve(e, uafvar)])
    sols = "$$" + sols + "$$"
    if len(sols) == 0:
        return make_quadratic_eq()
    return gengiv(e), sols



def opg_redurcer(uafvar='x'):
    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))
    f1 = random.choice(_polynomier)
    f2 = random.choice(_polynomier)
    f3 = random.choice(_polynomier)

    eq = f1(uafvar)+f2(uafvar)+f3(uafvar)

    sol = sympy.latex(sympy.simplify(eq))
    eq = sympy.latex(eq)

    return gengiv(eq), gengiv(sol)
