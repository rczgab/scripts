from logger import info_logger, error_logger
import os

def crawler(root_directory,file_type):
    try:
          for subdir, _, files in os.walk(root_directory):
            for file in files:
                if file.lower().endswith(file_type):
                    file_path = os.path.normpath(os.path.join(subdir, file))
                    yield file_path
    except Exception as e:
        info_logger.error(f"Location finder: {e}")
