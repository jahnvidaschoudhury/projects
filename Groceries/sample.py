print ("Hello! I am a robot that counts your purcheses! Just give me the date and what you have bought. ")
print ("Fist go through the setting then we can get started!") 
name = input ("What is your name? ") 
print ("hello "+ name)

your_answer = input ( " What are your favorite store(s)? ")

fh = open("myfile.txt" , "a")
fh.write(your_answer)
fh.close()
print(name + " Your favorite store(s) are sucessfully saved in my file! From now on type in 'i' and you will see your favorite store(s).")

Costly_stores = input ("Which store in you place is very expensive?" )

fh = open("Expensive_storessss" , "a")
fh.write(Costly_stores)
fh.close()
print(name + " Your expensive store(s) are sucessfully saved in my file! From now on type in 'e' and you will see your expensive store(s).")

cheap_stores = input ("What are your cheap stores in your aaarea?" )

fh = open("Cheap_stores" , "a")
fh.write(cheap_stores)
fh.close()
print(name + " Your cheap stores are sucessfully saved in my file! From now on type in 'c' and you will see your cheap stores.")


What_to_do = input ("What would you like to do? (press 'i' to seefavorite stores, press 'e' to see expensive stores ")



# if input.upper() == 'i':
#      fh = open("myfile.txt" , "r")
#      print(fh.readlines())

# if input.upper() == 'e':
#      fh = open("Expensive_stores" , "r")
#      print(fh.readlines())

# if input.upper() == 'c':
#      fh = open("Expensive_stores" , "r")
#      print(fh.readlines())