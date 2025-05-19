from utils.logger import get_logger

logger = get_logger(__name__)

def some_function():
    logger.info("Starting function...")
    try:
        # logic
        pass
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
