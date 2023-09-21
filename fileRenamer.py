from argparse import ArgumentParser
from os import listdir, rename
from os.path import isfile, isdir, join as os_join, isabs, abspath

parser = ArgumentParser(description='bulk rename files')

parser.add_argument(
    'path',
    help='path to dir where files are stored',
)

parser.add_argument(
    'extension',
    help='files extension (without the first dot)'
)

args = parser.parse_args()

if not isabs(args.path):
    args.path = abspath(args.path)

if isdir(args.path):
    files = [
        filename
        for filename in listdir(args.path)
        if (isfile(filename) and filename.endswith(args.extension))
    ]
    files.sort()

    for n, file in enumerate(files):
        print()
        print(f'[{n + 1}/{len(files)}] {file}')
        try:
            case = input('[r]ename | [d]elete | empty to skip: ').strip().lower()
        except:
            raise SystemExit

        if case == 'd':
            new_name = 'to_remove_' + str(n)
        elif case != 'r':
            print('skipped')
            continue

        else:
            try:
                new_name = input('New name: ').strip()
            except:
                raise SystemExit

            if not new_name:
                print('skipped')
                continue
                new_name += '.' + args.extension

        old_path = os_join(args.path, file)
        new_path = os_join(args.path, new_name)
        rename(old_path, new_path)
        print(f'renamed to {new_name}')
