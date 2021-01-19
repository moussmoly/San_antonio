quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

user_answer = "B"

if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
    pass
    # show another quote
    
def show_random_quote(my_list):
    # get a random number
    quote = my_list[1]
    print(quote)

show_random_quote(quotes)


