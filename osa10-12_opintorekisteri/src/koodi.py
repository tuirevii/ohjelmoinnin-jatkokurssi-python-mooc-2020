# OPINTOREKISTERI:

# Tee interaktiivinen ohjelma, jonka avulla voit pitää kirjaa opintomenestyksestäsi. 
# Tyyli on vapaa, mutta nyt on hyvä tilaisuus harjoitella osan esimerkin kaltaisen 
# oliorakenteen muodostamista.

# Ohjelma toimii seuraavasti:
# Esimerkkitulostus

# 1 lisää suoritus
# 2 hae suoritus
# 3 tilastot
# 0 lopetus

# komento: 1
# kurssi: Ohpe
# arvosana: 3
# opintopisteet: 5

# komento: 2
# kurssi: Ohpe
# Ohpe (5 op) arvosana 3

# komento: 1
# kurssi: Ohpe
# arvosana: 5
# opintopisteet: 5

# komento: 2
# kurssi: Ohpe
# Ohpe (5 op) arvosana 5

# komento: 1
# kurssi: Ohpe
# arvosana: 1
# opintopisteet: 5

# komento: 2
# kurssi: Ohpe
# Ohpe (5 op) arvosana 5

# komento: 2
# kurssi: Java-ohjelmointi
# ei suoritusta

# komento: 1
# kurssi: Tira
# arvosana: 1
# opintopisteet: 10

# komento: 1
# kurssi: Tilpe
# arvosana: 2
# opintopisteet: 5

# komento: 1
# kurssi: Lapio
# arvosana: 4
# opintopisteet: 1

# komento: 1
# kurssi: Lama
# arvosana: 5
# opintopisteet: 8

# komento: 3
# suorituksia 5 kurssilta, yhteensä 29 opintopistettä
# keskiarvo 3.4
# arvosanajakauma
# 5: xx
# 4: x
# 3:
# 2: x
# 1: x

# komento: 0

# Muutama huomio: kultakin kursilta tallentuu ainoastaan yksi arvosana. Arvosanaa voi korottaa, mutta se ei voi laskea.

# Tehtävästä on tarjolla kaksi tehtäväpistettä. Ensimmäisen pisteen saa jos toiminnot 1 ja 2 sekä lopetus toimivat. 
# Toisen pisteen saa jos myös toiminto 3 on toteutettu.

class Kurssi:
    def __init__(self, nimi: str, arvosana: int, op: int):
        self.__nimi = nimi
        self.__arvosana = arvosana
        self.__op = op
    
    def nimi(self):
        return self.__nimi

    def arvosana(self):
        return self.__arvosana
        
    def op(self):
        return self.__op

class Opintorekisteri:
    def __init__(self):
        self.__suoritukset = {}
    
    def lisaa_suoritus(self, nimi: str, arvosana: int, op: int):
        if not nimi in self.__suoritukset:
            self.__suoritukset[nimi] = Kurssi(nimi, arvosana, op)
        elif self.__suoritukset[nimi].arvosana() < arvosana:
            self.__suoritukset[nimi] = Kurssi(nimi, arvosana, op)
        else:
            print("arvosana ei saa laskea")

    def hae_tiedot(self, kurssi: Kurssi):
        if not kurssi in self.__suoritukset:
            return None
        return self.__suoritukset[kurssi]

    def kaikki_tiedot(self):
        return self.__suoritukset
    

class OpintorekisteriSovellus:
    def __init__(self):
        self.__rekisteri = Opintorekisteri()

    def ohje(self):
        print("komennot: ")
        print("lisää suoritus")
        print("hae suoritus")
        print("tilastot")
        print("0 lopetus")

    def suorituksen_lisays(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        op = input("opintopisteet: ")
        self.__rekisteri.lisaa_suoritus(kurssi, arvosana, op)
    
    def haku(self):
        kurssi = input("kurssi: ")
        tiedot = self.__rekisteri.hae_tiedot(kurssi)
        if tiedot == None:
            print("ei suoritusta")
            return
        print(f"{tiedot.nimi()} ({tiedot.op()} op) arvosana {tiedot.arvosana()}")
    
    def kaikki_tiedot(self):
        opintopisteet = 0
        kurssimaara = 0
        ykkoset = ""
        kakkoset = ""
        kolmoset = ""
        neloset = ""
        vitoset = ""
        kurssit = self.__rekisteri.kaikki_tiedot()
        arvosanat_yht = 0
        for nimi, kurssi in kurssit.items():
            kurssimaara += 1
            arvosanat_yht += int(kurssi.arvosana())
            if kurssi.arvosana() == "1":
                ykkoset += "x"
            elif kurssi.arvosana() == "2":
                kakkoset += "x"
            elif kurssi.arvosana() == "3":
                kolmoset += "x"
            elif kurssi.arvosana() == "4":
                neloset += "x"
            elif kurssi.arvosana() == "5":
                vitoset += "x"
            opintopisteet += int(kurssi.op())
        print(f"suorituksia {kurssimaara} kurssilta, yhteensä {opintopisteet} opintopistettä")
        keskiarvo = round(arvosanat_yht / kurssimaara, 1)
        print(f"keskiarvo {keskiarvo}")
        print("arvosanajakauma")
        print(f"5: {vitoset}")
        print(f"4: {neloset}")
        print(f"3: {kolmoset}")
        print(f"2: {kakkoset}")
        print(f"1: {ykkoset}")

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.kaikki_tiedot()
            else:
                self.ohje()


sovellus = OpintorekisteriSovellus()
sovellus.suorita()

