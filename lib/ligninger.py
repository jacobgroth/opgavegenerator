import os
import sympy
import random
from lib.misc import var,gen_koef,gengiv,cifre_nozero,_polynomier,cifre_for_sg, andengrads_nulloes, _kvadratur

def opg_linear_ligning(x="", rhs = None, var_coeffs=True, sg=2 , niv ='B'):

    if not x:
        x = random.choice(var)
    elif isinstance(x, list):
        x = random.choice(x)
    fjern = [x.upper(), x.lower()]
    x = sympy.Symbol(x)
    c1, c2, c3, c4 = gen_koef(4, var_coeffs=var_coeffs, exclude = fjern,sg = sg )
    lhs = c1*x + c2
    rhs = c3*x + c4
    e = sympy.Eq(lhs, rhs)
    loes = [gengiv(ex, x) for ex in sympy.solve(e, x)]
    return "Løs for $%s$ : %s" % (x, gengiv(e)), loes


def opg_andengradsligning(uafvar="x", rhs = None, introed=True,sg=2, niv = 'B'):



    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))

    if introed:

        rannr  = random.choice(list(range(50)))

        if rannr > 25:
            r1 = random.choice(cifre_for_sg(sg))
            r2 = random.choice(cifre_for_sg(sg))
            lhs = (uafvar - r1) * (uafvar - r2)
            lhs = lhs.expand()

        elif rannr <= 25 and rannr > 10:
            r = random.choice(cifre_for_sg(sg))
            lhs = (uafvar - r) * (uafvar - r)
            lhs = lhs.expand()

        else:
            a, b, c = andengrads_nulloes(sg)
            lhs = a * uafvar ** 2 + b * uafvar + c
            return gengiv(sympy.Eq(lhs, 0)), 'Der er ingen løsninger'


    else:
        a, b, c = gen_koef(3,sg = sg)
        lhs = a*uafvar**2 + b*uafvar + c

    rhs = 0

    e = sympy.Eq(lhs, rhs)
    puafvar = str(uafvar)
    sols = ', '.join([puafvar + " = " + sympy.latex(ex) for ex in sympy.solve(e, uafvar)])
    sols = "$$" + sols + "$$"
    return gengiv(e), sols



def opg_redurcer(uafvar='x',sg=2, niv = 'B'):
    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))

    f1 = random.choice(_polynomier + _kvadratur)
    f2 = random.choice(_polynomier + _kvadratur)
    f3 = random.choice(_polynomier + _kvadratur)

    if sg == 1:
        f = f1(uafvar)
        eq = sympy.latex(f1(uafvar))
    elif sg == 2:
        f = f1(uafvar)+f2(uafvar)
        eq = sympy.latex(f1(uafvar)) + ' + ' + sympy.latex(f2(uafvar))
    elif sg == 3:
        f = f1(uafvar)+f2(uafvar)+f3(uafvar)
        eq = sympy.latex(f1(uafvar)) + ' + ' +sympy.latex(f2(uafvar)) +' + ' + sympy.latex(f3(uafvar))

    sol = sympy.latex(sympy.simplify(f))


    return gengiv(eq), gengiv(sol)
