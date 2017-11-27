# Scripts
A bunch of automation scripts

# search_for_a_file_in_archives.py
Script for file search inside archives. Requirements: libarchive(library and python package), rarfile.
# How to:
# 1. Install the requirements:
    sudo apt-get install libarchive-dev
    pip install libarchive rarfile
# 2. Run:
    python search_for_a_file_in_archives.py <search_path> <search_pattern>
Example:
    python search_for_a_file_in_archives.py . *.txt
