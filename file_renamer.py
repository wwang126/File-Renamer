"""Renames files"""
import re
import os

def main():
    """Main Program runner """
    num_list = []
    end_list = []
    match_list = []
    for filename in os.listdir(os.getcwd()):
        print(filename)
        num_match = re.search("[0-9]+", filename)
        if num_match:
            match_list.append(num_match.string)
            num_list.append(num_match.group(0))
            end_list.append(filename[num_match.end(0):])
    max_len = len(max(num_list, key=len))
    print(max_len)
    idx = 0
    for name in match_list:
        new_name = num_list[idx].zfill(max_len) + end_list[idx]
        os.rename(name, new_name)
        idx += 1
if __name__ == '__main__':
    main()
