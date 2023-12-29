#This was largely written by Lars to explain while loop concepts to me.
while(True):
    comfy = input('How comfy are you on a scale from 1 (uncomfy) to 10 (purrito)?')
    try:
        comfy = int(comfy)
        if comfy < 1 or comfy > 10:
            print("That's not a number between 1 and 10!")
            continue
    except:
        print("That's not a number!")
        continue
    break #This break applies when the "if" of the try section is not met, breaking the loop and continuing with the rest of the code.

cookies = 2

if comfy >= 5:
    print('Nice.')
else:
    answer= input("Have you tried cookies? (Y/N)")
    first_letter = answer.lower()[0]
    if first_letter == "y":
        comfy += cookies
        print(f"Aww, have {cookies} more and cheer up.")
    else: 
        print(f"Try {(5-comfy)*cookies} cookies!")