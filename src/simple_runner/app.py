import sys

def main(outpath):
    header = ['id', 'val1', 'val2', 'val3']
    with open(outpath, 'w') as out:
        out.write(header)
        out.write('\n')
        for row in range(100):
            out.write(','.join([row] + [random.randint(1, 100) for col in header]))
            out.write('\n')


if __name__ == '__main__':
    main(sys.argv[1])