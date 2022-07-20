# change vowels --> a e i o u --> z

def translate(str):

    translation = ""

    for letter in str:

        if letter.lower() in "aeiou":

            if letter.isupper():
                translation = translation + "Z"

            else:
                translation = translation + "z"

        else:
            translation = translation + letter

    return translation

output = translate(input("enter a phrase: "))
print(output)
