import argparse



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Make a file')
    parser.add_argument('--input')
    parser.add_argument('--output')


    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write('Input = {}\n'.format(args.input))
