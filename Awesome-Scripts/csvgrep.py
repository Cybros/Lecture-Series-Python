#!/usr/bin/env python

import argparse
import logging
import re
import sys

import unicodecsv as csv


def csvgrep(args):
    matcher = re.compile(args.pattern)
    writer = csv.writer(args.output, dialect=args.outdialect)
    for input_file in args.inputs:
        reader = csv.reader(
            input_file, dialect=args.indialect, encoding=args.encoding)
        for row in reader:
            try:
                target_value = row[args.target]
            except IndexError:
                logging.warning("Skipping line. Target column doesn't exist on line {} of {}".format(
                    reader.line_num, input_file))
                continue

            if matcher.match(target_value):
                writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find rows in csv file that match pattern in target column.")
    parser.add_argument("-o", "--output",
                        type=argparse.FileType("wb"),
                        default=sys.stdout,
                        help="Output file. Standard out will be used if not specified.")
    parser.add_argument("--indialect",
                        default="excel",
                        help="Dialect of the input file.")
    parser.add_argument("--encoding",
                        default="utf-8",
                        help="Encoding of the input file.")
    parser.add_argument("--outdialect",
                        default="excel",
                        help="Dialect of the output file.")
    parser.add_argument("target",
                        type=int,
                        help="Target column.")
    parser.add_argument("pattern",
                        help="Pattern to match.")
    parser.add_argument("inputs",
                        type=argparse.FileType("rb"),
                        nargs='*',
                        default=sys.stdin,
                        help="CSV File from which to read.")

    args = parser.parse_args()

    csvgrep(args)
