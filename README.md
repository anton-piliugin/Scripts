# Scripts
A bunch of usefull automation scripts to run under Linux

# search_for_a_file_in_archives.py
Script for a case-sensitive(!) file search inside archives. Requirements: libarchive(library and python package), rarfile.
Script searches for archives recursively. The result of successfull search will be a list of absolute path(s) to archive(s), that contains file(s) matched your search.

# 1. Install the requirements:
    sudo apt-get install libarchive-dev
    sudo pip install libarchive rarfile
# 2. Run:
    python search_for_a_file_in_archives.py <search_path> <search_pattern>
Example:

    python search_for_a_file_in_archives.py . *.txt
    
Special characters that can be used in a search pattern:

    * – matches everything
    ? – matches any single character
    [seq] – matches any character in seq
    [!seq] – matches any character not in seq
