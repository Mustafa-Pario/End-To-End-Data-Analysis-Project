import zipfile

def extract_file():
    #extract file from zip file
    zip_ref = zipfile.ZipFile('orders.csv.zip') 
    zip_ref.extractall() # extract file to dir
    zip_ref.close() # close file