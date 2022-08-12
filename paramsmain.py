import time
from params import set_args, set_data_params

if __name__ == '__main__':
    args = set_args()
    api_params = ('oNe', 'tWo', 'tHrEe', 'fOuR', 'fIvE', 'sIx', 'sEvEn')
    positional_params = (args.one, args.two, args.three, args.four, args.five, args.six, args.seven)

    # with the builtin function
    start = time.perf_counter()
    data = {k: v for k,v in zip(api_params, positional_params) if v is not None}
    end = time.perf_counter()
    print(f'The mapping with builtin function finished in {round(end - start, 8)} seconds.\n')
    print(data, '\n')

    # with the maping function
    start = time.perf_counter()
    data_map = set_data_params(api_params, positional_params)
    end = time.perf_counter()
    print(f'The mapping with the mapping function finished in {round(end - start, 8)} seconds.\n')
    # print(positional_params)
    print(data_map)
