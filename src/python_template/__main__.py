"""アプリケーションのエントリーポイント。

このモジュールは、コマンドラインからアプリケーションを実行するための
エントリーポイントを提供します。
"""

import logging
import argparse
from python_template.logging_config import setup_logging


def main() -> None:
    """コマンドライン引数を解析し、アプリケーションを実行します。"""
    parser = argparse.ArgumentParser(
        description="Pythonテンプレートアプリケーション",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="詳細出力レベルを上げる (最大 -vv)",
    )
    parser.add_argument(
        "--log-file",
        help="ログファイルのパス",
    )
    args = parser.parse_args()

    setup_logging(args.verbose, args.log_file)
    logger = logging.getLogger(__name__)

    logger.info("アプリケーションを開始します")
    logger.debug("デバッグ情報を出力します")


if __name__ == "__main__":
    main()
