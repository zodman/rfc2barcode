## Code by Andres Vargas para cotemar
## programadorti07@cotemar.com.mx
##

import easygui
import sys
import csv

def error(msg):
    easygui.msgbox(msg, title ="Error")
    sys.exit(0)

def get_index_rfc(list_colums):
    if "RFC" in list_colums or "R.F.C." in list_colums:
        for c,i in enumerate(list_colums):
            if "RFC" in i or "R.F.C." in i:
                return c
    else:
        return None

def get_rfcs2(filepath):
    reader = csv.reader(open(filepath))
    list_colums = reader[0]
    datas = reader[1:]


def get_rfcs(filepath):
    fileopen = open(filepath)
    reader = csv.reader(fileopen)
    lines = [ r for r in reader]
    list_colums = lines[0]
    datas = lines[1:]
    index_rfc = get_index_rfc(list_colums)

    if index_rfc is None:
        error( "No se encontro columna con RFC o R.F.C.")

    return  [row[index_rfc] for row in datas]

def genpdf(filepath,pdf_file):
    from code import run
    run(get_rfcs(filepath), pdf_file)

def main():
    fileopen = easygui.fileopenbox(msg="Selecciona el archivo cvs",
     filetypes = ["*.csv"])
    pdf_file = easygui.filesavebox(msg = "Guardar archivo pdf con codigo de barras",
        default ="barcode.pdf", filetypes=["*.pdf"] )
    genpdf(fileopen,pdf_file)
    #genpdf("archivo.csv","barcode.pdf")
if __name__ == "__main__":
    main()