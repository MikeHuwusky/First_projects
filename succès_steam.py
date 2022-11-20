from types import NoneType
import webbrowser
question = NoneType

while question not in ("y", "n"):
    question = input("Tu veux un succès Steam ? (y/n)")
    if question == "y":
        webbrowser.open('https://cdn.discordapp.com/attachments/885509189860999168/934189010358771732/1f3c6.png')
    elif question == "n":
        print("Dommage pour toi UwU")
    else:
        print("allez, je sais que tu en veux un~")