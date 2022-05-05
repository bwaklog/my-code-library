import random
print("Smaller the better ;)")


alphabets = {
    'cons': 'b c d f g h j k l m n p q r s t v w x y z'.split(' '),
    'vovs': 'a e i o u'.split(' ')
}


# Start of function
def randomise(initLetter, deflen=7):
    pass


pref_init = str(input("""
Do you want a custom inital letter?
(y/n) : """)).lower()

if pref_init == "y":
    initLetter = input("Enter a initializing character : ")
else:
    # choose b/w {cons} or {vovs}
    # 50 % chance for vovs or cons
    choise_set = random.choice(['cons', 'vovs'])
    initLetter = random.choice(alphabets[choise_set])
    print(initLetter)
