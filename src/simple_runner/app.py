import sys
import random
from loguru import logger  # test external module, ensure correct path being set
from simple_runner.util import get_string_options


def main(outpath):
    header = ['id', 'val1', 'val2', 'val3', 'val4', 'val5']
    n_num = 4
    n_str = 1
    assert n_num + n_str + 1 == len(header)
    str_options = get_string_options()
    with open(outpath, 'w') as out:
        out.write(','.join(header))
        out.write('\n')
        for row in range(100):
            out.write(','.join(str(x) for x in [row] +
                               [random.randint(0, 20) for _ in range(n_num)] +
                               [random.choice(str_options) for _ in range(n_str)]
                               ))
            out.write('\n')


if __name__ == '__main__':
    main(sys.argv[1])
