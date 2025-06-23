# #question 2
# print("Enter marks out of 100 for 5 subjects:")
# subject1 = float(input("Subject 1: "))
# subject2 = float(input("Subject 2: "))
# subject3 = float(input("Subject 3: "))
# subject4 = float(input("Subject 4: "))
# subject5 = float(input("Subject 5: "))
#
#
# total = subject1 + subject2 + subject3 + subject4 + subject5
# percentage = (total / 500 * 100)
#
# if percentage >= 60:
#     grade = 'A'
# elif percentage >= 50:
#     grade = 'B'
# elif percentage >= 40:
#     grade = 'C'
# elif percentage >= 33:
#     grade = 'D'
# else:
#     grade = 'Fail'
#
# # Output the results
# print("\n--- Result ---")
# print(f"Total Marks: {total}")
# print(f"Percentage: {percentage:.2f}%")
# print(f"Grade: {grade}")




#Ques 3

num = int(input("Enter a number to find its factorial: "))


if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i


    print(f"The factorial of {num} is: {factorial}")

