from OpgaveArkInfo import opgave_ark_info as oai
from lib.fileIO import filIO
from lib.OpgaveArk import *
from lib.TexDele import texdoc_startogslut

cvsfil = filIO(oai,'')
elevinfo = cvsfil.hentCVSfilfraLectio()

for ei in elevinfo:

    oai['elevnavn'] = ei[0]
    oai['sværhedgrad'] = ei[1]

    opgavedokument = opgave_ark(oai["lav loesning"], texdoc_startogslut)

    for opgtype,antalopg in zip(oai["opgavetyper"],oai["antal opgaver"]):
        opgavedokument.tilfoej_afsnit(opgtype,antalopg)

    opgavedokument.skriv_og_kompiler()

