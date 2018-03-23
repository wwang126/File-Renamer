"""Renames files"""
import re

def main():
    """Main Program runner """
    test_string = "01-asdfasdf01-asdfasf10adsfasd22adsf3344"
    num_list = re.findall("[0-9]+", test_string)
    print(num_list)
    max_len = len(max(num_list, key=len))
    print(max_len)
    new_list = []
    for str in num_list:
        new_list.append(str.zfill(max_len))
    print(new_list)
if __name__ == '__main__':
    main()
