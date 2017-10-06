#!/usr/bin/env python

"""csv_constructor.py: Download and create csv file for dataset"""
__author__      = "Abner Tellez"
__copyright__   = "Copyright 2017, NTHU"

import csv
import glob
import os
import shutil
import urllib.request
from zipfile import ZipFile

DATA_FILES = "_labelled.txt"
DATA_SET_DIR = "dataset/"
DATA_SET_CSV = DATA_SET_DIR + "dataset.csv"
FILE_NAME = "dataset.zip"

def download_zip(url) :
    print('Download files...')
    urllib.request.urlretrieve(url, "dataset.zip")
    # check if directory exists
    if not os.path.exists(DATA_SET_DIR):
        os.makedirs(DATA_SET_DIR)

    # opening the zip file
    with ZipFile(FILE_NAME, 'r') as zip:
        print('Extracting files...')
        for file_item in zip.namelist():
            if DATA_FILES  in file_item and "__MACOSX" not in file_item: 
                source = zip.open(file_item)
                target = open(os.path.join(DATA_SET_DIR, os.path.basename(file_item)), "wb")
                with source, target:
                    # extracting all *.txt 
                    shutil.copyfileobj(source, target)
        os.remove("dataset.zip")
        create_csv()

def create_csv():
    with open(DATA_SET_CSV, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter='|')
        filewriter.writerow(['Source', 'Sentence', 'Score'])
        files = glob.glob(DATA_SET_DIR + "*.txt")
        for file_item in files:
            with open(file_item) as infile:
                source = file_item[file_item.find("dataset/")+len("dataset/"):file_item.rfind("_labelled")]
                for line in infile:
                    filewriter.writerow([source] + line.rstrip().split('\t'))
    print('Done!')
