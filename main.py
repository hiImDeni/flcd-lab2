from scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner('perr.txt')
    scanner.get_tokens()
    scanner.write_files()
    