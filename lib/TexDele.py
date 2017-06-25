def texdoc_startogslut(titel,elevnavn,klasse):
    start="""
     \\documentclass{exam}
    \\usepackage{amsfonts}
    \\usepackage{amsmath,multicol,eso-pic}
    \\usepackage[utf8]{inputenc}
    \\usepackage[danish]{babel}
    \\usepackage[T1]{fontenc}
    \\noprintanswers
    \\addpoints 
    \\qformat{\\textbf{Spørgsmål \\quad \\\\ \\thequestion}\\quad(\\thepoints)\\hfill}
    \\usepackage{color}
    \\definecolor{SolutionColor}{rgb}{0.8,0.9,1} 
    \\shadedsolutions 
    \\renewcommand{\\solutiontitle}{\\noindent\\textbf{Løsning:}\\par\\noindent}

    \\begin{document}
    \\title{%s \\\\ \\large Hold : %s }
    \\maketitle
    \\AddToShipoutPicture{
        \\AtTextUpperLeft{
        \\makebox(400,45)[lt]{ 
          \\footnotesize
          \\begin{tabular}{r@{\\,}l}
            Navn:  & %s \\\\[.5cm]
            Dato:  & \\rule{0.5\\linewidth}{\\linethickness} \\\\
          \end{tabular}
    }}}
    \\begin{minipage}{.8\\textwidth}
    Denne prøve indeholder \\numquestions\\ spørgsmål. Det totale antal mulige point er \\numpoints.
    \\end{minipage}
    """ % (titel,klasse,elevnavn)

    slut = """
    \end{document}
    """
    return start, slut

def afsnit_tex(titel, instr="", cols = 1):
    if cols >= 2:
        afsnit_start="""
        \\section{%s}
        %s
        \\begin{multicols}{1}
        \\begin{questions}
        """ % (titel, instr)

        afsnit_slut="""
        \\end{questions}
        \\end{multicols}
        """
    else:
        afsnit_start = """
        \\section{%s}
        %s
        \\begin{questions}
        """ % (titel, instr)
        afsnit_slut = """
        \\end{questions}
        """
    return afsnit_start, afsnit_slut

def opgave_tex(instruktioner, problem, loesning, point=1):
    code = """
    \\question[%s]
        %s
        %s
    \\begin{solution} 
        %s
    \\end{solution}
    """ % (str(point), instruktioner, problem, loesning)
    return code
