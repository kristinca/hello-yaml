import argparse
import re


def set_data_params(paramsList, dataDict):
    for el in paramsList:
        dataDict['args.' + re.findall(r'\w+', el)[0]] = re.findall(r'\w+', el)[1]


try:

    parser = argparse.ArgumentParser()
    parser.add_argument('--one', help='first REQUIRED', required=True)
    parser.add_argument('--two', help='two REQUIRED', required=True)
    parser.add_argument('--three', help='three REQUIRED', required=True)

    args = parser.parse_args()

    a1 = str(args)
    a2 = re.sub(r'Namespace\(', '', a1)
    a3 = re.sub(r'\)', '', a2).replace('=', ':').split(", ")
    a4 = dict()

    set_data_params(a3, a4)

    print(a4)
    print(type(a4))

except Exception as e:
    print(e)