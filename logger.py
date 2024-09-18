import logging
import configPath
import os

def global_logging(output_main):
    #log_name = f"{logType}.log"
    info_log_path = os.path.normpath(os.path.join(output_main,'info.log'))
    error_log_path = os.path.normpath(os.path.join(output_main,'error.log'))
    #if not os.path.exists(log_path):
    #    os.makedirs(log_path)
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    info_logger = logging.getLogger('info_logger')
    info_handler = logging.FileHandler(info_log_path)
    info_logger.addHandler(info_handler)

    error_logger = logging.getLogger('error_logger')
    error_handler = logging.FileHandler(error_log_path)
    error_logger.addHandler(error_handler)

    return info_logger, error_logger

info_logger, error_logger = global_logging(configPath.output_main)