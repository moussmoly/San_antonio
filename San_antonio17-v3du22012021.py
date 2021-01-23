quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

charaters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté"]

def show_random_quote(my_list):
    # TOOO: get a random number
    item = my_list[0]
    return item

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

user_answer = "A"
    
while user_answer != "B":
    print(show_random_quote(quotes))
    user_answer = "B"
