# CS362-SU20, A2-TDD
# Ryan Stachura
# Oregon State University

SYMBOLS = "~`!@#$%^&*()_+-="

def check_pwd(pwd):

    if (len(pwd)>=8 and len(pwd)<=20):
        return True

    else:
        return False

    return False
