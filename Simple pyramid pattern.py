# Pattern Printing
# input Number integer
# example n = 5 Than Print The Pattern like
# *
# **
# ***
# ****
# *****
n = int(input("Enter The any Number Between '[1 to 9]' :: \n"))


def ptn(p):
    # outer loop to handle number of rows
    for i in range(0, p):
        # inner loop to handle number of columns
        for j in range(0, i + 1):
            # printing stars
            print('*', end=" ")
        print('\r')


ptn(n)
