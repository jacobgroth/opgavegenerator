from OpgaveArkInfo import *
from pandas import ExcelFile
import os,sys

class filIO:


    def __init__(self, opgave_ark_info):
        self.opgave_ark_info = opgave_ark_info

    def __init__(self,opgave_ark_info,listaftekst):
        self.string = ''.join(listaftekst)
        self.opgave_ark_info=opgave_ark_info

    def hentfilenavn(self):
        outputdir = self.opgave_ark_info['basedir'] + '/output/' + self.opgave_ark_info['ext']

        if os.path.exists(outputdir) == False:
            os.makedirs(outputdir)
        return [outputdir, outputdir + '/' + self.opgave_ark_info['elevnavn'].replace(' ','_') + '.tex']

    def skrivtilfil(self,sol=False):
        filnavn = self.hentfilenavn()[1]
        if sol == True:
            filnavn=filnavn.replace('.tex','_loesninger.tex')
            self.string=self.string.replace("\\noprintanswers", "\\printanswers")

        with open(filnavn, "w") as text_file:
            text_file.write(self.string)

    def kompile(self,sol=False):

        filnavn = self.hentfilenavn()[1]
        if sol == True:
            filnavn = filnavn.replace('.tex', '_loesninger.tex')

        filnavn = filnavn.replace('Google Drev','Google\ Drev')
        self.outputdir = self.hentfilenavn()[0].replace('Google Drev','Google\ Drev')
        os.system("pdflatex -output-directory {} {}".format(self.outputdir,filnavn))

    def rydop(self):
        os.system("rm {}/*aux".format(self.outputdir))
        os.system("rm {}/*log".format(self.outputdir))
        os.system("rm {}/*tex".format(self.outputdir))

    def hentCVSfilfraLectio(self):
        xl = ExcelFile(self.opgave_ark_info['basedir']+self.opgave_ark_info['excelfile'])
        df = xl.parse("cvstest.csv")

        kar_cols = [col for col in df.columns if 'standpunkt' in col]

        df['karaktersnit'] = df[kar_cols].mean(axis=1)

        svaerhedsgrad = []

        for kar in df['karaktersnit'].dropna():
            if -3 <= kar < 4:
                svaerhedsgrad.append(1)
            elif 4 <= kar < 9:
                svaerhedsgrad.append(2)
            elif 9 <= kar < 12:
                svaerhedsgrad.append(3)

        return zip(df["Elev\nNavn"].dropna().tolist(), svaerhedsgrad)



