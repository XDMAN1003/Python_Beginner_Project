# String concatenation (aka how to put string together)
# suppose we want to create a string that can say "subscribe to ______"
# Youtuber = "Lebron James" # some string variable

# A few way to do this
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subsribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")


madlib = f"Computer programming is so {adj}! It makes me so exicted all the time  " \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)