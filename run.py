from app import parse_file
import argparse


parser = argparse.ArgumentParser(description='Super cool workout data tool')
parser.add_argument('--file', help='file path')

args = parser.parse_args()
parse_file(args.file)