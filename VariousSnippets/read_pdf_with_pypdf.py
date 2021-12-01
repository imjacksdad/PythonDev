# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('C:\Python39\DEVFiles\PythonDev\Support Files\ReadPDF\The_Iliad_Of_ Homer.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Getting number of pages in pdf file
pages = pdfReader.numPages
    
# printing number of pages in pdf file 
print(pdfReader.numPages)
            
# Loop for reading all the Pages
for p in range(pages):

        # Creating a page object
        pageObj = pdfReader.getPage(p)

        # Printing Page Number
        #print("Page No: ",i)

        # Extracting text from page
        # And splitting it into chunks of lines or individual words
        text = pageObj.extractText().split(" ")

        # Finally the lines are stored into list
        # For iterating over list a loop is used
        for i in range(len(text)):
                # Printing the line
                # Lines are seprated using "\n"
                #if text[i] == 'poet':
                 print(text[i],end="\n\n")
        # For Seprating the Pages
        #print()
# closing the pdf file object
pdfFileObj.close()
