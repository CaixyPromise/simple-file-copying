# fileutil.py
import os


def copy(sourcefilename, targetfilename, bufsize = 1024, tellprogress = None):
    total_size = os.path.getsize(sourcefilename)
    copied_size = 0

    with open(sourcefilename, 'rb') as src, open(targetfilename, 'wb') as dst:
        while True:
            buffer = src.read(bufsize)
            if not buffer:
                break
            dst.write(buffer)
            copied_size += len(buffer)
            if tellprogress:
                tellprogress(copied_size, total_size)
