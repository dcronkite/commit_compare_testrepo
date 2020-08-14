import sys
import random


def main(outpath):
    header = ['id', 'val1', 'val2', 'val3']
    with open(outpath, 'w') as out:
        out.write(','.join(header))
        out.write('\n')
        for row in range(100):
            out.write(','.join(str(x) for x in [row] + [random.randint(0, 20) for col in header]))
            out.write('\n')


if __name__ == '__main__':
    main(sys.argv[1])
