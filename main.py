import pandas as pd
import time
import os
from dbx import init_doc
import argparse



fn = os.getcwd() + '/pandapush.csv'
fn = fn.replace(os.path.sep, '/')

def init_pandapush(fn):
    if not os.path.exists(fn):
        PandaPush = pd.DataFrame({'unix': [],
                                  'message': []})
        PandaPush.to_csv(fn, index=False)
        print("File does not exist. Creating file.")
    else:
        print("File exists.")

    PandaPush = pd.read_csv(fn)
    return PandaPush

class NewPush:

    def __init__(self, message):
        self.msg = message

    def push(self):
        PandaPush = init_pandapush(fn)
        unix = time.time()

        df = pd.DataFrame({'unix':[unix],
                           'message':[self.msg]})
        df = pd.concat([PandaPush, df])
        df.to_csv(fn, index=False)
        with open(fn, 'rb') as f:
            init_doc(f)


parser = argparse.ArgumentParser(description='Your go-to trash command line tool for dropbox.')
parser.add_argument('-i', '--input', help='Input desired text', required=True)
args = parser.parse_args()

print("Input text: %s" % args.input)
NewPush(args.input).push()