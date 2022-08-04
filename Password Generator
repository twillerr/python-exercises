words = ['religion', 'tidy', 'rabid', 'reset', 'rigid','peace', 'son', 'art',
         'clocks', 'flowers', 'blood', 'smile', 'sticks', 'chicken', 'hairy',
         'oranges', 'bait', 'action', 'convey', 'spray', 'expect', 'treat', 'sip',
         'shun', 'wave', 'bid', 'vanish', 'point', 'enter']

chars = ["a","b","c","d","e","f","g","h","i","j",
         "k","l","m","n","o","p","q","r","s","t","u",
         "v","w","x","y","z","A","B","C","D","E","F","G",
         "H","I","J","K","L","M","N","O","P","Q","R","S",
         "T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",
         "!","£","$","%","&","#","_","?"]

import random

while True:
    query = input("Would you like a new password? yes/no. ")
    if query == "no":
        print("Closing.")
        break
    
    elif query == "yes":
        query2 = input("Would you like a strong or weak password? strong/weak. ")
        if query2 == "weak":
            print("Your new password is: " + random.choice(words) + random.choice(words))

        elif query2 == "strong":
            query3 = int(input("How many characters? "))
            i=0
            pas = []

            while i < query3:
                pas.append(random.choice(chars))
                i+=1
            print("Your new password is: "+"".join(pas))
        
