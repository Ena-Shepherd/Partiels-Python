"""

 Author: Yannis STEFANELLI

 Creation Date: 07-03-2023 09:34:05

 Description :

"""

class Material:
    def __init__(self, type, serial):
        self.type = type
        self.serial = serial

class Clavier(Material):
    def __init__(self, type, serial, keynb):
        super().__init__(type, serial)
        self.keynb = keynb

class Ecran(Material):
    def __init__(self, type, serial, resolution):
        super().__init__(type, serial)
        self.resolution = resolution

class Pc(Material):
    def __init__(self, type, serial, ecran, clavier):
        super().__init__(type, serial)
        self.ecran = ecran
        self.clavier = clavier
        
    def sauvegarder(self, nom_fichier):
        with open(nom_fichier, "w") as f:
            f.write(f"Type: {self.type}\n")
            f.write(f"Serial: {self.serial}\n")
            f.write(f"Ecran type: {self.ecran.type}\n")
            f.write(f"Ecran serial: {self.ecran.serial}\n")
            f.write(f"Ecran resolution: {self.ecran.resolution}\n")
            f.write(f"Clavier type: {self.clavier.type}\n")
            f.write(f"Clavier serial: {self.clavier.serial}\n")
            f.write(f"Clavier keynb: {self.clavier.keynb}\n")
            
    def charger(self, nom_fichier):
        with open(nom_fichier, "r") as f:
            self.type = f.readline().split(": ")[1].rstrip("\n")
            self.serial = f.readline().split(": ")[1].rstrip("\n")
            ecran_type = f.readline().split(": ")[1].rstrip("\n")
            ecran_serial = f.readline().split(": ")[1].rstrip("\n")
            ecran_resolution = f.readline().split(": ")[1].rstrip("\n")
            clavier_type = f.readline().split(": ")[1].rstrip("\n")
            clavier_serial = f.readline().split(": ")[1].rstrip("\n")
            clavier_keynb = f.readline().split(": ")[1].rstrip("\n")
            self.ecran = Ecran(ecran_type, ecran_serial, ecran_resolution)
            self.clavier = Clavier(clavier_type, clavier_serial, int(clavier_keynb))

def exercice3():
    ecrantype = input("Type d'écran\n")
    ecranserial = input("Ecran nb série\n")
    res = input("Résolution ecran\n")

    claviertype = input("Type de clavier\n")
    clavierserial = input("Clavier nb série\n")
    nbtouches = input("Nb touches\n")

    ecran = Ecran(ecrantype, ecranserial, res)
    clavier = Clavier(claviertype, clavierserial, nbtouches)
    pc = Pc("Portable", "ABC123", ecran, clavier)

    pc.sauvegarder("config.txt")
    pc.charger("config.txt")

    with open('config.txt', 'r') as file:
        content = file.read()
    print(content)