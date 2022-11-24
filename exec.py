import sys
n = len(sys.argv)
if (n >= 1):
    s = ' '.join(sys.argv[1:])
    print(s[::-1].swapcase())
sys.exit(0)