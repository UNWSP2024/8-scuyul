# Program #2: Word spreader, Griffin Corniea, 10/21/25

def word_separator(sentence):
    new_sentence = ""

    for i in range(len(sentence)):
        letter = sentence[i]


        if letter.isupper() and i != 0:

            new_sentence += " " + letter.lower()

        else:
            new_sentence += letter


    new_sentence += "."

    return new_sentence



sentence = input("Enter a sentence in cammel case: ")
print(word_separator(sentence))