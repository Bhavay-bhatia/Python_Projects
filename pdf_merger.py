from PyPDF2 import PdfWriter
merger=PdfWriter()
pdfs=[]
n=int(input("enter the no. of pdfs you want to merge: "))
for i in range(n):
    name=input(f"enter the {i+1} pdf : ")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()