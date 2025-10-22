# Program #1: Initals Maker, Griffin Corniea, 10/21/25

def initials_generator(personsName):
    personsInitials = ""


    names = personsName.split()


    for name in names:
        personsInitials += name[0].upper() + ". "

    return personsInitials.strip()


personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)