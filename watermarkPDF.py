from PyPDF2 import PdfFileWriter, PdfFileReader

def create_watermark(input_PDF, output, watermark):
    #These first two lines get the watermark page of the watermark PDF which should be on the first page
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0) 

    #These lines create objects to use from the PyPDF library
    pdf_reader = PdfFileReader(input_PDF)
    pdf_writer = PdfFileWriter()

    #Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    #This writes newly watermarked PDF to disk
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    create_watermark(
        input_PDF = '/Users/christopher/Downloads/pdf/reportlab-sample.pdf', #Give the filepath to the PDF that you are going to be adding a watermark to
        output = '/Users/christopher/Downloads/pdf/watermarked_notebook77.pdf', #Give the filepath to where you want the newly created watermarked PDF to be saved
        watermark = '/Users/christopher/Downloads/pdf/watermark.pdf') #Give the filepath to the PDF that contains the watermark image        