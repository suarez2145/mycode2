#!/usr/bin/env python3


def main():
    with open("dracula.txt","r") as foo:
        count = 0
        for line in foo:
            word = 'vampire'
            if word in line.lower():
                count += 1
                # look at line in loop
                print(line, end='')
                print(count)



















if __name__ == "__main__":
    main()
