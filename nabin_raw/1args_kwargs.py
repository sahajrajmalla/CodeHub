def mainargs(normal, *argsdata, **kwargs):
    print(normal)
    for names in argsdata:
        print(names)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


names = ["Nabin", "World", "fire", "burn"]
work = {"Nabin": "Coder", "World": "place for living",
        "fire": "Burns which comes near"}
mainargs(*names, **work)