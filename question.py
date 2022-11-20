question = None

while question not in ("y", "n"):
    question = input("est-ce que tu es cute ? (y/n)")
    if question == "y":
        print("ouiiiiiiii!!!!")
    elif question == "n":
        print("menteur va!")
    else:
        print("repond a la question!")