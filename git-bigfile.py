import argparse
import subprocess
import re

requery = '''[0-9]+ blob [a-z0-9]+[ ]+([0-9]+)[ \t]+(.+)'''

def size(s):
    if s < 1024:
        return '{0:.2f} B'.format(s)
    elif s < 1024**2:
        return '{0:.2f} KB'.format(s/1024)
    elif s < 1024**3:
        return '{0:.2f} MB'.format(s/1024**2)
    elif s < 1024**4:
        return '{0:.2f} GB'.format(s/1024**3)
    else:
        return '{0:.2f}'.format(int(s))

def find(rev, minSize):

    print('Finding files bigger than {}\n'.format(size(minSize)))

    output = subprocess.check_output([ 'git', 'ls-tree', '-rl', rev ], universal_newlines=True).strip()

    for line in output.split('\n'):
        try:
            m = re.search(requery, line.strip())

            s = int(m.group(1))

            if s > minSize:
                print(m.group(2), size(s), sep='\t')
        except Exception as ex:
            print('Error parsing {}'.format(line))

def parse_size(size):
    if size.upper().endswith('K'):
        return 1024 * int(size[:-1])
    elif size.upper().endswith('M'):
        return 1024**2 * int(size[:-1])
    elif size.upper().endswith('G'):
        return 1024**3 * int(size[:-1])
    else:
        return int(size)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Finds big files in revision')

    parser.add_argument('rev', help='Revision id')
    parser.add_argument('-s', '--size', help='Minimum size (eg. 1024, 10K, 5M)', default='1024')

    args = parser.parse_args()

    find(args.rev, parse_size(args.size))
