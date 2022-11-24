import sys
def text_analyzer(string=None):

    """\n    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    pass
    if string == None:
        print("What is the text to analyze?")
        x = input("")
        if x.isdigit():
            print("AssertionError: argument is not a string")
        else:
            text_analyzer(x)
    elif type(string) != str:
        print("AssertionError: argument is not a string")
    else:
        punctuation = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        upper_count = sum(1 for c in string if c.isupper())
        lower_count = sum(1 for c in string if c.islower())
        punct_count = sum(1 for c in string if c in punctuation)
        space_count = sum(1 for c in string if c.isspace())
        total = (upper_count + lower_count + punct_count + space_count)
        print("The text contains", total, "character(s):")
        print("-", upper_count, "upper letter(s)")
        print("-", lower_count, "lower letter(s)")
        print("-", punct_count, "punctuation mark(s)")
        print("-", space_count, "space(s)")