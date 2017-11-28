# Scripts
A bunch of usefull automation scripts to run under Linux

# search_for_a_file_in_archives.py
Script for a case-sensitive(!) file search inside archives. Requirements: libarchive(library and python package), rarfile.
Script searches for archives recursively. The result of search will be a list of absolute paths to archives, that contains files matched your search (if any has been found).

# 1. Install the requirements:
    sudo apt-get install libarchive-dev
    sudo pip install libarchive rarfile
# 2. Run:
    python search_for_a_file_in_archives.py <search_path> <search_pattern>
  
Special characters that can be used in a search pattern:

    * - matches everything
    ? - matches any single character
    [seq] - matches any character in seq
    [!seq] - matches any character not in seq

Example:

    python search_for_a_file_in_archives.py . *.txt
  
