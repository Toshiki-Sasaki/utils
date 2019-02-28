import dill
import json
import sys
import os
import glob

#i/o method
def save_txt(data, savepath):
    with open(savepath, "wt") as f:
        for line in data:
            f.write()

def save_dill(data, savepath):
    with open(savepath, "wb") as f:
            dill.dump(data, f)

def save_json(data, savepath):
    with open(savepath, "wt") as f:
            json.dump(data, f)

def read_txt(path):
    with open(path, "rt", encoding="utf-8-sig") as f:
        return f.readlines()

def read_dill(path):
    with open(path, "rb") as f:
        return dill.load(f)

def read_json(path):
    with open(path, "rt") as f:
        return json.load(f)

# directolies
def check_path( path ):
    """
    check the path already exists, if not, make a directory.
    """
    if not os.path.exists( path ):
        os.makedirs(path)
        print('new directory "{}" was created.'.format( path ) )

def get_filelist( path, cond='*' ):
    """
    cond: conditional file name, e.g.) *.py, *.dev.*, etc.
    """
    return glob.glob( os.path.join(path,cond) )

def add_syspath(path):
    sys.path.append( os.path.dirname(os.path.abspath(__file__))+(path) )

# debug
def stop():
    sys.exit(0)
