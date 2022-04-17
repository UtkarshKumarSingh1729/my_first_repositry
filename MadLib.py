## string concatenation (aka how to put strings togrther)
## suppose we want to create a string that says "subscribe to___ abcd"
#youtuber="Iron man"
#print("subscribe to "+youtuber)
#print("subscrbe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")
adj=input("Adjective: ")
verb1=input("verb1: ")
verb2=input("verb2: ")
famous_person= input("famous person: ")
madlib=f"computer programing is so {adj}! It makes me so excited all the time because \
I love to {verb1}, stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)