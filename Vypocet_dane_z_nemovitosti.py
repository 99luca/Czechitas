# Vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. 
# Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

import math
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. 
# Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).

class Property:
    def __init__(self, locality):
        self.locality = locality

# Vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
# Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). 

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

# Přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo 
# (pro zaokrouhlení použij funkci ceil() z modulu math).
# Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. 
#  U atributu estate_type následující hodnoty a koeficienty:
# - land (zemědělský pozemek) má koeficient 0.85.
# - building site (stavební pozemek) má koeficient 9.
# - forrest (les) má koeficient 0.35,
# - garden (zahrada) má koeficient 2. 

    def calculate_tax(self):
        if self.estate_type == "land":
            return math.ceil(self.area * 0.85 * self.locality.locality_coefficient)
        if self.estate_type == "building site":
            return math.ceil(self.area * 9 * self.locality.locality_coefficient)
        if self.estate_type == "forrest":
            return math.ceil(self.area * 0.35 * self.locality.locality_coefficient)
        if self.estate_type == "garden":
            return math.ceil(self.area * 2 * self.locality.locality_coefficient)
        else:
            return {f"Typ pozemku {self.estate_type} není definován."}
        
#Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.

lokalita = Locality("Ujezdec", 2)
lesni_pozemek = Estate(lokalita, "forrest", 500)

print(f"Daň z pozemku je {lesni_pozemek.calculate_tax()} Kč.")

# Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. 
# Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). 

class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

# přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. 
# Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.
    
    def calculate_tax(self):
        if self.commercial == True:
            return math.ceil(self.area * self.locality.locality_coefficient * 15 * 2)
        else:
            return math.ceil(self.area * self.locality.locality_coefficient * 15)
        
# Například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. 
# Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.
        
lokalita_bytu = Locality("Zlín", 3)
byt = Residence(lokalita_bytu, 60)

print(f"Daň z bytu je {byt.calculate_tax()} Kč.")

Lokalita_bytu_k_podnikani = Locality("Zlín", 3)
byt_k_podnikani = Residence(Lokalita_bytu_k_podnikani, 60, commercial=True)

print(f"Daň z bytu k podnikání je {byt_k_podnikani.calculate_tax()} Kč.")

# Vyzkoušej svůj program pomocí následujících nemovitostí:

# - Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
lokalita_zemedelskeho_pomezemku = Locality("Manětín", 0.8)
zemedelsky_pozemek = Estate(lokalita_zemedelskeho_pomezemku, "land", 900)

print(f"Daň pro zemědělský pozemek je {zemedelsky_pozemek.calculate_tax()} Kč.")

# - Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
lokalita_domu = Locality("Manětín", 0.8)
dum = Residence(lokalita_domu, 120)

print(f"Daň z domu je {dum.calculate_tax()} Kč.")

# - Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
lokalita_kancelare = Locality("Brno", 3)
kancelar = Residence(lokalita_kancelare, 90, commercial=True)

print(f"Daň z kanceláře je {kancelar.calculate_tax()} Kč.")
