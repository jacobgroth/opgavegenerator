from lib.LavOpgave import *
from lib.TexDele import afsnit_tex
from lib.tekst import afsnittekstdict


class afsnit:

    def __init__(self,opgavetype,antalopgaver,lavloesning=True):
        self.lavloesning = lavloesning
        self.afnit = []
        self.opgavetype = opgavetype
        self.antalopgaver = antalopgaver

    def lavafsnit(self):

        self.afsnitstart, self.afsnitslut = afsnit_tex(self.opgavetype,
                                                       ''.join(afsnittekstdict[self.opgavetype]), cols=2)

        self.afnit.append(self.afsnitstart)

        for opgnr in range(self.antalopgaver):

            opg = opgave(self.opgavetype,self.lavloesning)
            opgavetekst = opg.lavopgave()
            self.afnit.append(''.join(opgavetekst))

        self.afnit.append(self.afsnitslut)

        return self.afnit

