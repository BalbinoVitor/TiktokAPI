import logging


# Define a custom log level for 'SUCCESS'
SUCCESS_LEVEL = 25  # Between WARNING (30) and INFO (20)
logging.addLevelName(SUCCESS_LEVEL, 'SUCCESS')


def success(self, message, *args, **kwargs):
    """Log 'SUCCESS' level messages."""
    if self.isEnabledFor(SUCCESS_LEVEL):
        self._log(SUCCESS_LEVEL, message, args, **kwargs)


logging.Logger.success = success


def setup_logging(log_file='app.log', level=logging.INFO):
    """Setup logging configuration."""
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level
    )
    logger = logging.getLogger(__name__)
    return logger


def get_logger(name):
    """Get a logger with the specified name."""
    logger = logging.getLogger(name)
    return logger


# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.success("This is a success message.")
    logger.error("This is an error message.")
    logger.warning("This is a warning message.")