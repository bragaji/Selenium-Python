import csv
import re
import PyPDF2

pdfReader = PyPDF2.PdfFileReader('INPUT/Sample.pdf')

pageNum = pdfReader.getNumPages()

String= "New York"

for i in range(0,pageNum):
    PageObj = pdfReader.getPage(i)
    #print("this is page " + str(i))
    Text = PageObj.extractText()
    #print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)

#print(pageObj.extractText())

#a=pageObj.ext

