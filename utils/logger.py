import logging
import os

def setup_logger():
    # Buat folder logs kalau belum ada
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Buat formatter (format teks log)
    formatter = logging.Formatter(
        fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Setup root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Handler untuk console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler untuk file (semua log INFO+)
    file_handler = logging.FileHandler('logs/blakeshley_bot.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler khusus ERROR (optional)
    error_handler = logging.FileHandler('logs/blakeshley_bot_errors.log', encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)