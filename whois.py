import sys
l = len(sys.argv) - 1
if ( l == 1 ):
    try:
        n = int(sys.argv[1])
    except:
        print("AssertionError: argument is not an integer")
        sys.exit(0)
    if (n == 0):
        print("I'm Zero")
    elif (n % 2 == 0):
        print("I'm Even")
    elif( n % 2 != 0):
        print("I'm Odd")
elif(l > 1):
    print("AssertionError: more than one argument are provided")