import logging
import sys
from pathlib import Path
from typing import Optional


def _get_log_level(verbose: int) -> int:
    """
    verboseレベルに応じたロギングレベルを返す

    Args:
        verbose (int): 冗長性レベル

    Returns:
        int: ロギングレベル
    """
    return {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }.get(verbose, logging.DEBUG)


def _create_console_handler() -> logging.Handler:
    """
    コンソール出力用のハンドラを作成する

    Returns:
        logging.Handler: コンソールハンドラ
    """
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
    )
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    return handler


def _create_file_handler(log_file: str) -> logging.Handler:
    """
    ファイル出力用のハンドラを作成する

    Args:
        log_file (str): ログファイルのパス

    Returns:
        logging.Handler: ファイルハンドラ
    """
    log_dir = Path(log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
    )
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    return handler


def setup_logging(verbose: int = 0, log_file: Optional[str] = None) -> None:
    """
    ロギングを設定する

    Args:
        verbose (int): 冗長性レベル (0: WARNING, 1: INFO, 2: DEBUG)
        log_file (str, optional): ログファイルのパス
    """
    level = _get_log_level(verbose)
    handlers = [_create_console_handler()]

    if log_file:
        handlers.append(_create_file_handler(log_file))

    logging.basicConfig(
        level=level, handlers=handlers, datefmt="%Y-%m-%dT%H:%M:%S%z", force=True
    )
