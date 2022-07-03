from params import set_args, set_data_params

if __name__ == '__main__':
    args = set_args()
    api_params = ['oNe', 'tWo', 'tHrEe', 'fOuR', 'fIvE', 'sIx', 'sEvEn']
    data = set_data_params(api_params, list(vars(args).values()))
    print(data)
