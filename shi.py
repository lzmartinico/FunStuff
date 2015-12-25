# Always form ship name when an overlap is found
# except when they both start or end in the same letter

# Onset Conservation: ship starts with the name that starts with more consonants

# TODO: quantify pronunciation difficulty and choose that

# TODO: avoid consonant + a sonorant + a vowel + the same sonorant

# TODO: check if word is somehow pronouncable (NLTK may help)

# TODO: input checking preprocessing

# TODO (in the far future): offer ranking, take into account votes and Brown existence

# TODO: ot3???

def addConditions(ship, first, second):
    return len(ship) > 3 and ship != first and ship != second

def ship(first, second):

    # a and b are numbered lists of the strings

    enA = enumerate(first)
    enB = enumerate(second)

    a = []
    b = []
    for i in enA:
        a.append(i)

    for i in enB:
        b.append(i)

    # count the number of vowels in the names

    vowels = ['a','e','i','o','u']
    countA = 0
    countB = 0

    for i in a:
        if i[1].lower() not in vowels:
            countA += 1
        else:
            break

    for i in b:
        if i[1].lower() not in vowels:
            countB += 1
        else:
            break

    #print countA
    #print countB

    # a should be the noun with greater offset

    if countB > countA:
        temp = a
        a = b
        b = temp
        temp = first
        first = second
        second = temp


    # find matchings

    ships = []

    for l in a:
        for m in b:
            notLimit = ((l[0] != 0 or m[0] !=0) and (l[0] != len(l)-1 or m[0] != len(m)-1))
            if l[1].lower() == m[1].lower() and notLimit:
                if countB == countA:
                    ship = first[0:l[0]] + second[m[0]:]
                    if addConditions(ship, first, second):
                        ships.append(ship)
                    ship = second[0:m[0]] + first[l[0]:]
                    if addConditions(ship, first, second):
                        ships.append(ship)
                else:
                    ship = first[0:l[0]] + second[m[0]:]
                    if addConditions(ship, first, second):
                        ships.append(ship)
                    else:
                        ship = second[0:m[0]] + first[l[0]:]
                        if addConditions(ship, first, second):
                            ships.append(ship)


    ships.sort(key = len, reverse = True)
    return ships
