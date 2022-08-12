import time
from params import set_args, set_data_params

if __name__ == '__main__':
    args = set_args()
    api_params = ('oNe', 'tWo', 'tHrEe', 'fOuR', 'fIvE', 'sIx', 'sEvEn')
    # api_params = ('oNe', 'tWo', 'tHrEe', 'fOuR', 'fIvE', 'sIx', 'sEvEn',
    #               'oNe1', 'tWo1', 'tHrEe1', 'fOuR1', 'fIvE1', 'sIx1', 'sEvEn1',
    #               'oNe2', 'tWo2', 'tHrEe2', 'fOuR2', 'fIvE2', 'sIx2', 'sEvEn2',
    #               'oNe3', 'tWo3', 'tHrEe3', 'fOuR3', 'fIvE3', 'sIx3', 'sEvEn3'
    #               )
    positional_params = (args.one, args.two, args.three, args.four, args.five, args.six, args.seven)
    # positional_params = (args.one, args.two, args.three, args.four, args.five, args.six, args.seven,
    #                      args.one1, args.two1, args.three1, args.four1, args.five1, args.six1, args.seven1,
    #                      args.one2, args.two2, args.three2, args.four2, args.five2, args.six2, args.seven2,
    #                      args.one3, args.two3, args.three3, args.four3, args.five3, args.six3, args.seven3
    #                      )

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
