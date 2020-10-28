from scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner('perr.txt')
    scanner.parse()
    scanner.write_files()
    