import os
import sympy
import random
from lib.misc import var,gen_koef,gengiv,cifre_nozero,_funktioner


def opg_find_ubestemt_integral(uafvar="x",sg=2, niv = 'B', MC = False):
    F = sympy.Function("f")
    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))

    funktioner = _funktioner
    if niv == 'B': funktioner = _funktioner[:-3]


    f1 = random.choice(funktioner)
    f2 = random.choice(funktioner)
    f3 = random.choice(funktioner)

    if sg == 1:
        f = f1(uafvar)
    elif sg == 2:
        f = f1(uafvar)+f2(uafvar)
    elif sg == 3:
        f = f1(uafvar)+f2(uafvar)+f3(uafvar)


    sol = sympy.integrate(f, uafvar)
    f = sympy.latex(f)
    sol = sympy.latex(sol)

    df = sympy.latex(sympy.Integral(F(uafvar), uafvar))

    df = 'd'.join(df.split("\\partial"))
    sol = df + "=" + str(sol)
    fx = "f \\left(%s \\right)" % str(uafvar)
    return gengiv(f,fx), gengiv(sol)