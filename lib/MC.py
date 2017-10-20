import random

def tilfoejMCspg(altløsninger):

    kode = ""

    random.shuffle(altløsninger)

    tilleagstr = "\\vspace{0.4cm} \n \\begin{checkboxes}"

    for al in altløsninger:
        tilleagstr += "\choice " + al + "\n"

    tilleagstr += "\\end{checkboxes}"

    return tilleagstr
