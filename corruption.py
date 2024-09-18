from logger import info_logger, error_logger
import PyPDF2
from crawler import crawler
from relocate import relocate_file


#2_1 CORRUPTION CONDITIONS
    #2_1_0 Encryption check
def check_pdf_encryption(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                error_logger.error(f"PDF is encrypted. {file_path}")
                return True
            else:
                print(f"PDF is not encrypted. {file_path}")
                return False
    except Exception as e:
        error_logger.error(f"Error checking encryption: {file_path} {e}")
        return False
    
    #2_1_1 Structural check
def check_pdf_structure(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"{file_path} PDF loaded successfully, number of pages: {num_pages}")
            return True
    except PyPDF2.errors.PdfReadError as e:
        error_logger.error(f"Error reading PDF structure: {file_path} {e}")
        return False
    except Exception as e:
        error_logger.error(f"Other error: {file_path} {e}")
        return False

#2_2 CORRUPTION SUMMARIZER
#If return is true, the pdf file is corrupted.

def is_pdf_valid(file_path):

    if (check_pdf_encryption(file_path)):
        return True
    #Shall True if correct
    else:
        check_1 = check_pdf_structure(file_path)
        
        if check_1:
            return True
        else:
            return False



#!Modify for other filetypes!
def validityCondition(file_path, file_type):

    if file_type == 'pdf':
        validity = is_pdf_valid(file_path)

    else:
        error_logger.error(f"Wrong file type! {file_path}")
        validity = True

    #!Conditions Not valid = false, Valid = true
    return validity

#filetype: pdf
def corruptedFinder(search_dir,file_type,corrupted_dir):
    for file_path in crawler(search_dir,file_type):
        if not (validityCondition(file_path, file_type)):
            try:
                relocate_file(file_path,corrupted_dir)
                info_logger.info(f"Corrupted file sent to trash_corrupted folder: {file_path}")
            except Exception as e:
                error_logger.error(f"Failed to move CORRUPTED file to trash_corrupted folder: {file_path} and {e}")