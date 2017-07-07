import brainfuck
import sys

# https://github.com/RoliSoft/Esoteric-Code-Interpreter/blob/master/Spoon.cs

dic = {
    "1": '+',
    "000": '-',
    "010": '>',
    "011": '<',
    "0011": ']',
    "00100": '[',
    "001010": '.',
    "0010110": ':',
    "00101111": '\0'
}
def spoon_to_brainfuck(input):
    input = input.replace(" ", "").strip()
    bf = ""
    last = ""
    for ch in input:
        last += ch;
        if (dic.has_key(last)):
            bf += dic[last]
            last = ""
    return bf

def execute(filename):
    f = open(filename, "r")
    spoon = f.read()
    f.close()

    bf = spoon_to_brainfuck(spoon)
    brainfuck.evaluate(bf)

def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__":
    main()
