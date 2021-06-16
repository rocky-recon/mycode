#!/usr/bin/env python3




def stars_going_up():
    # outer loop to handle rows
    for i in range (5, 0, -1):
        print(" ")
        # inner loop to handle columns
        for j in range(i, 5):
            # print stars
            print("* ", end = " ")
    for i in range (0, 5):
        print(" ")
        for j in range(i, 5):
            print("* ", end = " ")
        print("\r")         
stars_going_up()


#def main():
 #   stars_going_up(n_rows)
