inputTest = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
road ='A-D-C-D'
inputTwoPointsTrip='A-C'


class TrainExercise:
    """blabla"""
    def __init__(self, inputTest):
        self.inputTest = inputTest        
        #self.parseinput = ''
        self.dico = {}

    def parseInput(self):
        self.parseinput = self.inputTest.split(", ")

        for distanceInput in self.parseinput:
            if not distanceInput[0] in self.dico:
                self.dico[distanceInput[0]] = { distanceInput[1]: distanceInput[2:]}
            else:
                self.dico[distanceInput[0]][distanceInput[1]] = distanceInput[2:]
        
        print(self.dico)
        nbrOfSubDico=0
        for key in self.dico:
            nbrOfSubDico+= len(self.dico[key])
            print(nbrOfSubDico)
        self.maxtest= len(self.dico)*nbrOfSubDico
        



    def parseRoad(self, road):
        self.road = road
        self.distTotal=0
        error= False
        self.parseroad= self.road.split('-')
        print(self.parseroad)

        for i in range(len(self.parseroad)-1):
            try:
                self.distTotal += int(self.dico[self.parseroad[i]][self.parseroad[i+1]])
            except KeyError:
                print("NO SUCH ROUTE")
                error = True

        if not error == True:
            print(self.distTotal)
            return self.distTotal


    def numberOfTrip(self, inputTwoPointsTrip, maxStep):
        self.maxStep = maxStep
        self.inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = self.inputTwoPointsTrip[0], self.inputTwoPointsTrip[1]
        liste = [start]
        temporary_liste = []

        for i in range(maxStep):
            if i==0:
                for key in self.dico[start]:
                    j=0
                    if j != len(self.dico):
                        temporary_liste.append(liste[i] + key)
                        j+=1
                liste = temporary_liste
                temporary_liste=[]
            else:
                for keyliste in liste:
                    for key in self.dico[keyliste[-1]]:
                        temporary_liste.append(keyliste + key)                        
                liste = temporary_liste
                temporary_liste=[]
        print(liste)

        
        liste_result=[]
        for results in liste:
            
            if end in results[1:]:
                car=""
                k=0
                for j in results:
                    
                    if k==0:
                        car = j
                        k+=1
                    elif not j == end:
                        car+=j                        
                        k+=1                       
                    else:
                        car+=j
                        break
                resultattts= car          
                if not resultattts in liste_result:
                    liste_result.append(resultattts)
        print(liste_result)
        self.finalresult=len(liste_result)
        print(self.finalresult)

    def numberOfTripWithMaxStep(self, inputTwoPointsTrip, NumberStep):
        self.inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = self.inputTwoPointsTrip[0], self.inputTwoPointsTrip[1]
        liste = [start]
        temporary_liste = []
        for i in range(NumberStep):
            if i==0:
                for key in self.dico[start]:
                    j=0
                    if j != len(self.dico):
                        temporary_liste.append(liste[i] + key)
                        j+=1
                liste = temporary_liste
                temporary_liste=[]
            else:
                for keyliste in liste:
                    for key in self.dico[keyliste[-1]]:
                        temporary_liste.append(keyliste + key)                        
                liste = temporary_liste
                temporary_liste=[]         
        liste_result=[]

        for results in liste:
            if results.endswith(end):
                liste_result.append(results)
        self.numberOfTripWithMaxStep=len(liste_result)
        print(self.numberOfTripWithMaxStep)

    def shorterRoute(self, inputTwoPointsTrip):
        self.inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = self.inputTwoPointsTrip[0], self.inputTwoPointsTrip[1]
        liste = [start]
        temporary_liste = []
        Finboucle = False
        Finboucle2=0
        print("sm " + str(self.maxtest))
        i=0

        while Finboucle == False and Finboucle2 != self.maxtest:
            
            if i==0:
                for key in self.dico[start]:
                    j=0
                    if j != len(self.dico):
                        temporary_liste.append(liste[i] + key)
                        j+=1
                liste = temporary_liste
                temporary_liste=[]
                i=1
            else:
                #print(liste)
                for keyliste in liste:
                    for key in self.dico[keyliste[-1]]:
                        if not keyliste[-1] == end:
                            temporary_liste.append(keyliste + key)
                        elif keyliste in temporary_liste:
                            pass
                        else:
                            temporary_liste.append(keyliste)
                if temporary_liste == liste:
                    Finboucle=True
                    print("finfin")
                liste = temporary_liste
                temporary_liste=[]
            Finboucle2+=1
            print(Finboucle2)
        dicoDeparse=[]
        for cities in liste:
            TempVal=""
            for city in cities[:-1]:
                print(city)
                TempVal+= str(city) + "-"
            TempVal+= str(cities[-1])            
            dicoDeparse.append(TempVal)
        listeDistance=[]
        for test in dicoDeparse:
            bla=self.parseRoad(test)
            listeDistance.append(bla)
        print(min(listeDistance))


                
             
        



       
    
map = TrainExercise(inputTest)
map.parseInput()
map.parseRoad(road)
#map.numberOfTrip(inputTwoPointsTrip, 4)
#map.numberOfTripWithMaxStep(inputTwoPointsTrip, 4)
map.shorterRoute("B-B")