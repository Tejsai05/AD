# -*- coding: utf-8 -*-
"""day3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tFPKqmDg2nEGe5KMy72wEvP7QDumteeH
"""

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3

if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

