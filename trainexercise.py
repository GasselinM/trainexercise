class TrainExercise:
    """Class to calculate distance or to deteminate all combinaison between routes
    The algorithm takes a first input: the roads with their distance.
    The input looks likes this pattern: AB5, BC4, CD8, DC10"""
    def __init__(self, inputTest):
        self.inputTest = inputTest
        self.graphRoads = {}


    def parseInput(self):
        """Convert the input into dictionnary"""
        parseinput = self.inputTest.split(", ")
        for distanceInput in parseinput:
            if not distanceInput[0] in self.graphRoads: #If the key doesn't exist, it creates it 
                self.graphRoads[distanceInput[0]] = { distanceInput[1]: distanceInput[2:] }
            else:
                self.graphRoads[distanceInput[0]][distanceInput[1]] = distanceInput[2:]


    def distanceBetweenCities(self, road):
        """Method to calculate distance of a road:
        the expected input looks like : "A-B" or "A-B-C-E" or "ABC" """
        distTotal = 0
        parseroad = road.split('-')#Convert the pattern "A-B..." into a list

        if parseroad[0] == road:  #Convert the pattern "AB..." into a list
            parseroad = list(road)
        try:
            for i in range(len(parseroad)-1):
                distTotal += int(self.graphRoads[parseroad[i]][parseroad[i+1]])
                #Increment the distotal with the distance between two cities
        except KeyError:
                distTotal = "NO SUCH ROUTE"
                #If the road between 2 cities doesn't exist, return NO SUCH ROUTE
        return distTotal


    def numberOfTrip(self, inputTwoPointsTrip, maxStop):
        """Method to calculate The number of trips between two cities with a maximum of stop
        The first input expected is the two cities: "AB" or "AA" or "A-B" 
        The second input expected is an integer for the maximum of stop"""
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1] #City of begining and ending
        listOfRoad = [start] #List of possible routes
        temporary_list = []

        for i in range(maxStop):
            if i == 0 :
                for key in self.graphRoads[start]:
                    listOfRoad.append(listOfRoad[i] + key)
                    #For the first stop, it appends all the routes possible starting with the start city
            else:
                for keylist in listOfRoad:
                    for key in self.graphRoads[keylist[-1]]:
                        temporary_list.append(keylist + key)
                listOfRoad = temporary_list #We throw roads under construction
                temporary_list = []        
        finalList = []

        for results in listOfRoad:
            if end in results[1:]: #If the ending city is on the road except for the first position
                temporaryRoad= ""
                k = 0 #The k incremetation avoid to stop the test if start==end
                for city in results:
                    if k == 0 or city != end:
                        temporaryRoad += city
                        k += 1
                    else:
                        temporaryRoad += city
                        break
                if not temporaryRoad in finalList: #delete duplicate
                    finalList.append(temporaryRoad)
        return len(finalList)

    def numberOfTripWithMaxStep(self, inputTwoPointsTrip, stopNumber):
        """Method to calculate The number of trips between two cities with a fixed number of stop
        The first input expected is the two cities: "AB" or "AA" or "A-B" 
        The second input expected is an integer for the maximum of stop"""
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        listOfRoad = [start]
        temporary_list = []
        #Same method than precedent
        for i in range(stopNumber):
            if i == 0 :
                for city in self.graphRoads[start]:
                    listOfRoad.append(listOfRoad[i] + city)
            else:
                for roadInProgress in listOfRoad:
                    for city in self.graphRoads[roadInProgress[-1]]:
                        temporary_list.append(roadInProgress + city)
                listOfRoad = temporary_list
                temporary_list = []
        finalRoadsList = []

        for results in listOfRoad:
            if results.endswith(end) and len(results) == stopNumber +1:
                finalRoadsList.append(results)
                #Keep only roads with expected ending and whith good number of stop(s)
        return len(finalRoadsList)

    def shortestRoute(self, inputTwoPointsTrip):
        """Method to calculate the shortest distance between two points:
        The first input expected is the two cities: "AB" or "AA" or "A-B" """

        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        mylist = [start]
        temporary_list = []
        Finboucle = False
        minlist, minlist2 = 0, 0
        i = 0
        #Same method than precedent with an end loop when the shorter route is the same between two loops

        while Finboucle == False:
            if i == 0:
                for city in self.graphRoads[start]:
                    temporary_list.append(mylist[i] + city)
                mylist = temporary_list
                temporary_list = []
                i = 1
            else:
                for roads in mylist:
                    for city in self.graphRoads[roads[-1]]:
                        if not roads[-1] == end: #If the road stop with end, it adds the road only once and does not continue the road construction
                            temporary_list.append(roads + city)
                        elif roads in temporary_list:
                            pass
                        else:
                            temporary_list.append(roads)
                mylist = temporary_list
                temporary_list = []
                distancelist = []

                for roads in mylist:
                    distancelist.append(self.distanceBetweenCities(roads))
                minlist = min(distancelist)
                if minlist == minlist2: #End the loop if the shortest distance is the same than the precedent loop
                    Finboucle = True
                    return minlist
                else:
                    minlist2 = minlist


    def numberOfPossibleRoad(self, inputTwoPointsTrip, lengthLimit):
        """The number of different routes between two cities with a maximum distance.
        The first input expected is the two cities: "AB" or "AA" or "A-B" 
        The second input expected is an integer for the maximum of stop"""
        inputTwoPointsTrip = inputTwoPointsTrip.split('-')
        start, end = inputTwoPointsTrip[0], inputTwoPointsTrip[1]
        mylist = [start]
        temporary_list = []
        Finboucle = False
        finalList =[]
        i = 0
        #Same strategy than precedent with an end loop when all the routes under construction are higher than lengthLimit

        while Finboucle == False:
            if i == 0:
                for city in self.graphRoads[start]:
                    temporary_list.append(mylist[i] + city)
                mylist = temporary_list
                temporary_list = []
                i = 1
            else:
                for roads in mylist:
                    for city in self.graphRoads[roads[-1]]:
                        temporary_list.append(roads + city)
                        if roads[-1] == end and self.distanceBetweenCities(roads) < 30:
                            finalList.append(roads) #if roads satisfied criteria, appends it into the finallist
                distancelist = []
                
                for roads in temporary_list:
                    distancelist.append(self.distanceBetweenCities(roads)) #list of the distance of roads under construction
                Finboucle = all(i >= 30 for i in distancelist) #if all the distance are higher than 30, Finboucle = True
                mylist = temporary_list
                temporary_list = []
        return len(set(finalList))

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
print(map.shortestRoute("A-C"))
print(map.shortestRoute("B-B"))

print(map.numberOfPossibleRoad("C-C", 30))"""