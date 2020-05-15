# Init variables
thematrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""
profession = ["","","",""]
adj = ["",""]

# get user input 
print("welcome user!")
print("lets play a game of madlibs")
neo = input("please tell me your name: ")

# Getting the matrix variable from user
print(f"Hello {neo}! Are you ready")
thematrix = input("what is somthing you want to know more about: ")

# Getting system variable from user
print(f"Ooooh! You want to know more about {thematrix} huh?")
print(f"Okay well frist, tell me what you already know about {thematrix}")
system = input(f"what noun would you categorize {thematrix} as: ")

# Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}: ")

# Getting inside variable from user
inside = input(f"Now give me any noun (presnet tense): ")
 
# Getting all profession variable from user
print(f"Okay, now i need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"profession (plural) {i+1} / {len(profession)}: ")

# Getting the save variable
save = input(f"give me a  verb (present tense): ")

# Getting the unplugged variable 
unplugged = input(f"Now give me another verb (past tense): ")

# Getting the adjectives
print(f"I need 2 dystopian adjectives")

for i in range(len(adj)):
    adj[i] = input(f"adjective {i+1} / {len(adj)}: ")

# Getting the fight varible
fight = input(f"& a verb: ")

# Init story 
madlibsstory = (f"{thematrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{profession[0]},{profession[1]},{profession[2]},{profession[3]}. The very minds " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people "+
f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# print story 
print(madlibsstory)
