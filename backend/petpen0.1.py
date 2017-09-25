import argparse
import time
from datetime import datetime
import sys,os,re
import pandas as pd

from model import get_model,backend_model
from utils import train_func, predict_func
from utils import Batch_History,Model_state,load_dataset
from utils import save_history
import utils
# from keras.callbacks import TensorBoard

parser = argparse.ArgumentParser(prog='petpen')
subparsers = parser.add_subparsers()
parser.add_argument('-n', '--name', default='result', help='specify the model name.')
parser.add_argument('-m', '--model', required=True, help='set model folder')
parser.add_argument('-d', '--dataset', required=True, help='set dataset folder')
parser.add_argument('-w', dest='w',action='store_true', help='set -w to load weight')
parser.set_defaults(w=False)

subparser = subparsers.add_parser('train')
subparser.set_defaults(func=train_func)

subparser = subparsers.add_parser('validate')
subparser.set_defaults(func=validate_func)

subparser = subparsers.add_parser('predict')
subparser.set_defaults(func=predict_func)


args = parser.parse_args()
args.func(args)

