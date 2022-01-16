# coding=utf-8
import os
from sys import argv


def count_data(filename):
    with open(filename) as f:
        lines = 0
        a = 0
        buf_size = 1024 * 1024
        read_f = f.read

        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            a += buf.count('а')
            buf = read_f(buf_size)

        return {'char_a': a, 'lines': lines, }


if __name__ == '__main__':
    if len(argv) < 2:
        print('Usage: python file_data.py <filename>')
    else:
        txt_file = os.path.join(os.getcwd(), argv[1])
        print(count_data(txt_file))
