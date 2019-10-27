# Day 5 advent of code
# will take in some polyer chain
# types are different letters like 'r' and 's'
# polarity is represented by its case like 'r' and 'R' being opposite polarity
# oppoiste polarity annihilates

filename = 'day5_input.txt'
data = open(filename)
datain = data.read()
data.close()

partnum = int(input("which part number(1/2)?:"))

def charmap(let):
    chcd = ord(let)
    if chcd < 95:
        ans = chcd + 32
    else:
        ans = chcd - 32
    return chr(ans)

polist = list(datain)
done = 0
popamt = 0

# part 1
if partnum == 1:
    while done == 0:
        for e in range(len(polist)):
            if e == len(polist) - 1:
                done = 1
                break
            elif polist[e+1] == charmap(polist[e]):
                polist.pop(e)
                polist.pop(e)
                popamt += 2
                break

    print("The amount of entries left in the polymer is:",len(polist)-1)
elif partnum == 2:
    # start part 2 here
    # removing a and A from list 
    for ent in polist:
        if ent == 'a' or ent == 'A':
            polist.remove(ent)

    # Time to shrink the polymer
    while done == 0:
        for e in range(len(polist)):
            if e == len(polist) - 1:
                done = 1
                break
            elif polist[e+1] == charmap(polist[e]):
                polist.pop(e)
                polist.pop(e)
                popamt += 2
                break

    print("The amount of entries left in the polymer is:",len(polist)-1)
else:
    print("bad input buddy")

        
