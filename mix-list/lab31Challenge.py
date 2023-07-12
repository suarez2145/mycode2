#!/usr/bin/env python3

# creating word bank list
wordbank= ["indentation", "spaces"]

# creating word tlgstudents list
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# appending the integer 4 to the word bank list
wordbank.append(4)

# printing the word bank list
print(wordbank)

#asking for user to input number betwixt 0 and 20

num = input("Please enter a number between 0 and 20 sir?")

#confirming user input

print("Sir has entered " + num )

# converting num into integer

numInt = int(num)
student_name = tlgstudents[numInt]
print(student_name)

