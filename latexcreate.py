# want to:
'''
run program to create a new latex file with
title
homework number
number of questions + formatting for them
make sure shortcuts and environments also at top
'''

import subprocess
import os

DEFAULT_DIR = "/Users/aanya/Life/School/2018-2019/WINTER\\ 2019"
LOOKUP_DICT = {"diffeq": ("MATH 273", "/MATH\\ 273"),\
               "compsci": ("CMSC 122", "/CMSC\\ 122"),\
               "stat": ("STAT 244", "/STAT\\ 244")}

def create_latex_text(class_name, hw_num, num_questions, due_date):
    header = "\\documentclass[11pt, a4paper]{article} \n" +\
    "\usepackage[utf8]{inputenc} \n" +\
    "\usepackage{graphicx} \n" +\
    "\usepackage{amsmath} \n" +\
    "\usepackage{amssymb} \n" +\
    "\usepackage{tabto} \n" +\
    "\usepackage[margin=1in]{geometry} \n" +\
    "\usepackage{array} \n" +\
    "\n" +\
    "\n" +\
    "\\newcommand{\\R}{\\mathbb{R}}\n" +\
    "\\newcommand{\\N}{\\mathbb{N}}\n" +\
    "\\newcommand{\\Q}{\\mathbb{Q}}\n" +\
    "\\newcommand{\\p}{\\rho}\n" +\
    "\\newcommand{\\s}{\\sigma}\n" +\
    "\\newcommand{\\e}{\\epsilon}\n" +\
    "\\newcommand{\\del}{\\delta}\n" +\
    "\\newcommand{\\lam}{\\lambda}\n" +\
    "\\newcommand{\\qbreak}{\\bigbreak \\bigbreak}\n" +\
    "\\newcommand{\\dspace}{\\text{ }}\n" +\
    "\\newcommand{\\pr}{\\text{P}}\n" +\
    "\\newcommand{\\Om}{\\Omega}\n" +\
    "\\def\\changemargin#1#2{\\list{}{\\rightmargin#2\\leftmargin#1}\\item[]} \n" +\
    "\\let\\endchangemargin=\\endlist \n" +\
    "\\DeclareUnicodeCharacter{2212}{FIX ME!!!!} \n" +\
    "\\setlength\\parindent{0pt}"

    title = "\\title{\\vspace{-0.25in}" + class_name + "HW " + str(hw_num) +"} \n" +\
            "\\author{Aanya Jhaveri} \n" +\
            "\\date{Due " + due_date + "}"

    document = "\\begin{document} \n" +\
               "\\maketitle \n"

    for i in range(num_questions):
        document += "\\textbf{Question " + str(i + 1) + "} \n" +\
                    "\\begin{changemargin}{0.25in}{0.25in} \n" +\
                    "Answer \n" +\
                    "\\end{changemargin} \n" +\
                    "\\bigbreak \n"
    document += "\\end{document}"

    return header + title + document

def create_file(class_name, hw_num, num_questions, due_date):
    assert class_name in LOOKUP_DICT.keys()

    hw_name = "HW" + str(hw_num)

    folder_path = DEFAULT_DIR + LOOKUP_DICT[class_name][1] + "/" + hw_name
    hw_text = create_latex_text(LOOKUP_DICT[class_name][0], hw_num, num_questions,\
                                due_date)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        subprocess.call(["cd", folder_path])

    f = open(hw_name + ".tex", "w+")
    f.write(hw_text)
    f.close()

create_file("diffeq", 1, 2, "December 16, 2018")
