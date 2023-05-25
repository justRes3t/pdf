# script for applying a watermark to a pdf file and creating a new pdf file with the watermark applied
import PyPDF4 
from PyPDF4 import PdfFileReader, PdfFileWriter

def put_watermark(input_pdf, output_pdf, watermark):
    # Reads watermark file through PdfFileReader and assigns it to watermark_instance variable
    watermark_instance = PdfFileReader(watermark)
      
    # Fetches the first page of the watermark pdf file, watermark needs to be on the first page
    watermark_page = watermark_instance.getPage(0)
      
    # Reads the input PDF file
    pdf_reader = PdfFileReader(input_pdf)
      
    # Creates a PdfFileWriter and assigns it to pdf_writer variable
    pdf_writer = PdfFileWriter()
  
    # Loops through the input PDF pages and applies watermark
    for page in range(pdf_reader.getNumPages()):

        # Assigns the current page of the PDF being read to the variable page  
        page = pdf_reader.getPage(page)
          
        # Places the watermark by merging watermark page with current page of input PDF
        page.mergePage(watermark_page)
          
        # Adds the new page to the PdfFileWriter object we assigned previously
        pdf_writer.addPage(page)
  
    with open(output_pdf, 'wb') as out:    
        # Writes the file to disk that we made with the loop and is stored in the PdfFileWriter object 
        pdf_writer.write(out)

# Runs the script   
if __name__ == "__main__":
    put_watermark(
        input_pdf='FilepathToInputPdf',  # filepath to the input pdf
        output_pdf='FilepathWhereNewPdfIsSaved',  # filepath where we want the newly created pdf to be saved
        watermark='FilepathToWatermarkPdf'  # filepath to the watermark pdf
    )
