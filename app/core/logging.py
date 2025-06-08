import colorlog
from app.config.settings import settings


def setup_logging():
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        )
    )

    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(settings.LOG_LEVEL)

    return logger


logger = setup_logging()
