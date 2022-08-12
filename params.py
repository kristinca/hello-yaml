import argparse
import time


def set_data_params(apiParams, posArgs):
    """
    A function to map the positional arguments to the API parameters
    :param apiParams: list, the API parameters
    :param posArgs: list, the positional parameters
    :return: dict
    """
    dataDict = dict()
    # start = time.perf_counter()
    for i in range(len(apiParams)):
        if posArgs[i]:
            dataDict[f'{apiParams[i]}'] = posArgs[i]
    # end = time.perf_counter()
    # print(f'The mapping finished in {round(end - start, 8)} seconds.\n')
    return dataDict


def set_args():
    """
    A function to set the positional parameters
    :return: Namespace object, the positional arguments
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--one', type=int, help='first REQUIRED', required=True)
        parser.add_argument('--two', type=str, help='two REQUIRED', required=True)
        parser.add_argument('--three', type=list, help='three REQUIRED', required=False)
        parser.add_argument('--four', type=tuple, help='four REQUIRED', required=True)
        parser.add_argument('--five', type=float, help='five', required=False)
        parser.add_argument('--six', type=set, help='six REQUIRED', required=True)
        parser.add_argument('--seven', type=int, help='seven', required=False)

        return parser.parse_args()
    except Exception as e:
        print(e)

