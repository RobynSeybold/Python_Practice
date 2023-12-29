#This was written entirely by myself. 
comfy = input('How comfy are you on a scale from 1 (uncomfy) to 10 (purrito)?')
try:
    comfy = int(comfy)
except:
    print( "Please enter a number between 1 and 10 next time.")
    quit() #This is clunky because it never displays the error message and instead just closes the program.
cookies = 2

if comfy >= 5:
    print('Nice.')
else:
    answer= input("Have you tried cookies? (Y/N)")
    first_letter = answer.lower()[0]
    if first_letter == "y":
        comfy += cookies
        if comfy >= 5:
            print("Here, have some chocolate.")
        else:
            print("I'm sorry. I hope your day gets comfier soon.")
    else: 
        print("Time for a nap!")