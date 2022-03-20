from optparse import OptionParser
import re
from pip._vendor.msgpack.fallback import xrange
import AbstractStudent
import os
import csv

# generate Class Attendance Sheet
def ClassAttendanceSheet(AllFilesNames,outPutDirectory):
    parentDirectory = outPutDirectory
    try:
        os.mkdir(path)
    except OSError as e:
        pass
    listNameandIDandDates = []
    listNameandIDandDates.append("Student Name")
    listNameandIDandDates.append("Student ID")
    count = 0
    # to know how many file we have
    for i in AllFilesNames:
        count = count+1
    # creating nested list of size length and count, the count is for the attendance sheet
    listForStudents = [[] for _ in xrange(length)]

    for line in range(1,length):
        listForStudents[line].append(courseStudentList[line].getName())
        listForStudents[line].append(courseStudentList[line].getId())
        # attendance sheet is a list in the AbstractStudent hence count is used to access each element in it
        for attLen in range(0,count):
            listForStudents[line].append(courseStudentList[line].getAttending()[attLen])
    # split the files and take the date
    for i in AllFilesNames:
        s = i.split("-")
        listNameandIDandDates.append(s[1]+"-"+s[2]+"-"+s[3])
    # to get the course code
    f = AllFilesNames[0].split("-")
    fullFileLocation=parentDirectory+"\\"+f[0]+" "+" Class Attendance Sheet.csv"

    with open(fullFileLocation, 'w',encoding='UTF8',newline='') as fCSV:
        writer = csv.writer(fCSV)
        writer.writerow(listNameandIDandDates)
        for m in listForStudents:
            # if statment in order not to print the empty list
            if m!=[]:
             writer.writerow(m)

# generate Class Score Sheet
def ClassScoreSheet(AllFilesNames,outPutDirectory):
    parentDirectory = outPutDirectory
    try:
        os.mkdir(path)
    except OSError as e:
        pass
    listNameandIDandDates = []
    listNameandIDandDates.append("Student Name")
    listNameandIDandDates.append("Student ID")
    count = 0
    # to know how many file we have
    for i in AllFilesNames:
        count = count + 1
    # creating nested list of size length and count, the count is for the attendance sheet
    listForStudents = [[] for _ in xrange(length)]

    for line in range(1, length):
        listForStudents[line].append(courseStudentList[line].getName())
        listForStudents[line].append(courseStudentList[line].getId())
        # participation sheet is a list in the AbstractStudent hence count is used to access each element in it
        for attLen in range(0, count):
            listForStudents[line].append(courseStudentList[line].getParticipationList()[attLen])
    # split the files and take the date
    for i in AllFilesNames:
        s = i.split("-")
        listNameandIDandDates.append(s[1] + "-" + s[2] + "-" + s[3])
    # to get the course code
    f = AllFilesNames[0].split("-")
    fullFileLocation = parentDirectory + "\\" + f[0] + " " + " Class Score Sheet.csv"

    with open(fullFileLocation, 'w', encoding='UTF8', newline='') as fCSV:
        writer = csv.writer(fCSV)
        writer.writerow(listNameandIDandDates)
        for m in listForStudents:
            # if statment in order not to print the empty list
            if m != []:
                writer.writerow(m)

# generate Non Valid Meeting Attendance Reports
def NonvalidMeetingAttendanceReports(student,fileName,outPutDirectory):
    directory = "Nonvalid Meeting Attendance Reports"
    parentDirectory = outPutDirectory
    path = os.path.join(parentDirectory, directory)
    try:
        os.mkdir(path)
    except OSError as e:
        pass
    fName =fileName.split(".")
    NonValidFileName = fName[0]+"-NV.csv"
    l =[]
    l.append(student.getName())
    l.append(student.gettotalDuration())
    # full location of the files
    fullDirLocation=path+"\\"+NonValidFileName
    # if file exists just append
    if os.path.isfile(fullDirLocation):
        with open(fullDirLocation, 'a',encoding='UTF8',newline='') as fCSV:
            writer= csv.writer(fCSV)
            writer.writerow(l)
    else:
        with open(fullDirLocation, 'w',encoding='UTF8',newline='') as fCSV:
            writer = csv.writer(fCSV)
            labels =[]
            labels.append("Name")
            labels.append("Total Duration (minutes)")
            writer.writerow(labels)
            writer.writerow(l)


# generate Non Valid Meeting Participation Reports
def NonvalidMeetingParticipationReports(NVMPRList,fileName,outPutDirectory,Tb):
            directory = "Nonvalid Meeting Participation Reports"
            parentDirectory = outPutDirectory
            pathDir = os.path.join(parentDirectory, directory)

            try:
                os.mkdir(pathDir)
            except OSError as e:
                pass
            fName = fileName.split(".")
            NonValidFileName = fName[0] + "-NV.csv"
            l = []
            # full location of the files
            fullDirLocation = pathDir + "\\" + NonValidFileName
            # if file exists just append
            if os.path.isfile(fullDirLocation):
                # pass only when
                with open(fullDirLocation, 'a', encoding='UTF8', newline='') as fCSV:
                    writer = csv.writer(fCSV)
                    for i in NVMPRList:
                        # to add eac line in one cell
                        l1 =[]
                        l1.append(" ".join(i))
                        writer.writerow(l1)
            else:
                with open(fullDirLocation, 'w', encoding='UTF8', newline='') as fCSV:
                    writer = csv.writer(fCSV)
                    labels = []
                    labels.append("Non Valid Participants and Participations")
                    writer.writerow(labels)
                    for i in NVMPRList:
                        # to add eac line in one cell
                        l1 =[]
                        l1.append(" ".join(i))
                        writer.writerow(l1)

# child class that implements the AbstractStudent class
class studetnMainClass(AbstractStudent.Student):

    # constructor for Meeting Attendance Reports
    def __init__(self, name, id, totalDuration):
        super(studetnMainClass, self).__init__(name, id, totalDuration)
    # Function for meeting attendance reports
    def __markAttendance(self ,p,index,courseFileName):
         splittedAttendance0=re.split('[-_ ()]', self.getName().lower())
         splittedAttendance=[]
         # removing space elements in the list resulted from deleting - or _ or ( or )
         for s in splittedAttendance0:
             if s !='':
                 splittedAttendance.append(s)
         occuranceOf =0
         found =False
         # to know the length of splittedAttendance since len function is not working
         lengthW=0
         for lenOfWord in splittedAttendance:
             lengthW = lengthW+1
         # the current student  in the attendence meeting report (first/last name or id or combined)
         for inSplittedAtt in splittedAttendance:
              occuranceOf = occuranceOf + 1
              # the current student (full name)  in the student list
              for inSplittedStu in splittedStudentSheet:
                  if inSplittedAtt in inSplittedStu:
                           for i in range(1, length):
                                if inSplittedAtt in courseStudentList[i].getName().lower().split() or (inSplittedAtt) == str( courseStudentList[i].getId()):
                                       if int(self.gettotalDuration()) > int(p) and (occuranceOf == lengthW):
                                           courseStudentList[i].setAttending("x")
                                           found = True
                                           index.append(i)
                                           break
                                       elif int(self.gettotalDuration()) < int(p) and (occuranceOf==lengthW):
                                           courseStudentList[i].setAttending("a")
                                           found = True
                                           index.append(i)
                                           break
                  if found == True:
                      break

              if found == True:
                  break
         #Not valid: student is not registered in this class or his name doesn't match any of the student name list
         if occuranceOf == lengthW and found == False:
               NonvalidMeetingAttendanceReports(self,courseFileName,options[0].outDir)

# to read the file from a given directory
def readFileFromDirectory(path, filename):
    if filename == None:
        fullFilePath = path
        fInDir = open(fullFilePath, 'r', encoding='utf-8')
        inp = fInDir.read()
        lines = inp.splitlines()
        return lines

    else:
        fullFilePath = path + "\\" + filename
        fInDir = open(fullFilePath, 'r', encoding='utf-8')
        inp = fInDir.read()
        lines = inp.splitlines()
        return lines



# Option Parser
parser = OptionParser()
parser.add_option('--inpSL', action='store')
parser.add_option('--inpMARdir', action='store')
parser.add_option('--inpMPRdir', action='store')
parser.add_option('--outDir',action='store')

options = parser.parse_args()
# to read students in StudentList
if options[0].inpSL != None  and options[0].outDir != None:
        all_lines = readFileFromDirectory(options[0].inpSL,None)
        courseStudentList = []
        for line in all_lines:
            one_line = line.split(',')
            courseStudentList.append(AbstractStudent.Student(one_line[1], one_line[0],0)) # 0 for total duration
        length = len(courseStudentList)

# split the student list sheet to use it in the __markAttendance method
if options[0].inpSL != None and options[0].outDir != None:
    splittedStudentSheet=[]
    for l in range(1, int(length)):
        s= courseStudentList[l].getName().lower().split() + courseStudentList[l].getId().split()
        splittedStudentSheet.append(s)
# input directory

# inpMARdir is chosen ( MAR: Meeting Attendance Reports )
if options[0].inpMARdir != None and options[0].inpSL != None and options[0].outDir != None:
    # read all the meeting attendance reports from the given directory
    all_files = os.listdir(options[0].inpMARdir)
    # to count total number of files
    __numberOfFiles =0
    for path in os.listdir(options[0].inpMARdir):
        if os.path.isfile(os.path.join(options[0].inpMARdir, path)):
            __numberOfFiles += 1
    # creating a nested list with size of numberOfFiles
    __meetingListWithVariableLength = [[] for _ in xrange(__numberOfFiles)]
    # split the lines in each file
    len=0
    for file in all_files:
        contentOfFile = readFileFromDirectory(options[0].inpMARdir, file)
        __meetingListWithVariableLength[len].append(file)
        for line in contentOfFile:
            one_line = line.split(',')
            __meetingListWithVariableLength[len].append(studetnMainClass(one_line[0], 0, one_line[1])) # 0 for ID
        len=len+1
    p = input("Please enter the value of P: ")

    AllFiles=[]
    # for each MeetingAttendanceFile in the course
    for MeetingAttendanceFile in (__meetingListWithVariableLength):
        # to know the indices of student who were absent
        index = []
        c=0
        # append all the files name in meeting attendance reports
        AllFiles.append(MeetingAttendanceFile[0])
        # loop in each file
        for content in MeetingAttendanceFile:
            # starts printing the content from 2
            # because c=0 has the name of file and  c=1 has the heading (Name (Original Name),Total Duration (Minutes))
            if c >=2:
                content._studetnMainClass__markAttendance(p, index, MeetingAttendanceFile[0])
            c=c+1
        # to mark (a) of the absent student who didn't attend
        for ind in range(1,length):
            if ind not in (index):
                    courseStudentList[ind].setAttending("a")


    #to produce the class attendance sheet
    ClassAttendanceSheet( AllFiles, options[0].outDir)



# Tb is chosen to chop off the messages  whose it's time is less than than (first message time + Tb entires)
def TbIsChosen(contentOffileTb):
    try:
        if int(Tb) > 0:
            messageTime = re.split("[: ]", contentOffileTb)
            timeOfMinutes = int(Tb) - (60 - int(messageTime[1]))
            firstTimeMessage = ""
            while int(timeOfMinutes) > 0:
                if int(messageTime[0]) < 24:
                    messageTime[0] = int(messageTime[0]) + 1
                    timeOfMinutes = int(timeOfMinutes) - 60
                    # print("firstTimeMessage = ",firstTimeMessage)
                # if the day has ended
                else:
                    messageTime[0] = 0
                    timeOfMinutes = int(timeOfMinutes) - 60

            else:
                (messageTime[1]) = (60 + timeOfMinutes)
                firstTimeMessage = str(messageTime[0]) + ":" + str(messageTime[1]) + ":" + str(messageTime[2])
                print("First time message = ", firstTimeMessage)

            # print("firstTimeMessage = ", firstTimeMessage)
        else:
            return  -1
    except ValueError:
        print("Tb must be integer")
        exit()
    return firstTimeMessage

# Te is chosen to chop off the messages from whose it's time is greater than (last message time + Te entires)
def TeIsChosen(contetofFileTe,):
    try:
        if (int(Te) > 0):
            messageTimeTe = re.split("[: ]", contetofFileTe)

            if int(Te) <= int(messageTimeTe[1]):
                messageTimeTe[1] = int(messageTimeTe[1]) - int(Te)
                # concatenate 0 if hour is less than 10
                if int(messageTimeTe[0]) < 10:
                    lastMessage =  str("0") + str(messageTimeTe[0] + ":" + str(messageTimeTe[1]) + ":" + str(messageTimeTe[2]))
                    print("last time message = ", lastMessage)
                else:
                    lastMessage = str(messageTimeTe[0]) + ":" + str(messageTimeTe[1]) + ":" + str(messageTimeTe[2])
                    print("last time message = ", lastMessage)

            else:
                timeOfMinutes = int(Te) - int(messageTimeTe[1])
                while timeOfMinutes > 0:
                    if int(messageTimeTe[0]) > 0 and int(messageTimeTe[0]) <=24:
                            messageTimeTe[0] = int(messageTimeTe[0]) - 1
                            timeOfMinutes = int(timeOfMinutes) - 60
                    elif int(messageTimeTe[0]) == 0:
                             messageTimeTe[0] = 23
                             timeOfMinutes = int(timeOfMinutes) - 60
                else:
                    timeOfMinutes = -1 * timeOfMinutes
                    messageTimeTe[1] = timeOfMinutes
                    # concatenate 0 if hour is less than 10
                    if int(messageTimeTe[0]) < 10:
                        lastMessage = "0"+str(messageTimeTe[0]) + ":" + str(messageTimeTe[1]) + ":" + str(messageTimeTe[2])
                        print("last time message = ", lastMessage)
                    else:
                        lastMessage = str(messageTimeTe[0]) + ":" + str(messageTimeTe[1]) + ":" + str(messageTimeTe[2])
                        print("last time message = ", lastMessage)

        else:
            return  -1
    except ValueError:
        print("Te must be integer")
        exit()
    return lastMessage



# inpMPRdir is chosen ( MAR: Meeting Participation Reports )
if options[0].inpMPRdir != None and options[0].inpSL != None and options[0].outDir != None:
    print("Please enter the value of Tb in minutes to drop some entities at the beginning of the meeting report (e.g = 5) OR -1 if you don't want to:")
    Tb = input("Tb = ")
    print("Please enter the value of Te in minutes to drop some entities at the end of the meeting report (e.g = 5) OR -1 if you don't want to:")
    Te = input("Te = ")

    # read all the meeting attendance reports from the given directory
    all_files = os.listdir(options[0].inpMPRdir)
    # to count total number of files
    __numberOfFiles = 0
    for path in os.listdir(options[0].inpMPRdir):
        if os.path.isfile(os.path.join(options[0].inpMPRdir, path)):
            __numberOfFiles += 1
    # creating a nested list with size of numberOfFiles
    __participationListWithVariableLength = [[] for _ in xrange(__numberOfFiles)]
    # split the lines in each file
    len = 0
    AllFilesinMPR=[]

    for file in all_files:
          contentOfFile = readFileFromDirectory(options[0].inpMPRdir, file)
          __participationListWithVariableLength[len].append(file)
        # Function to drop the first entities when Tb is chosen
          firstTimeMessage = TbIsChosen(contentOfFile[0])
          lastTimeMessage = TeIsChosen(contentOfFile[-1])
          print("File = ",file)
          NonValidMPRList = []
          # append read file
          AllFilesinMPR.append(file)
          for line in contentOfFile:
                one_line= re.split("[-_ ]", line.lower())
                indeX = 0
                # If Tb is choosen and one_line[0] ( the date) is less than the first date + Tb then it's not valid
                if int(Tb)>0 and one_line[0] < firstTimeMessage:
                    #print("one_line[0]",one_line[0],"one_line[2] name = ",one_line[2],"firstTimeMessage= ",firstTimeMessage)
                    NonValidMPRList.append(one_line)
                    continue
                # If Te is choosen and one_line[0] ( the date) is greater than the last date - Te then it's not valid
                if int (Te) > 0 and one_line[0] > lastTimeMessage:
                     NonValidMPRList.append(one_line)
                     continue

                for student in splittedStudentSheet:
                    indeX = indeX + 1 # to know the index in the coursStudentList
                    participate = False
                    occurance = 0
                    for nameOrId in student:
                            # of one line
                            for inOneLine in one_line:
                                                       # and: to make sure that the rest of the name is also in the same name, e.g Yazan Majdi Daibes: first name = Yazan and Majdi is in Yazan
                                                        # and I don't want majdi in other name excpet with first name Yazan same thing with the ID if it was in one_line[2] instead of first name
                                try:
                                    if nameOrId==inOneLine and (student[0] == one_line[2] or student[-1] == one_line[2]):
                                        participate = True
                                        occurance = occurance + 1
                                    if inOneLine=="to" and participate == True and int(nameOrId) and (occurance>1 or (occurance == 1 and int(one_line[2]))):
                                              courseStudentList[indeX].setParticipation(courseStudentList[indeX].getParticipation() + 1)
                                              # dFinished519Code code is to indicate that the student has participated and in student list sheet
                                              one_line.append("dFinished519Code")
                                except ValueError:
                                    pass
                                except IndexError:
                                    pass
                # if the participated student is not in student list sheet then consider the participation non-valid.
                if one_line[-1] != "dFinished519Code":
                    NonValidMPRList.append(one_line)

          for i in range(1,length):
                  courseStudentList[i].setParticipationList(courseStudentList[i].getParticipation())
                  #print("Name = ", courseStudentList[i].getName(), "Participation() = ", courseStudentList[i].getParticipationList())

                  # assign zero to the participation once a file is read
                  courseStudentList[i].setParticipation(0)

          NonvalidMeetingParticipationReports(NonValidMPRList,file,options[0].outDir,Tb)
          len = len + 1
    ClassScoreSheet(all_files, options[0].outDir)


if  options[0].inpSL == None or options[0].outDir == None:
    print("Please enter the path to the Student Sheet List, Meeting Attendance Report and the output Directory as:"
          "--inpSL 'your student list sheet path', "
          "--inpMARdir 'your Meeting Attendance Reports path'"
          "--inpMPRdir 'your Meeting Participation Reports path ,"
          "--outDir 'your output path'")
# # # output directory
# if options[0].outDir != None and options[0].inpSL != None and options[0].inpMARdir != None:
#     print("Hiii")

class course (studetnMainClass):

    def __init__(self,courseName, name, id):
        self.__courseName = courseName
        self.__name = name
        self.__id = id

    def getcourseName(self):
        return self.__courseName

    def setcourseName(self, courseName):
        self.__courseName = courseName

