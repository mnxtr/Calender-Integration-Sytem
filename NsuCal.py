import urllib.request
import urllib.error
import pdftables_api
import os
from typing import Optional

#fetching the pdf from the nsu site  
pdf_path = "https://www.northsouth.edu/newassets/images/Registrs%20Office/academiccalendar-spring-2025-30-dec-2025.pdf"

def download_file(download_url: str, filename: str, chunk_size: int = 8192) -> bool:
    """
    Downloads a file from the given URL and saves it as a PDF with efficient memory usage.

    Args:
        download_url (str): The URL from which to retrieve the file.
        filename (str): The base name used for the saved PDF file (without extension).
        chunk_size (int): Size of chunks to read at a time (default: 8192 bytes).

    Returns:
        bool: True if download was successful, False otherwise.
    
    Raises:
        urllib.error.URLError: If there's a network-related error.
        IOError: If there's a file writing error.
    """
    try:
        # Use context manager for response to ensure it's always closed
        with urllib.request.urlopen(download_url, timeout=30) as response:
            # Check if the request was successful
            if response.status != 200:
                print(f"Error: Server returned status code {response.status}")
                return False
            
            # Use context manager to ensure file is properly closed
            output_path = filename + ".pdf"
            with open(output_path, 'wb') as file:
                # Download in chunks for better memory efficiency
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    file.write(chunk)
            
            print(f"Successfully downloaded {output_path}")
            return True
        
    except urllib.error.URLError as e:
        print(f"Network error downloading file: {e}")
        return False
    except IOError as e:
        print(f"File error while saving: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during download: {e}")
        return False
 

#Converter Api that Converts the given Pdf into Xlsx

def convert_pdf_to_xlsx(pdf_filename: str, output_filename: str, api_key: Optional[str] = None) -> bool:
    """
    Converts a PDF file to XLSX format using pdftables API.
    
    Args:
        pdf_filename (str): Path to the input PDF file.
        output_filename (str): Path for the output XLSX file (without extension).
        api_key (str, optional): API key for pdftables. If None, reads from environment variable.
    
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Get API key from environment variable for better security
        if api_key is None:
            api_key = os.environ.get('PDFTABLES_API_KEY', '9v1fb38u4aah')
        
        if not api_key:
            print("Error: No API key provided")
            return False
        
        # Check if input file exists
        if not os.path.exists(pdf_filename):
            print(f"Error: Input file {pdf_filename} does not exist")
            return False
        
        c = pdftables_api.Client(api_key)
        c.xlsx(pdf_filename, output_filename)
        print(f"Successfully converted {pdf_filename} to {output_filename}")
        return True
        
    except Exception as e:
        print(f"Error converting PDF to XLSX: {e}")
        return False


# Main execution
if __name__ == "__main__":
    # Download the PDF file
    if download_file(pdf_path, "Test"):
        # Convert to XLSX if download was successful
        convert_pdf_to_xlsx('Test.pdf', 'output')              


#replace c.xlsx with c.csv to convert to CSV



# Configuring google standard csv events. 





#Google Calender Api imprt converted csv file. 
