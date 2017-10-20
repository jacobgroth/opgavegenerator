from OpgaveArkInfo import opgave_ark_info as oai
from lib.fileIO import filIO
from lib.OpgaveArk import *
from lib.TexDele import texdoc_startogslut

cvsfil = filIO(oai,'')
elevinfo = cvsfil.hentCVSfilfraLectio()

for ei in elevinfo:

    oai['elevnavn'] = ei[0]
    oai['sværhedsgrad'] = ei[1]

    opgavedokument = opgave_ark(oai["lav loesning"], texdoc_startogslut)



    for opgtype,antalopg in zip(oai["opgavetyper"],oai["antal opgaver"]):

        oai["MC"] = False
        if type( antalopg ) != int:
            antalopg = int(antalopg[:-2])
            oai["MC"] = True

        opgavedokument.tilfoej_afsnit(opgtype,antalopg)

    opgavedokument.skriv_og_kompiler()

