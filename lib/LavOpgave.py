from lib.TexDele import opgave_tex
from lib.ligninger import opg_linear_ligning,opg_andengradsligning,opg_redurcer
from lib.differentialregning import opg_find_afledet
from lib.integralregning import opg_find_ubestemt_integral
from lib.tekst import opgavetekstdict
from OpgaveArkInfo import opgave_ark_info as oai

_opgave_dict = {

    "Førstegradsligninger": opg_linear_ligning,
    "Andengradsligninger" : opg_andengradsligning,
    "Reducer": opg_redurcer,
    "Find afledet funktion" : opg_find_afledet,
    "Find ubestemt integral": opg_find_ubestemt_integral

}


class opgave:

    def __init__(self,opgavetype,lavloesning=True):
        self.lavloesning = lavloesning
        self.opgavetype = opgavetype
        self.opgavetekstdict = opgavetekstdict
        self.opgavetekst = []
        self.vspace = 1


    def lavopgave(self):


        instruktion = self.opgavetekstdict[self.opgavetype][0]
        args = self.opgavetekstdict[self.opgavetype][1]
        kwargs = self.opgavetekstdict[self.opgavetype][2]
        kwargs['sg'] = oai['sværhedgrad']

        if hasattr(self.opgavetype, '__call__'):
            opg_generator = self.opgavetype
        else:
            opg_generator = _opgave_dict[self.opgavetype]

        opg,loesning = opg_generator(*args, **kwargs)
        loesning = ''.join(loesning)
        opgavetekst = opgave_tex(instruktion,opg,loesning,4)
        self.opgavetekst.append(opgavetekst)
        self.opgavetekst.append("\\vspace{%spt}" % self.vspace)

        return self.opgavetekst



