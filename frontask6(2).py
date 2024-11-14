# Υπολογισμός Ημερομηνίας Πάσχα

# Η ημερομηνία της Κυριακής του Ορθόδοξου Πάσχα είναι 3 Απριλίου + p ημέρες, όπου το p εξαρτάται από το έτος και υπολογίζεται από την εξής διαδικασία:
#     p = v1+v2
#     v1 = (6*v2+m4+m2) mod 7
#     v2 = (16+m19) mod 30
#     m2 = 2*(ΕΤΟΣ mod 4)
#     m4 = 4*(ΕΤΟΣ mod 7)
#     m19 = 19*(ΕΤΟΣ mod 19)
# Με (x mod y) συμβολίζεται το υπόλοιπο της ακέραιας διαίρεσης x/y. Με βάση τα παραπάνω, γράψτε πρόγραμμα σε Python που θα υπολογίζει την ημερομηνία του Πάσχα για οποιοδήποτε έτος.

def century(century):
        L = []
        for i in range((century-1)*100, century*100): L.append(i)
        return L
           
class date:
    def __init__(date, day, month, year):
         date.day = day
         date.month = month
         date.year = year

class easter:
    def easterDay(year):
        p = ((6*((16+(19*(year%19)))%30)+(4*(year%7))+(2*(year%4)))%7) + ((16+(19*(year%19)))%30)

        if p < 29: easterDate = date(3+p, "april", year)
        else: easterDate = date(3+p-30, "may", year)
        return easterDate.day, easterDate.month, easterDate.year
    
    def earliestEaster(centuryInput):
        yearList = century(centuryInput)
        L = [100,100,100]
        for u in yearList:
            temp = easter.easterDay(u)
            if temp[1] != 'may' and temp[0] < L[-2]: 
                L.append(temp[0])
                L.append(temp[2])
        return L
    
    def latestEaster(centuryInput):
        yearList = century(centuryInput)
        L = [0, 0, 0]
        for u in yearList:
            temp = easter.easterDay(u)
            if temp[1] != 'april' and temp[0] > L[-2]: 
                L.append(temp[0])
                L.append(temp[2])
        return L
    
    def easterDayNotYear(year):
        p = ((6*((16+(19*(year%19)))%30)+(4*(year%7))+(2*(year%4)))%7) + ((16+(19*(year%19)))%30)

        if p < 29: easterDate = date(3+p, "april", "notImportant")
        else: easterDate = date(3+p-30, "may", "notImportant")
        return easterDate.day, easterDate.month
    
    def commonestEaster(centuryInput1, centuryInput2):
        yearList = century(centuryInput1) + century(centuryInput2)
        L = []
        for u in yearList: L.append(easter.easterDayNotYear(u))
        return max(set(L), key=L.count)
        

     
    

while True:
    userInput = input(">>")
    userInput = userInput.split()
    if userInput[0] == "easter" and len(userInput) < 3:
        try: print(easter.easterDay(int(userInput[1])))
        except: 
            try:print(f"'{userInput[1]}' is not a valid year.") 
            except: print("Usage: easter [year]")
    elif userInput[0] == "easter" and userInput[1] == "earliest" and len(userInput) == 3:
        try: print(f"april {easter.earliestEaster(int(userInput[2]))[-2]} {easter.earliestEaster(int(userInput[2]))[-1]}")
        except: print("Usage: easter earliest [century]")
    elif userInput[0] == "easter" and userInput[1] == "latest" and len(userInput) == 3:
        try: print(f"may {easter.latestEaster(int(userInput[2]))[-2]} {easter.latestEaster(int(userInput[2]))[-1]}")
        except: print("Usage: easter latest [century]")
    elif userInput[0] == "help" and len(userInput) == 1:
        print("easter [year] :  find the date of easter in the specified year\neaster earliest [century] :  find the earliest easter of the scpecified century\neaster latest [century] :  find the latest easter date of the specified century \neaster prevalent [century] :  find the most common easter date of the two centuries specified\nexit :  exit the program")
    elif userInput[0] == "easter" and userInput[1] == "prevalent" and len(userInput) == 4:
        try: print(easter.commonestEaster(int(userInput[2]), int(userInput[3])))
        except: print("Usage: easter prevalent [century1] [century2]")
    elif userInput[0] == "exit": break
    else: print("Unknown command. Type 'help' for help.")




