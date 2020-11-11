import argparse
import subprocess
import shutil
import os

def get_changed_files(since, until):
    return subprocess.check_output([ 'git', 'diff', '--name-status', since, until], universal_newlines=True).strip()

def main(since, until, output):
    print('{}..{}'.format(since, until))

    files = get_changed_files(since, until)

    if len(output) > 0:
        if os.path.exists(output):
            shutil.rmtree(output)

        os.mkdir(output)
        print('Created path: {}'.format(output))

    for f in files.split('\n'):
        op = f[0]
        path = f[1:].strip()

        print('{} -> {}'.format(op, path))

        if len(output) > 0:
            if op == 'M':
                dest = os.path.join(output, path)
                dest_path = os.path.dirname(dest)

                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                shutil.copyfile(path, dest)

                print('\tCopied {} -> {}'.format(path, dest))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prints changed file among revisions')

    parser.add_argument('-s', '--since', help='Start commit', required=True)
    parser.add_argument('-u', '--until', help='End commit', default='HEAD')
    parser.add_argument('-o', '--output', help='Output path', default='')

    args = parser.parse_args()

    main(args.since, args.until, args.output)
