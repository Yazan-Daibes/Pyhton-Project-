class Student:
    __participation=0
    #__TotalDuration = 0

    def __init__(self, name,id,totalDuration):
        self.__name = name
        self.__id = id
        self.__totalDuration = totalDuration
        self.__attending= []
        self.__participationList =[]


    def getName(self):
        return self.__name

    def setName(self, Name):
        self.__Name = Name

    def getId(self):
      return self.__id

    def setId(self, id):
            self.__id = id

    def getAttending(self):
        return self.__attending

    def setAttending(self,attends):
         self.__attending.append(attends)

    def getParticipation(self):
        return self.__participation

    def setParticipation(self,participate):
         self.__participation = participate

    def getParticipationList(self):
        return self.__participationList

    def setParticipationList(self,participateLIST):
         self.__participationList.append(participateLIST)

    def setId(self, id):
        self.__id = id

    def gettotalDuration(self):
        return self.__totalDuration

    def settotalDuration(self, attendance):
        self.attendance = attendance

    def getDidParticipate(self):
        return self.__didParticipate

    def setDidParticpate(self, didParticipate):
        self.__didParticipate = didParticipate

    def __markAttendance(self):
        raise NotImplementedError("Subclass must implement this method")


