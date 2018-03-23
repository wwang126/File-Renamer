"""Renames files"""
import re
import os

def main():
    """Main Program runner """
    num_list = []
    for filename in os.listdir(os.getcwd()):
        print(filename)
        num_match = re.search("[0-9]+", filename)
        if num_match:
            num_list.append(num_match.string)
    max_len = len(max(num_list, key=len))
    print(max_len)
    for num in num_list:
        os.rename(num, num.zfill(max_len))
if __name__ == '__main__':
    main()
