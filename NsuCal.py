import urllib.request
import pdftables_api
# fetching the pdf from the nsu site  
pdf_path = "http://www.northsouth.edu/newassets/images/5-240.AcademicCalendarSpring%202021.pdf"
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
 

 #Coverter Api that Converts the given Pdf into Xlxs 

download_file(pdf_path, "Test")
c = pdftables_api.Client('9v1fb38u4aah')
c.xlsx('Test.pdf', 'output')               #replace c.xlsx with c.csv to convert to CSV



# Configuring google standard csv events. 





#Google Calender Api imprt converted csv file. 
