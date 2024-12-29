#EX2//:
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def affiche_Time(self):
        print("Heure : ", self.hour)
        print("Minute : ", self.minute)
        print("Seconde : ", self.second)
    
    def modifier(self, hour, minute, second):
        if hour > 24:
            print("Erreur : L'heure ne peut pas dépasser 24.")
        elif minute >= 60:
            print("Erreur : Les minutes ne peuvent pas dépasser 59.")
        elif second >= 60:
            print("Erreur : Les secondes ne peuvent pas dépasser 59.")
        else:
            self.hour = hour
            self.minute = minute
            self.second = second
t1 = Time(12, 30, 45)
t1.affiche_Time()
t1.modifier(25, 70, 80)
t1.affiche_Time()
