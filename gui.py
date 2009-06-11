## Code by Andres Vargas para cotemar
## programadorti07@cotemar.com.mx
## 09/06/2009

import easygui
import csv

from reportlab.graphics.barcode.widgets import BarcodeCode128
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128
import os,sys



def run(rfc_list= [], pdf_file="barcode.pdf"):
    try:
        os.remove(pdf_file)
    except:
        pass

    c = Canvas(pdf_file)
    c.setFontSize(size="7")
    print  " %s pag para %s rfcs " % (int(round(len(rfc_list)/114.0,0)), len(rfc_list))
    for times in range(0,int(round(len(rfc_list)/114.0,0))):
        for i in range(0,6):
            for j in range(1,20):
                st = code128.Code128()
                if len(rfc_list) >0 :
                    rfc = rfc_list.pop()
                else:
                    c.save()
                    sys.exit()
                st.value = rfc
                pos_x = i*30*mm
                pos_y = j*15*mm
                #print pos_x/mm,pos_y/mm
                st.drawOn(c, x = pos_x, y = pos_y)
                c.drawString(pos_x+10*mm, pos_y+7*mm , rfc )
        c.showPage()
        c.setFontSize(size="7")

    try:
        f = open(pdf_file, "wb")
    except IOError:
        easygui.msgbox("El archivo pdf esta abierto, por lo que no se puede guardar", "Error")
        sys.exit(0)
    c.save()


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