import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from zoneinfo import ZoneInfo

LOG_DIRECTORY = ".logs"

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)


def customTime(*args):
    return datetime.now(ZoneInfo("Asia/Tokyo")).timetuple()


# ログフォーマットの設定
log_format = "[%(asctime)s][%(levelname)s] - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S %z"
logging.basicConfig(format=log_format, datefmt=datefmt, level=logging.DEBUG)
formatter = logging.Formatter(log_format)
formatter.converter = customTime

# ファイルハンドラーの設定
handler = TimedRotatingFileHandler(
    LOG_DIRECTORY + f"/{datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y%m%d')}.log",
    when="midnight",
    interval=1,
    backupCount=365,
)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

# ログ設定
root_logger = logging.getLogger(__name__)
root_logger.addHandler(handler)


def debug(message: str):
    root_logger.debug(message)


def info(message: str):
    root_logger.info(message)


def warning(message: str):
    root_logger.warning(message)


def error(message: str):
    root_logger.error(message)
