



class TrainExercise:
    """blabla"""
    def __init__(self, inputTest):
        self.inputTest = inputTest
        self.graphRoads = {}


    def parseInput(self):
        parseinput = self.inputTest.split(", ")
        for distanceInput in parseinput:
            if not distanceInput[0] in self.graphRoads:
                self.graphRoads[distanceInput[0]] = { distanceInput[1]: distanceInput[2:]}
            else:
                self.graphRoads[distanceInput[0]][distanceInput[1]] = distanceInput[2:]
        
        nbrOfSubgraphRoads=0
        for key in self.graphRoads:
            nbrOfSubgraphRoads+= len(self.graphRoads[key])
        self.maxtest= len(self.graphRoads)*nbrOfSubgraphRoads


    def distanceBetweenCities(self, road):
        distTotal=0
        parseroad= road.split('-')
        if parseroad[0] == road:
            parseroad = list(road)
        try:
            for i in range(len(parseroad)-1):
                distTotal += int(self.graphRoads[parseroad[i]][parseroad[i+1]])
        except KeyError:
                distTotal="NO SUCH ROUTE"
        return distTotal


    def numberOfTrip(self, inputTwoPointsTrip, maxStop):
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        listOfRoad = [start]
        temporary_liste = []

        for i in range(maxStop):
            if i==0:
                for key in self.graphRoads[start]:
                    listOfRoad.append(listOfRoad[i] + key)
            else:
                for keyliste in listOfRoad:
                    for key in self.graphRoads[keyliste[-1]]:
                        temporary_liste.append(keyliste + key)                        
                listOfRoad = temporary_liste
                temporary_liste=[]
        
        finalListe=[]
        for results in listOfRoad:
            
            if end in results[1:]:
                temporaryRoad=""
                k=0 #The k incremetation avoid to stop the test if start==end
                for city in results:                    
                    if k==0 or city != end:
                        temporaryRoad+=city                        
                        k+=1                       
                    else:
                        temporaryRoad+=city
                        break         
                if not temporaryRoad in finalListe:
                    finalListe.append(temporaryRoad)
        return len(finalListe)

    def numberOfTripWithMaxStep(self, inputTwoPointsTrip, stopNumber):
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        listOfRoad = [start]
        temporary_liste = []
        for i in range(stopNumber):
            if i==0:
                for city in self.graphRoads[start]:
                    listOfRoad.append(listOfRoad[i] + city)
            else:
                for roadInProgress in listOfRoad:
                    for city in self.graphRoads[roadInProgress[-1]]:
                        temporary_liste.append(roadInProgress + city)                        
                listOfRoad = temporary_liste
                temporary_liste=[]         
        finalRoadsList=[]

        for results in listOfRoad:
            if results.endswith(end) and len(results)==stopNumber +1:
                finalRoadsList.append(results)
        return len(finalRoadsList)

    def shorterRoute(self, inputTwoPointsTrip):
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        liste = [start]
        temporary_liste = []
        Finboucle = False
        Finboucle2=0
        i=0

        while Finboucle == False and Finboucle2 != self.maxtest:
            
            if i==0:
                for city in self.graphRoads[start]:
                    temporary_liste.append(liste[i] + city)
                liste = temporary_liste
                temporary_liste=[]
                i=1
            else:
                for roads in liste:
                    for city in self.graphRoads[roads[-1]]:
                        if not roads[-1] == end:
                            temporary_liste.append(roads + city)
                        elif roads in temporary_liste:
                            pass
                        else:
                            temporary_liste.append(roads)
                if temporary_liste == liste:
                    Finboucle=True
                liste = temporary_liste
                temporary_liste=[]
            Finboucle2+=1

        listeDistance=[]
        for road in liste:
            listeDistance.append(self.distanceBetweenCities(road))
        return min(listeDistance)


    def numberOfPossibleRoad(self, inputTwoPointsTrip, lengthLimit):
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        liste = [start]
        temporary_liste = []
        Finboucle = 0
        finalList=[]
        i=0

        while Finboucle != lengthLimit:            
            if i==0:
                for city in self.graphRoads[start]:
                    temporary_liste.append(liste[i] + city)
                liste = temporary_liste
                temporary_liste=[]
                i=1
            else:
                for roads in liste:
                    for city in self.graphRoads[roads[-1]]:
                        temporary_liste.append(roads + city)
                        if roads[-1] == end:
                            finalList.append(roads)
                liste = temporary_liste
                temporary_liste=[]
            Finboucle+=1
        roadsPreparation=[]
        for cities in list(set(finalList)):        
            roadsPreparation.append(cities)
        listeDistance=[]
        for road in roadsPreparation:
            roadDistance= self.distanceBetweenCities(road)
            if roadDistance < lengthLimit:
                listeDistance.append(roadDistance)
        return len(listeDistance)

"""
inputTest = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
road="A-B-C"
map = TrainExercise(inputTest)
map.parseInput()
print(map.distanceBetweenCities(road))
road2 ="AD"

road3= "A-D-C"
road4= "A-E-B-C-D"
road5= "A-E-D"
print(map.distanceBetweenCities(road2))
print(map.distanceBetweenCities(road3))
print(map.distanceBetweenCities(road4))
print(map.distanceBetweenCities(road5))
print(map.numberOfTrip("C-C", 3))
print(map.numberOfTripWithMaxStep("A-C", 4))
print(map.shorterRoute("A-C"))
print(map.shorterRoute("B-B"))

print(map.numberOfPossibleRoad("C-C", 30))
"""