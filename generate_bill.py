from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from datetime import date



def report(UID,DISH_NAME,QUANTITY,TOTAL):
        now = datetime.now()
        timee = now.strftime("%H-%M-%S")
        datee = date.today()
        time_detail = "Bill generated on:  " + str(datee) + " at " + str(timee)
        
        t = "UID : " + str(UID)
        p = "DISH NAME : " + str(DISH_NAME)
        d = "QUANTITY : " + str(QUANTITY)
        a_a = "PRICE : " + str(TOTAL)
        
        
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(50, 530, time_detail)
        can.drawString(50, 510, t)
        can.drawString(50, 490, p)
        can.drawString(50, 470, d)
        can.drawString(50, 450, a_a)
                
        t = 0
        can.showPage()
        can.save()
          
        # packet.seek(0)
 
        nw_pdf = PdfFileReader(packet)

        #move to the beginning of the StringIO buffer
        packet.seek(0)

        # create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("bill_generate.pdf", "rb"))
        output = PdfFileWriter()
        

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        # report_path = "report/" + str(datee) + "-report.pdf"
        report_path = str(datee) + "-report.pdf"
        outputStream = open(report_path, "wb")
        output.write(outputStream)
        outputStream.close()

# report(2.81863556817906E+37,'Chicken Biryani',2,144)