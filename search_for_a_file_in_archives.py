#!/usr/bin/env python

import libarchive.public, rarfile, locale, fnmatch, os, sys

locale.setlocale(locale.LC_ALL, '')

def find_files(directory):
    found = set()
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, '*.7z') or fnmatch.fnmatch(basename, '*.gz') or fnmatch.fnmatch(basename, '*.rar') or fnmatch.fnmatch(basename, '*.tar') or fnmatch.fnmatch(basename, '*.tar.*') or fnmatch.fnmatch(basename, '*.zip'):
                filename = os.path.join(root, basename)
                yield filename

def find_file(filename, pattern):
    found = set()
    try:
        if os.path.splitext(filename)[1] == '.rar':
            with rarfile.RarFile(filename) as archive:
                for entry in archive.infolist():
                    if fnmatch.fnmatch(os.path.basename(entry.filename), pattern):
                        found.add(filename)
        else:
            with libarchive.public.file_reader(filename) as archive:
                for entry in archive:
                    if fnmatch.fnmatch(os.path.basename(entry.pathname), pattern):
                        found.add(filename)
    except:
        pass
    if (len(found) > 0):
        for f in found:
            print os.path.abspath(f)

def main(argv):
    if (len(sys.argv) < 3) or sys.argv[1] == '-h':
        print 'How to use:'
        print sys.argv[0] + ' <search_path> <search_pattern>'
        print 'Example: ' + sys.argv[0] + ' . *.txt'
        sys.exit()
    else:
        for filename in find_files(sys.argv[1]):
            find_file(filename, sys.argv[2])

if __name__ == "__main__":
    main(sys.argv[1:])
