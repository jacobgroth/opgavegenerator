from OpgaveArkInfo import opgave_ark_info as oai
from lib.OpgaveArk import *
from lib.TexDele import texdoc_startogslut


opgavedokument = opgave_ark(oai["lav loesning"], texdoc_startogslut)

for opgtype,antalopg in zip(oai["opgavetyper"],oai["antal opgaver"]):
    opgavedokument.tilfoej_afsnit(opgtype,antalopg)

opgavedokument.skriv_og_kompiler()

