friend_name = input("Your Friend's Name: ")
number_of_hours = int(input("Number of Hours: "))
vehicle = input("Favourite Vehicle: ")
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
verb_ing = input("Verb(Continuos Format): ")
animal = input("Animal: ")
adjective3 = input("Adjective: ")
past_tense_verb = input("Verb (Past Tense): ")
adjective4 = input("Adjective: ")
past_tense_verb1 = input("Verb (Past Tense): ")
past_tense_verb2 = input("Verb (Past Tense): ")
place = input("Just a place: ")
verb = input("Verb (Present Tense): ")

madlibs = f"""Last month, I went to Disney World with {friend_name}. We
traveled for {number_of_hours} hours by {vehicle}. Finally, we
arrived and it was very {adjective1}. There were
{adjective1} people {verb_ing} everywhere. There
were also people dressed up in {animal} costumes.\n

 I wish it had been more {adjective3}, but we {past_tense_verb} anyway. 
 We also went on a(n) {adjective4} ride
called Magic (noun). {friend_name} nearly fell off a ride and had to be
{past_tense_verb1}. Later, we went to the hotel and
{past_tense_verb2}. Next year, I want to go to {place},
where we can {verb}. """

print(madlibs)