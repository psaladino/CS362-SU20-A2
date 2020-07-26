# CS362-SU20, A2-TDD
# Ryan Stachura
# Oregon State University

SYMBOLS = "~`!@#$%^&*()_+-="

def check_pwd(pwd):

    if (len(pwd)<8 or len(pwd)<20):
        return False

    return True
