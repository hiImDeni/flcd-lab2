from scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner('p1.txt')
    scanner.parse()
    scanner.write_files()
    