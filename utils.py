import dill
import json

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

#
