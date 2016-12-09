import sys
import os
import csv
import argparse


def read_src_file(src_file_path):
    pass


def format_to_geojson():
    pass


def write_dest_file(dest_file_path):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', required=True,
                        help='Source CSV file to read from')
    parser.add_argument('--dest', required=True,
                        help='Destination GeoJSON file to write to')
    parser.add_argument('--excel', default=False, action='store_true',
                        help='Use for CSV files with Excel format')
    opts = parser.parse_args()
    if not (opts.src and opts.dest):
        parser.error("You have to specify both source and destination file.")

    return opts


def main(argv):
    # get args
    opts = parse_args()

    # read csv file

    # format file to geoJSON

    # write dest file


if __name__ == '__main__':
    main()