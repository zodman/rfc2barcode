import easygui
import sys

def error(msg):
    easygui.msgbox(msg, title ="Error")
    sys.exit(0)

def get_index_rfc(list_colums):
    if "RFC" in list_colums or "R.F.C." in list_colums:
        for c,i in enumerate(list_colums):
            if "RFC" in i or "R.F.C." in i:
                return c+1
    else:
        return None


def get_rfcs(filepath):
    fileopen = open(filepath)

    lines = fileopen.readlines()
    list_colums = lines[0].split(",")
    datas = lines[1:]

    index_rfc = get_index_rfc(list_colums)
    if index_rfc is None:
        error( "No se encontro columna con RFC o R.F.C.")

    return  [row.split(",")[index_rfc] for row in datas]

def genpdf(filepath,pdf_file):
    from code import run
    run(get_rfcs(filepath), pdf_file)

def main():
    fileopen = easygui.fileopenbox(msg="Selecciona el archivo cvs", filetypes = ["*.csv"])
    pdf_file = easygui.filesavebox(msg="Guardar archivo pdf con codigo de barras")
    genpdf(fileopen,pdf_file)
if __name__ == "__main__":
    main()