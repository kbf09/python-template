import sys

import logging
import argparse
from logging_config import setup_logging

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="詳細出力レベルを上げる (最大 -vv)",
    )
    parser.add_argument("--log-file", help="ログファイルのパス")
    args = parser.parse_args()

    setup_logging(args.verbose, args.log_file)

    logger.info("info")
    logger.debug("debug")


if __name__ == "__main__":
    main()
