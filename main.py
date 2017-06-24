from OpgaveArkInfo import opgave_ark_info as oai
from lib.fileIO import filIO
from lib.OpgaveArk import *
from lib.TexDele import texdoc_startogslut

cvsfil = filIO(oai,'')
elevnavne = cvsfil.hentCVSfilfraLectio()

for elev in elevnavne:

    oai['elevnavn'] = elev
    opgavedokument = opgave_ark(oai["lav loesning"], texdoc_startogslut)

    for opgtype,antalopg in zip(oai["opgavetyper"],oai["antal opgaver"]):
        opgavedokument.tilfoej_afsnit(opgtype,antalopg)

    opgavedokument.skriv_og_kompiler()

