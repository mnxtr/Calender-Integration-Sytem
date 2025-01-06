import urllib.request
import pdftables_api
#fetching the pdf from the nsu site  
pdf_path = "https://www.northsouth.edu/newassets/images/Registrs%20Office/academiccalendar-spring-2025-30-dec-2025.pdf"
def download_file(download_url, filename):
    """
    Downloads a file from the given URL and saves it as a PDF.

    Args:
        download_url (str): The URL from which to retrieve the file.
        filename (str): The base name used for the saved PDF file (without extension).

    Returns:
        None
    """
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
 

#Coverter Api that Converts the given Pdf into Xlxs 

download_file(pdf_path, "Test")
c = pdftables_api.Client('9v1fb38u4aah')
c.xlsx('Test.pdf', 'output')              


#replace c.xlsx with c.csv to convert to CSV



# Configuring google standard csv events. 





#Google Calender Api imprt converted csv file. 
