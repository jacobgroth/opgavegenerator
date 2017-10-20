from lib.Afsnit import *
from lib.TexDele import texdoc_startogslut
from OpgaveArkInfo import opgave_ark_info as oai
from lib.fileIO import *

class opgave_ark:

    def __init__(self, opgave_ark_info = oai, lavloesning=True, dok_generator = texdoc_startogslut):

        self.oai = oai
        self.lavloesning = lavloesning
        self.texdokument = []
        self.opgavedokument = []
        self.loesningsdokument = []
        self.start , self.slut = dok_generator(self.oai['titel'],
                                               str( self.oai['elevnavn'] ),
                                               str(self.oai['klasse'] ) )


    def skriv_tekst_til_texdokument(self,tekst):

        self.texdokument.append(tekst)

    def skriv_tekst_til_opgavedokument(self,tekst):

        self.opgavedokument.append(tekst)


    def tilfoej_afsnit(self,opgavetype,antalopgaver):


        nytafsnit = afsnit(opgavetype,antalopgaver, self.lavloesning)

        nytafsnittekst = nytafsnit.lavafsnit()
        self.opgavedokument.append( ''.join(nytafsnittekst)  )



    def skriv_og_kompiler(self):

        self.skriv_tekst_til_texdokument(self.start)
        self.skriv_tekst_til_texdokument(''.join(self.opgavedokument))
        self.skriv_tekst_til_texdokument(self.slut)

        if self.oai['debug'] == False:
            outputfil = filIO(opgave_ark_info, self.texdokument)

            outputfil.skrivtilfil()
            outputfil.kompile()
            outputfil.rydop()

            if self.oai['lav loesning'] == True:
                outputfil.skrivtilfil(sol=True)
                outputfil.kompile(sol=True)
                outputfil.rydop()

        else:
            #print(''.join(self.texdokument))
            print('HEP')


        return True