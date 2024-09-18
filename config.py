import os
import configPath
from logger import info_logger, error_logger

def pathExists(folder_path):
    try:
        # Create the directory if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        error_logger.error(f"{folder_path} folder error: {e}")

def config():

    output_dir = os.path.normpath(os.path.join((configPath.output_main),'0_files'))
    duplicates_dir = os.path.normpath(os.path.join((configPath.output_main),'1_duplicates'))
    corrupted_dir = os.path.normpath(os.path.join((configPath.output_main),'2_corrupted'))
    out_diffBinary_dir = os.path.normpath(os.path.join((duplicates_dir),'0_binary_diff'))

    #INITIAL FOLDER CHECK
    #-------------------------------------------------------------------------------------------------#
    try:
        if not os.path.exists(configPath.root_directory):
            print('Root dir not existing!')
            quit()
        else:
            root_directory = configPath.root_directory
    except Exception as e:
        error_logger.error(f"Root folder error: {e}")
    
    pathExists(configPath.output_main)

    pathExists(output_dir)

    pathExists(duplicates_dir)

    pathExists(corrupted_dir)

    pathExists(out_diffBinary_dir)

    return root_directory,output_dir,duplicates_dir,corrupted_dir,out_diffBinary_dir