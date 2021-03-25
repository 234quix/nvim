"""
Python script skeleton
"""
import logging
import time
import argparse

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()

    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(description="Python skeleton")
    parser.add_argument(
        "--debug",
        help="Display debugging information.",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        "positional_argument", nargs="?", type=str, help="Positional argument."
    )
    parser.add_argument(
        "-b",
        "--boolean_flag",
        help="Boolean flag.",
        dest="boolean_flag",
        action="store_true",
    )
    parser.set_defaults(boolean_flag=False)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=format)
    return args


if __name__ == "__main__":
    main()
