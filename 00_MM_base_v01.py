# function go here

# Checks user has entered yes / no to a question 
def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
  
    elif response == "no" or response == "n":
      return "no"

    else:
      print("Please enter yes or no")

# checks the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

# Checks users enter integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please eneter an integer.")        
# main routine starts here


# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0
# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
  print("Instructions go here")

print()

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter yout name or 'xxx' to quit: ")

    if name == 'xxx':
        break
    
    age = num_check("Age: ")

    if 12 <= age <= 120:
       pass
    elif age < 12:
       print("Sorry you are too young for this movie")
       continue
    else:
       print("?? That looks like a typo, Please try again.")
       continue

    tickets_sold += 1


# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remanining".format(tickets_sold, MAX_TICKETS - tickets_sold))