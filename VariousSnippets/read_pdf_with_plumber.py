import pdfplumber

with pdfplumber.open(r'C:\Python39\DEVFiles\PythonDev\Support Files\StoneX\StoneX Daily 10-01.pdf') as pdf:
    page1 = pdf.pages[0]
    page2 = pdf.pages[1]
    page3 = pdf.pages[2]
    page4 = pdf.pages[3]
    page5 = pdf.pages[4]
    page6 = pdf.pages[5]
    page7 = pdf.pages[6]
    page8 = pdf.pages[7]
    
    print(page1.extract_text())
    print(page2.extract_text())
    print(page3.extract_text())
    print(page4.extract_text())
    print(page5.extract_text())
    print(page6.extract_text())
    print(page7.extract_text())
    print(page8.extract_text())
