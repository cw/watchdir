# standard libs
import zipfile
import glob
import os
import datetime
import ConfigParser

# nonstandard libs
import httplib2 # http://code.google.com/p/httplib2/


def write_to_zip():
    """adapted from http://effbot.org/librarybook/zipfile.htm
    open the zip file for writing, and write stuff to it"""

    file = zipfile.ZipFile("test.zip", "w")
    try:
        for name in glob.glob("samples/*"):
            file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    finally:
        file.close()

    # open the file again, to see what's in it

    file = zipfile.ZipFile("test.zip", "r")
    for info in file.infolist():
        print info.filename, info.date_time, info.file_size, info.compress_size

def upload_zip():
    pass


if __name__ == "__main__":
    # maybe look for timestamp changes?
    write_to_zip()
    upload_zip()
