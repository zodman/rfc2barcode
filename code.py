## Code by Andres Vargas para cotemar
## programadorti07@cotemar.com.mx
## 09/06/2009

from reportlab.graphics.barcode.widgets import BarcodeCode128
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import mm

from reportlab.graphics.barcode import code128

import os,sys


def run(rfc_list= "", pdf_file="barcode.pdf"):
    try:
        os.remove(pdf_file)
    except:
        pass

    c = Canvas(pdf_file)

    c.setFontSize(size="7")

    for times in range(0,2):
        print len(rfc_list)
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
    c.save()


if __name__=='__main__':
    run()
