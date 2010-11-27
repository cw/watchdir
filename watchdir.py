# standard libs
import zipfile
import glob
import os
import datetime
import ConfigParser
import urllib

# nonstandard libs
import httplib2 # http://code.google.com/p/httplib2/

config = ConfigParser.RawConfigParser()
config.read('config.ini')
# config.ini is expected to have a single group called [settings]
# [settings] is expected to contain two config options called
# url and directory

URL = config.get("settings", "url")
DIRECTORY = config.get("settings", "directory")

def write_to_zip():
    """adapted from http://effbot.org/librarybook/zipfile.htm
    open the zip file for writing, and write stuff to it"""

    assert os.path.exists(DIRECTORY), "%s not found" % DIRECTORY

    file = zipfile.ZipFile("test.zip", "w")
    try:
        for name in glob.glob("%s/*" % DIRECTORY):
            file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    finally:
        file.close()

    # open the file again, to see what's in it

    file = zipfile.ZipFile("test.zip", "r")
    for info in file.infolist():
        print info.filename, info.date_time, info.file_size, info.compress_size

def upload_file(path):
    """
    Only upload html files that are not named all.html
    """
    if path.lower().endswith("html") and "all.html" not in path:
        #print "uploading", path
        h = httplib2.Http()
        f = open(path, "r")
        try:
            s = f.read()
        finally:
            f.close()
        timestamp = os.stat(path).st_mtime
        data = {'contents': s, "filename": os.path.split(path)[1], "timestamp": timestamp}
        body = urllib.urlencode(data)
        resp, content = h.request(URL, "POST", body=body)
        print content

def upload_files():
    """
    """
    assert os.path.exists(DIRECTORY), "%s not found" % DIRECTORY
    for root, dirnames, filenames in os.walk(DIRECTORY):
        for filename in filenames:
            upload_file(os.path.join(root, filename))


if __name__ == "__main__":
    # maybe look for timestamp changes?
    #write_to_zip()
    upload_files()
