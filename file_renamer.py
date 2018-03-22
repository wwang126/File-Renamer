import re

def main():
    """Main Program runner """
    test_string = "01-asdfasdf01-asdfasf10adsfasd22adsf33"
    name_list = re.findall("[0-9]+-?",test_string)

if __name__ == '__main__':
    main()
