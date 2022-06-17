import matplotlib.pyplot as plt #Matplotlib bliver importeret for at kunne visualisere de grafer der bliver dannet af dataen der bliver indsamlet under Session.
import pandas as pd #Ved at importere pandas kan pandas dataanalysesbibliotek benyttes til analysere dataen der bliver indsamlet under sessions.
import numpy as np #Numpy gør det muligt for at matematiske og logiske operationer på arrays kan udføres.

class Login: #Klassen Login er en "Parent klass", hvor brugernavn og password bliver definieret.
#Efter at brugeren har skabt et Brugernavn og Password i klassen Profil kan dette benyttes til at åbne sin egen konto på applikationen
#Når brugeren logger ind på Appen via Login klassen ser systemet hvis brugeren findes i databasen og hvis det passer, logger brugeren ind.
    def __init__(self, brugernavn, password):
        self.brugernavn = brugernavn
        self.password = password

    def Validbrugernavn():
    def Validpassword():

class Dashboard: #Klassen Dashboard visualiserer data via Login Klassen, der henter relevante hjernefrekvenser for at kunne visualisere disse
#og give brugeren et overblik over hvordan månedens målinger har været.
    def Createpivot():
        StressFaktor = ""
        Sundhed = ""
        DatoTid = ""
        MalingsID = ""
    def Matplotlib():
        MalingsID = ""
        DatoTid = ""
        Sundhed = ""
        StressFaktor = ""
    def CSVreader():

class Database: #I klassen Database bliver inputtet fra Profil gemt. Klassen Login trækker data fra databasen for at se, hvorvidt brugeren har oprettet en profil, da profilen vil være gemt i
#databasen efter registrering i klassen Profil. I klassen Database gemmes de forskellige målinger kunderne udfører efter logget ind via Login og tilgået Session.
    def __init__(self, malingsID, malinger, brugerID):
        self.malingsID = malingsID
        self.malinger = malinger
        self.brugerID = brugerID

    def lagrebrugerID():
    def lagremalingID():

class Profil: #Under klassen profil er det der hvor brugeren opretter sin profil med nedenstående attributer.
#Brugerens profil bliver gemt i databasen
    def __init__(self, BrugerID, Brugernavn, Password, Email, Alder, Kon):
        self.BrugerID = BrugerID
        self.Brugernavn = Brugernavn
        self.Password = Password
        self.Email = Email
        self.Alder = Alder
        self.Kon = Kon

    def Createbrugernavn():
    def Createpassword():
    def TypeBrugernavn():
    def TypeAlder():
    def TypeKon():
    def TypeEmail():

class Session: #I klassen Session bliver MålingsID og Målingerne registereret efter brug har målt sine hjernefrekvenser og sender det til databasen hvor det bliver gemt
#Sessions klassen tilgås via Login klassen, hvor brugeren logger ind med sit specifikke brugernavn og password, hvorefter brugeren kan udføre sine målinger via Session.
   def lagrebrugerID():
        malingsID = ""
        malinger = ""
   def lagremalingID():
        malingsID = ""
        malinger = ""
