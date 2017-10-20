import os
import sympy
import random
from lib.misc import var,gen_koef,gengiv,cifre_nozero,_funktioner
from lib.MC import tilfoejMCspg

def opg_find_afledet(uafvar="x", sg=2, niv = 'B', MC = False):

    rhs = 4
    F = sympy.Function("f")
    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))

    funktioner = _funktioner
    if niv == 'B': funktioner = _funktioner[:-3]

    print(funktioner)
    f1 = random.choice(funktioner)
    f2 = random.choice(funktioner)
    f3 = random.choice(funktioner)

    if sg == 1:
        f = f1(uafvar)
    elif sg == 2:
        f = f1(uafvar)+f2(uafvar)
    elif sg == 3:
        f = f1(uafvar)+f2(uafvar)+f3(uafvar)

    sol = sympy.diff(f, uafvar)
    f = sympy.latex(f)
    sol = sympy.latex(sol)

    df = sympy.latex(sympy.Derivative(F(uafvar), uafvar))

    df = 'd'.join(df.split("\\partial"))
    sol = df + "=" + str(sol)
    fx = "f \\left(%s \\right)" % str(uafvar)
    return gengiv(f,fx), gengiv(sol)



def opg_tangent(uafvar="x", sg=2, niv = 'B', MC = False):


    rhs = 4

    F = sympy.Function("f")

    if isinstance(uafvar, str):
        uafvar = sympy.Symbol(uafvar)
    elif isinstance(uafvar, list):
        uafvar = sympy.Symbol(random.choice(uafvar))

    funktioner = _funktioner[:-3]

    f1 = random.choice(funktioner)
    f2 = random.choice(funktioner)
    f3 = random.choice(funktioner)

    if sg == 1:
        f = f1(uafvar)
    elif sg == 2 or sg == 3:
        f = f1(uafvar)+f2(uafvar)

    x0 = abs(gen_koef(1, sg )[0])
    y0 = f.subs(uafvar,x0).evalf()

    a = round(sympy.diff(f, uafvar).subs(uafvar,x0).evalf() ,2)
    b = round(y0 - a*x0, 2)

    sol = sympy.latex( a*uafvar +b)

    f = sympy.latex(f)
    fx = "f \\left(%s \\right)" % str(uafvar)

    spg = gengiv(f,fx) + "Bestem in ligning for tangenten til grafen for $f$ i punktet $P({0},f({0}))$".format(x0)
    loes = gengiv(sol)

    if MC:

        altløsninger = ["${}$".format(sol)]

        for dummy in range(1, 4):
            aalt = a + round(random.uniform(-10, 10), 2)
            balt = b + round(random.uniform(-10, 10), 2)
            altsol = sympy.latex(aalt * uafvar + balt)
            altløsninger.append("${}$".format(altsol))

        spg += tilfoejMCspg(altløsninger)


    return spg , loes
