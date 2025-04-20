import logging
from pathlib import Path
from typing import Optional
from logging.config import dictConfig
import yaml


def setup_logging(verbose: int = 0, log_file: Optional[str] = None) -> None:
    """
    ロギングを設定する

    Args:
        verbose (int): 冗長性レベル (0: WARNING, 1: INFO, 2: DEBUG)
        log_file (str, optional): ログファイルのパス
    """
    # ログレベルの設定
    level = {
        0: "WARNING",
        1: "INFO",
        2: "DEBUG",
    }.get(verbose, "DEBUG")

    # 基本設定の読み込み
    config_path = Path(__file__).parent.parent / "config" / "logging.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # ログレベルを設定
    for handler in config["handlers"].values():
        handler["level"] = level
    config["root"]["level"] = level

    # ファイル出力の設定
    if log_file:
        log_dir = Path(log_file).parent
        log_dir.mkdir(parents=True, exist_ok=True)
        config["handlers"]["file"]["filename"] = str(log_file)
        config["root"]["handlers"] = ["console", "file"]
    else:
        config["handlers"].pop("file", None)
        config["root"]["handlers"] = ["console"]

    dictConfig(config)
