import random
import time
import dicts

def getActionName():
    nr = random.randrange(0,3)
    if nr == 0:
        return "Normal"
    elif nr == 1:
        return "Summon"
    else:
        return "ChaseAway"


def addPersonNotActedBefore(current, hasActed):
    alll = current + hasActed

    if "Dumpe" not in alll:
        current.append("Dumpe")
        print("Dumpe kommer flyvende med sine blafrende ører.\n")

    elif "Gnavpot" not in alll:
        current.append("Gnavpot")
        print("Gnavpot trisser hen for at se om de andre laver ballade! O.o\n")
    elif "Søvnig" not in alll:
        current.append("Søvnig")
        print("Søvnig går i søvne. Han vågner og kigger ind i ansigtet på en af sine yndlings venner.\n")
    elif "Prosit" not in alll:
        current.append("Prosit")
        print("ATJUUUHHH heeej!!! råber Prosit og joiner det han tror er en fest. :D\n")


def act(names, queue, current, hasActed, index, nrRemoved):
    curIndex = index - nrRemoved

    if len(current) - 1 < curIndex:
        addPersonNotActedBefore(current, hasActed)

    print(current)
    name = current[curIndex]
    person = dicts.people[name]
    if index == 3:
        print(person["Last"])
        time.sleep(3)
    else:
        act = getActionName()

        msg, otherPerson = person[act]

        if act == "Summon":
            if (otherPerson in current) or (otherPerson in hasActed):
                act = "ChaseAway"
                msg, otherPerson = person[act]
            else:
                current.append(otherPerson)
        if act == "ChaseAway":
            if not(otherPerson in current):
                act = "Normal"
                msg, otherPerson = person[act]
            else:
                current.remove(otherPerson)
                nrRemoved += 1

        print(msg)
        time.sleep(3)
        hasActed.append(name)
        return nrRemoved


def story():
    # Make the people ready for the story
    queue = dicts.allPeople
    random.shuffle(queue)
    names = []
    for person in queue:
        names.append(person["Name"])
    current = names[:2]

    nrRemoved = 0
    hasActed = []
    for nr in range(4):
        nrRemoved = act(names, queue, current, hasActed, nr, nrRemoved)

story()


