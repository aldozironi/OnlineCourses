import sys

def test(did_pass):
    """ 
    Print the result of a test.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = f"Test at line {linenum} ok."
    else:
        msg = f"Test at line {linenum} FAILED."
    print(msg)
    return None