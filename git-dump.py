import argparse
import subprocess

def parse_rev(rev):
    return subprocess.check_output([ 'git', 'rev-list', '-1', rev ], universal_newlines=True).strip()

def dump(rev, label):

    if not rev:
        rev = 'HEAD'

    id = parse_rev(rev)

    if not label:
        label = rev

    with open('.commits', 'a') as f:
        print('{}\t{}'.format(id, label), file=f)

    print('Saved {} as "{}" in .commits'.format(id, label))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Appends commit id with label to file .commits')

    parser.add_argument('rev', help='Revision id', nargs='?')
    parser.add_argument('-l', '--label', help='Label for commit', nargs='?')

    args = parser.parse_args()

    dump(args.rev, args.label)
