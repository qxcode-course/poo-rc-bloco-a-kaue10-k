import sys

class Animal:
    def __init__(self, species: str = "", sound: str = ""):
        self.species = species
        self.sound = sound
        self.age = 0

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int):
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound

def main():
    animal = Animal("", "")
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if line == "":
            continue

        # Eco do comando
        print(f"${line}")

        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break

        elif cmd == "init":
            if len(parts) >= 3:
                species = parts[1]
                sound = parts[2]
                animal = Animal(species, sound)

        elif cmd == "show":
            print(animal)

        elif cmd == "grow":
            if len(parts) >= 2:
                inc = int(parts[1])
                animal.ageBy(inc)

        elif cmd == "noise":
            print(animal.makeSound())

        else:
            print("fail: comando invalido")

if __name__ == "__main__":
    main()