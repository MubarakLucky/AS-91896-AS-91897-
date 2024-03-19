# functions go here

# Checks users enter integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please eneter an integer.")


# main routine goes here
tickets_sold = 0
while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break
    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age <12:
        print("Sorry your are too young for this movie")
        continue
    else:
        print("?? Thats looks like a typo, please try again.")
        continue