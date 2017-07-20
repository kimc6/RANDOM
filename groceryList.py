groceryList = ["pineapples", 7, True]
groceryList2 = ["chicken nuggets, chicken nuggets, chicken nuggets, chicken nuggets, chicken nuggets"]
#print (groceryList)
#print (groceryList2)

#LEVEL 1:
import random

lovelyNames = ['Macbook', 'Notebook', 'Koala', 'BankofAmerica', 'cactus', 'watermelon','kiwi', 'potato']

randomNum=random.randint(0,7)

print("Your new name is!:")
print(lovelyNames[randomNum])

#LEVEL 2:
Appetizers = ['knives', 'forks', 'sporks', 'spatulas', 'spoons']
Entree = ['soft-shelled turtle', 'grizzly bear', 'tarantula', 'potato man', 'Buzzlight']
Dessert = ['ice cream', 'gelato', 'cake', 'milkshake', 'ginger extract']

randomNum=random.randint(0,4)

print ("And your lunch is!: ")
print("Appetizers:")
print (Appetizers[randomNum])
print ("Entree:")
print(Entree[randomNum])
print ("Dessert")
print(Dessert[randomNum])

#LEVEL 3:
print ("And here comes the fortune cookie!: ")
five_syllables = ["I drew a dino", "Christi is lovely", "Netflix is my homie", "They had a great time", "Cups of tea are great","Potatoes are great", "Strawberries are sweet", "I enjoy reading", "You are beautiful", "Food is beautiful"]
seven_syllables = ["Pineapples are amazing", "I am a couch potato", "Chicken nuggets are yummy","I found out I'm a squirrel", "I am a mashed potato", "Watermelons hate me. Why", "Express yourself through art", "Girls Who Code is fun", "Aliens are nice beings", "You are a sweet koala"]
five_syllables2 = ["Being mean is gross", "you're a pretty poo.", "In conclusion, yum.", "" "rat a tat a tat.", "blah blah blah blah blah", "Rainbows are great", "Haikus are pure art.", "Despicably great", "Pom poms are funny", "A chicken nugget"]
randomNum=random.randint(0,9)
print(five_syllables[randomNum])
print(seven_syllables[randomNum])
print(five_syllables2[randomNum])
