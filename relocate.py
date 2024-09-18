from logger import info_logger, error_logger
import os
import shutil

# Function to find the next available subfolder or create it
def get_available_subfolder(output_dir, base_name, max_attempts = 500):
    subfolder_index = 1
    while subfolder_index < max_attempts:
        subfolder_path = os.path.normpath(os.path.join(output_dir, str(subfolder_index)))
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        if not os.path.exists(os.path.normpath(os.path.join(subfolder_path, base_name))):
            return subfolder_path
        subfolder_index += 1
    
    error_logger.error(f"Could not find available subfolder after {max_attempts} attempts.")
    return None

# Function to relocate a file and log the movement
def relocate_file(old_path, new_dir):
    if os.path.exists(old_path):
        base_name = os.path.basename(old_path)
        target_path = os.path.normpath(os.path.join(new_dir, base_name))

        try:
            # Check if the file already exists in the output folder
            if not os.path.exists(target_path):
                try:
                    shutil.move(old_path, target_path)
                except (FileNotFoundError, PermissionError, OSError, shutil.Error) as e:
                    error_logger.error(f"Error moving file '{old_path}' : {e}")

                if os.path.exists(target_path):
                    info_logger.info(f"Moved '{old_path}' to '{target_path}'")
                else:
                    error_logger.error((f"NOT MOVED '{old_path}' to '{target_path}'"))
            else:
                # Find the next available subfolder
                subfolder_path = get_available_subfolder(new_dir, base_name)
                final_path = os.path.normpath(os.path.join(subfolder_path, base_name))
                try:
                    shutil.move(old_path, final_path)
                except (FileNotFoundError, PermissionError, OSError, shutil.Error) as e:
                    error_logger.error(f"Error moving file '{old_path}' : {e}")
                if os.path.exists(final_path):
                    info_logger.info(f"Moved '{old_path}' to '{final_path}'")
                else:
                    error_logger.error((f"NOT MOVED '{old_path}' to '{final_path}'"))

        except Exception as e:
            # Log any errors
            error_logger.error(f"Error moving '{old_path}' to '{target_path}' or subfolder: {e}")
    else:
        error_logger.error(f"Invalid log entry: {old_path}")