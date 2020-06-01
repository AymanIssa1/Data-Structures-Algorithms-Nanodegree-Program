## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print(os.listdir("./testdir/"))

# Let us check if this file is indeed a file!
print(os.path.isdir("./testdir/"))
print(os.path.isfile("./testdir/t1.h"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix == '' or suffix is None:
        return []

    if len(os.listdir(path)) == 0:
        return []

    elements = os.listdir(path)
    files_paths = []
    folder_paths = []

    for element in elements:
        print(element)
        if os.path.isdir(path + element):
            print("adding dir ...")
            folder_paths.append(path + element + '/')

        if os.path.isfile(path + element) and element[-len(suffix):] == suffix:
            print("adding file ...")
            files_paths.append(element)

    for folder_path in folder_paths:
        files_paths.extend(find_files(suffix, folder_path))

    return files_paths


base_path = "./testdir/"

files = find_files(None, None)
print("files: " + str(files))

files = find_files('', None)
print("files: " + str(files))

files = find_files('', base_path)
print("files: " + str(files))

files = find_files('.c', base_path)
print("files: " + str(files))

files = find_files('.h', base_path)
print("files: " + str(files))
