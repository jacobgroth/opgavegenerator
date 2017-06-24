from OpgaveArkInfo import *
from pandas import ExcelFile
import os,sys

class filIO:

    # laver og skrive dvs cards til serpent filen

    def __init__(self, opgave_ark_info):
        self.opgave_ark_info = opgave_ark_info

    def __init__(self,opgave_ark_info,listaftekst):
        self.string = ''.join(listaftekst)
        self.opgave_ark_info=opgave_ark_info

    def hentfilenavn(self):
        outputdir = self.opgave_ark_info['basedir'] + '/output/' + self.opgave_ark_info['ext']

        if os.path.exists(outputdir) == False:
            os.makedirs(outputdir)
        return outputdir, outputdir + '/' + self.opgave_ark_info['elevnavn'].replace(' ','_') + '.tex'

    def skrivtilfil(self):
        with open(self.hentfilenavn()[1], "w") as text_file:
            text_file.write(self.string)

    def kompile(self):
        filnavn = self.hentfilenavn()[1].replace('Google Drev','Google\ Drev')
        self.outputdir = self.hentfilenavn()[0].replace('Google Drev','Google\ Drev')
        os.system("pdflatex -output-directory {} {}".format(self.outputdir,filnavn))

    def rydop(self):
        os.system("rm {}/*aux".format(self.outputdir))
        os.system("rm {}/*log".format(self.outputdir))

    def hentCVSfilfraLectio(self):
        xl = ExcelFile(self.opgave_ark_info['basedir']+self.opgave_ark_info['excelfile'])
        df = xl.parse("cvstest.csv")
        return df["Elev\nNavn"].dropna().tolist()



