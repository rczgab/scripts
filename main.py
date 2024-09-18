import configPath
from crawler import crawler
from relocate import relocate_file
from duplicate import duplicateFinder
import config
from corruption import corruptedFinder
from logger import info_logger, error_logger


if __name__ == "__main__":

    root_directory,output_dir,duplicates_dir,corrupted_dir,diffBinary_dir = config.config()
    #file_type = configPath.file_type
    file_type = 'xlsx'

    info_logger.info(f"\n\nSystem started. - Filetype: {file_type}")

    for crawler_file in crawler(root_directory,file_type):
        #location_logger.info(f"{crawler_file}")
        relocate_file(crawler_file, output_dir)

    info_logger.info("\n\nRelocation finished.\n")

    #Comment out if corruption check not needed
    corruptedFinder(output_dir,file_type,corrupted_dir)
    info_logger.info("\n\nCorruption check and trash finished.\n\n")

    duplicateFinder(output_dir,file_type,duplicates_dir,diffBinary_dir)
    info_logger.info("\n\nDuplication check and trash finished.\n\n")


    error_logger.info(f"\n\nFILE END - Filetype: {file_type}")
    info_logger.info(f"\n\nFILE END - Filetype: {file_type}")