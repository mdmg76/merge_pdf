import os
from PyPDF2 import PdfFileMerger

source_dir = './PDF Files/'
merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        # print(item)
        merger.append(source_dir + item)

merger.write('Complete.pdf')       
merger.close()