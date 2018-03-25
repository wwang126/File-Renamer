"""Renames files"""
import re
import os

def main():
    """Main Program runner """
    match_list = []
    num_list = []
    for filename in os.listdir(os.getcwd()):
        num_match = re.search("([0-9]+)(.*)", filename)
        if num_match:
            match_list.append(num_match)
            num_list.append(num_match.group(1))
    max_len = len(max(num_list, key=len))
    print(max_len)
    for match in match_list:
        name = match.group(0)
        new_name = match.group(1).zfill(max_len) + match.group(2)
        os.rename(name, new_name)
if __name__ == '__main__':
    main()
