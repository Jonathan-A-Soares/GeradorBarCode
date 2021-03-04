from barcode import Code128
from barcode.writer import ImageWriter

code = input("Code:")
filename = input ("Nome do arquivo")

with open(filename,'wb') as arquivo:
   Code128(code, writer=ImageWriter()).write(arquivo)
print("Done")

'''
EAN-8
EAN-13 
EAN-14
UPC-A
JAN
ISBN-10
ISBN-13
ISSN
Code 39
Code 128
PZN
'''