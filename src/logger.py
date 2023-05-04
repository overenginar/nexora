import logging
from logging.config import dictConfig


def get_logger(logfile, loglevel="INFO"):

    logging_config = dict(
        disable_existing_loggers=False,
        version=1,
        formatters={
            "f": {
                "format": "%(asctime)-15s %(levelname)s %(name)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        handlers={
            "h1": {
                "class": "logging.StreamHandler",
                "level": loglevel,
                "formatter": "f",
            },
            "h2": {
                "class": "logging.FileHandler",
                "filename": logfile,
                "level": loglevel,
                "formatter": "f",
            },
        },
        root={"handlers": ["h1", "h2"], "level": getattr(logging, loglevel)},
    )
    dictConfig(logging_config)


if __name__ == "__main__":
    get_logger("/tmp/app.log")
    logger = logging.getLogger(name="new_logger")
    logger.info("test log")
    logger.info("test2 log")
