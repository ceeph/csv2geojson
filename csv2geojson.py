"""
    csv2geojson

    Script to convert csv file to geojson
"""
import sys
import os
import csv
import json
import argparse


def read_src_file(src_file_path, excel):
    """Reads source CSV file and returns file

    Parameters:
        src_file_path : string
        excel : bool

    Returns:
        csv_reader : csv.reader object
    """
    try:
        f = open(src_file_path)
        if excel:
            csv_reader = csv.reader(f, dialect='excel')
        else:
            csv_reader = csv.reader(f)
        return csv_reader, f
    except IOError as e:
        print("Error: %s not found." % src_file_path)


def format_to_geojson(index, line):
    data = {}
    data['id'] = index
    data['type'] = 'Feature'
    data['properties'] = {}
    data['geometry'] = {
        'type': 'Point',
        'coordinates': (float(line[0]), float(line[1]))
    }
    return data


def write_dest_file(src_file, dest_file_path):
    """Formats input data to gejson and writes result
    to destination file.

    Parameters:
        src_file : csv.reader
        dest_file_path : string
    """
    # basic geojson structure
    parsed_data = {
        "type": "FeatureCollection",
        "features": []
    }
    # skip header row containing field names
    headers = src_file.__next__

    # parse rows and add to object
    for line, index in enumerate(src_file):
        parsed_data['features'].append(format_to_geojson(line, index))

    with open(dest_file_path, 'w') as stream:
        json.dump(parsed_data, stream, sort_keys=False)


def parse_args():
    """Parses arguments from command line

    Returns:
        opts : Namespace : contains arg name and value
    """
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


def main():
    # get args
    opts = parse_args()

    # read csv file
    src_file, src_file_handler = read_src_file(opts.src, opts.excel)

    # format file to geoJSON

    # write dest file
    write_dest_file(src_file, opts.dest)
    src_file_handler.close()


if __name__ == '__main__':
    main()
