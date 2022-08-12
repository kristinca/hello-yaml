from params import set_args, set_data_params

if __name__ == '__main__':
    args = set_args()
    api_params = ['oNe', 'tWo', 'tHrEe', 'fOuR', 'fIvE', 'sIx', 'sEvEn']
    positional_params = [args.one, args.two, args.three, args.four, args.five, args.six, args.seven]
    data = set_data_params(api_params, positional_params)
    print(data)