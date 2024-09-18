from logger import info_logger, error_logger
import os
from relocate import relocate_file
from crawler import crawler


def CompareConditions(file_path, file_type):
    if file_type in ['png', 'jpg', 'jpeg']:

        #TODO Implement the specific conditions.
        
        conditions = (os.path.basename(file_path),
                        os.path.getsize(file_path))
        return conditions
    else:
        conditions = (os.path.basename(file_path),
                        os.path.getsize(file_path))
        return conditions

def binaryComparison(file_path):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    return file_bytes

def duplicateCompare(etalon_file, search_dir, file_type):

    etalon_conditions = CompareConditions(etalon_file, file_type)
    etalon_byte = binaryComparison(etalon_file)
    # List to store duplicate files
    duplicates = []
    binary_diff = []

    for file_path in crawler(search_dir,file_type):

        file_conditions = CompareConditions(file_path, file_type)
        
        if etalon_conditions == file_conditions:

            file_byte = binaryComparison(file_path)
            
            if etalon_byte == file_byte:
                duplicates.append(file_path)
            else:
                error_logger.error(f"Binary comparison failed! {file_path}")
                binary_diff.append(file_path)

    if duplicates:
        duplicates.pop(0)
    
    return duplicates, binary_diff


def duplicateFinder(search_dir, file_type, out_duplicates_dir, out_diffBinary_dir):
    #ha a file size nagyobb mint 50mb, ne csináljon binary compare-t! moviek-ra most még csak nagyon óvatosan!
    for crawler_file in crawler(search_dir,file_type):
        duplicate, binary_diff = duplicateCompare(crawler_file, search_dir, file_type)
        #location_logger.info(duplicate)
        for element_path in duplicate:
            try:
                relocate_file(element_path,out_duplicates_dir)
                info_logger.info(f"Duplicate file sent to trash_duplicate folder : {element_path}")
            except Exception as e:
                error_logger.error(f"Failed to move DUPLICATE file to trash_duplicate: {element_path} and {e}")
        for element_path in binary_diff:
            try:
                relocate_file(element_path,out_diffBinary_dir)
                info_logger.info(f"BINARY DIFF file sent to corrupted folder : {element_path}")
            except Exception as e:
                error_logger.error(f"Failed to move BINARY DIFF file to corrupted: {element_path} and {e}")