import argparse
import sys

from homebrew import HomeBrew, __version__


def parse_args(args):
    parser = argparse.ArgumentParser(description="Get homebrew info")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    return parser.parse_args(args)


def main():
    parse_args(sys.argv[1:])
    HomeBrew().info
