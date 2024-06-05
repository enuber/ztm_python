# pip3 install PyPDF2==1.26
# use above to follow videos as program has changed since

import PyPDF2
import sys

# note that 'rb' is read binary. So that the pdf can be read
with open('./pdfs/dummy.pdf', 'rb') as file:
    # print(file)  # <_io.TextIOWrapper name='./pdfs/dummy.pdf' mode='r' encoding='UTF-8'>
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # 1 = gives number of pages of PDF
    page = reader.getPage(0)
    print(page)
    # will rotate PDF backwards 90 degrees, this is an object though in memory, doesn't change the PDF
    page.rotateCounterClockwise(90)
    # by using pdf writer we can write to a pdf this process will add the rotated page to a file and create the file.
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    # writing to a file in binary just like it was read for PDF files
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

# PDF MERGER

# remember that 1: will start at 1 and grab everything after
inputs = sys.argv[1:]

# combines multiple pdfs into one file. have to call with python3 3_pdf_watermarking.py ./pdfs/dummy.pdf ./pdfs/twopage.pdf


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)


# WATERMARKING

template = PyPDF2.PdfFileReader(open('./pdfs/dummy.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./pdfs/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
