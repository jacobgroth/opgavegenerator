import os
import sympy
import random
import math
from lib.misc import var,gen_koef,gengiv,cifre_nozero,_funktioner, cifre_for_sg
from lib.MC import tilfoejMCspg


def opg_topunktformel(uafvar="x",sg=2, niv = 'B', MC = False):

    #_vaekstformer = [opg_topunktformel_linear,opg_topunktformel_eksponential,opg_topunktformel_potens]
    _vaekstformer = [opg_topunktformel_linear,opg_topunktformel_eksponential]

    funk = random.choice(_vaekstformer)

    return funk(sg = sg , MC = MC)


def opg_topunktformel_linear(uafvar="x",sg=2, MC = False):

    uafvar = sympy.Symbol(uafvar)

    x1, y1,x2,y2 = gen_koef(4)

    while x2 == x1:
        x1, y1, x2, y2 = gen_koef(4)

    a = round( (y2-y1)/(x2-x1),2 )
    b = round( ( y1 - a*x1 ),2 )

    rhs = a * uafvar + b
    lhs = sympy.Symbol('y')

    sol = sympy.Eq(lhs, rhs)
    sol = sympy.latex(sol)

    loes = gengiv(sol)

    spg = '{}, der går gennem punkterne $P({},{})$ og $Q({},{})$'.format("rette linje",x1, y1,x2,y2)

    if MC:
        altløsninger = ["${}$".format(sol)]

        for dummy in range(1, 4):
            aalt = a + round(random.uniform(-5, 5), 2)
            balt = b + round(random.uniform(-5, 5), 2)
            rhs = aalt * uafvar + balt
            lhs = sympy.Symbol('y')
            altsol = sympy.latex(sympy.Eq(lhs, rhs))
            altløsninger.append("${}$".format(altsol))

        spg += tilfoejMCspg(altløsninger)

    return spg, loes


def opg_topunktformel_eksponential(uafvar="x",sg=2, MC = False):


    uafvar = sympy.Symbol(uafvar)
    x1, y1, x2, y2 = gen_koef(4)

    while (y2/y1 < 0 or  (y2/y1) ** (1/(x2-x1)) < 0 ): x1,y1,x2,y2 = gen_koef(4)

    a = round( float( (y2/y1) ** (1/(x2-x1)) ) ,2)
    b = round( y1/(a**x1), 2)

    rhs = b * a ** uafvar
    lhs = sympy.Symbol('y')

    sol = sympy.Eq(lhs, rhs)

    sol = sympy.latex(sol)

    spg = ' {}, der går gennem punkterne $P({},{})$ og $Q({},{})$'.format("eksponentialfunktion",x1, y1, x2, y2)
    loes = gengiv(sol)

    if MC:
        altløsninger = ["${}$".format(sol)]
        for dummy in range(1, 4):
            aalt = a + round(random.uniform(-5, 5), 2)
            balt = b + round(random.uniform(-5, 5), 2)
            rhs =  balt*aalt ** uafvar
            lhs = sympy.Symbol('y')
            altsol = sympy.latex(sympy.Eq(lhs, rhs))
            altløsninger.append("${}$".format(altsol))
        spg += tilfoejMCspg(altløsninger)

    return spg, loes



def opg_topunktformel_potens(uafvar="x",sg=2, MC = False):
    uafvar = sympy.Symbol(uafvar)

    x1, y1, x2, y2 = gen_koef(4)

    while x2 == x1:
        x1, y1, x2, y2 = gen_koef(4)

    a =  sympy.log(y2/y1)/sympy.log(x2/x1)
    b = y1 / (x1 ** a)


    rhs = b *  uafvar ** a
    lhs = sympy.Symbol('y')

    sol = sympy.Eq(lhs, rhs)

    sol = sympy.latex(sol)

    spg = '{}, der går gennem punkterne $P({},{})$ og $Q({},{})$'.format("potens funktion",x1, y1, x2,y2)
    loes = gengiv(sol)

    if MC:
        altløsninger = ["${}$".format(sol)]
        for dummy in range(1, 4):
            aalt = a + round(random.uniform(-5, 5), 2)
            balt = b + round(random.uniform(-5, 5), 2)
            rhs =  balt*uafvar ** aalt
            lhs = sympy.Symbol('y')
            altsol = sympy.latex(sympy.Eq(lhs, rhs))
            altløsninger.append("${}$".format(altsol))
        spg += tilfoejMCspg(altløsninger)


    return spg, loes
