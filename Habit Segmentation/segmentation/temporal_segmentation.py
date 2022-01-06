import os

inputPath = "dataset_clustered_merge_successive_events.csv" # input file
outputPath = "minutes"

header = "case,timein,timeend,event,dayOfWeek,month\n"

f = open(inputPath)
lines = f.readlines()[1:]
f.close()

other = []

def stopSlot():
        return time_slots[1]

def startSlot():
        return time_slots[0]

def fSort(elem):
        return elem.split(",")[1]

def func(time_slots,fileOutput):
        for elem in lines:       
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
                
                if not os.path.exists(os.path.join(outputPath, fileOutput)):
                        f1 = open(os.path.join(outputPath, fileOutput), "w")
                        f1.writelines(header)
                else:
                        f1 = open(os.path.join(outputPath, fileOutput), "a")


                if dayStart == dayEnd:
                        if timeStart < time_slots[0] and timeEnd > time_slots[0]:
                                newTimeStart = startSlot() # round to the nearest time slot  
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeStart, newTimeStart).replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem.replace(timeStart, newTimeStart))
                                        
                        elif timeStart >= time_slots[0] and timeStart < time_slots[1]:                                
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem)
                                                
                f1.flush()
                f1.close()

def func2(start,stop):
        inputPath1 = "minutes\\" + start + "-" + stop + ".csv"

        f = open(inputPath1)
        lines = f.readlines()[1:]
        f.close()

        f1 = open(inputPath2)
        other = f1.readlines()[1:]
        f1.close()

        newLinesToWrite = []
        allLines = []

        for elem in other:
                case = elem.split(",")[0]
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
            
                #from 00_00
                if timeEnd > start.replace("_", ":") +":00":       
                        if timeEnd > stop.replace("_", ":") +":00":
                                newLinesToWrite.append(elem.replace(case,str(int(case)+1),1).replace(dayStart,dayEnd).replace(timeStart, start.replace("_", ":") +":00").replace(timeEnd, stop.replace("_", ":") +":00"))
                        else:
                                newLinesToWrite.append(elem.replace(case,str(int(case)+1),1).replace(dayStart,dayEnd).replace(timeStart, start.replace("_", ":") +":00"))

        print(len(newLinesToWrite))

        f2 = open(inputPath1, "w")
        f2.writelines(header)
        for elem in lines:
                allLines.append(elem)
        for elem in newLinesToWrite:
                allLines.append(elem)

        allLines.sort(key=fSort)
        f2.writelines(allLines)
        f2.flush()
        f2.close()

def func3(start,stop):
        inputPath1 = "minutes\\" + start + "-" + stop + ".csv"

        f = open(inputPath1)
        lines = f.readlines()[1:]
        f.close()

        f1 = open(inputPath2)
        other = f1.readlines()[1:]
        f1.close()

        newLinesToWrite = []
        allLines = []

        for elem in other:
                case = elem.split(",")[0]
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
            
                #to 00_00
                if timeStart < stop.replace("_", ":") +":00":
                        if timeStart < start.replace("_", ":") +":00":
                                newLinesToWrite.append(elem.replace(timeStart, start.replace("_", ":") +":00").replace(timeEnd, stop.replace("_", ":") +":00"))
                        else:
                                newLinesToWrite.append(elem.replace(timeEnd, stop.replace("_", ":") +":00"))

        print(len(newLinesToWrite))

        f2 = open(inputPath1, "w")
        f2.writelines(header)
        for elem in lines:
                allLines.append(elem)
        for elem in newLinesToWrite:
                allLines.append(elem)

        allLines.sort(key=fSort)
        f2.writelines(allLines)
        f2.flush()
        f2.close()



if not os.path.exists(outputPath):
        os.makedirs(outputPath)

for i in range(0,10):
        time_slots = ["0"+str(i)+":00:00", "0"+str(i)+":15:00"]
        
        fileOutput = "0"+str(i)+"_00-" + "0"+str(i)+"_15" + ".csv"

        for elem in lines:       
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
                
                if not os.path.exists(os.path.join(outputPath, fileOutput)):
                        f1 = open(os.path.join(outputPath, fileOutput), "w")
                        f1.writelines(header)
                else:
                        f1 = open(os.path.join(outputPath, fileOutput), "a")


                if dayStart == dayEnd:
                        if timeStart < time_slots[0] and timeEnd > time_slots[0]:
                                newTimeStart = startSlot() # round to the nearest time slot  
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeStart, newTimeStart).replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem.replace(timeStart, newTimeStart))
                                        
                        elif timeStart >= time_slots[0] and timeStart < time_slots[1]:                                
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem)

                else:
                        if not elem in other:
                                other.append(elem)
                                                
                f1.flush()
                f1.close()


f2 = open("otherDays.csv", "w")
f2.writelines(header)
f2.writelines(other)
f2.close()


for i in range(0,10):
        time_slots = ["0"+str(i)+":15:00", "0"+str(i)+":30:00"]
        fileOutput = "0"+str(i)+"_15-" + "0"+str(i)+"_30" + ".csv"
        func(time_slots, fileOutput)


for i in range(0,10):
        time_slots = ["0"+str(i)+":30:00", "0"+str(i)+":45:00"]
        fileOutput = "0"+str(i)+"_30-" + "0"+str(i)+"_45" + ".csv"
        func(time_slots, fileOutput)


for i in range(0,9):
        time_slots = ["0"+str(i)+":45:00", "0"+str(i+1)+":00:00"]
        fileOutput = "0"+str(i)+"_45-" + "0"+str(i+1)+"_00" + ".csv"
        func(time_slots, fileOutput)

#####################################################################################
#func(["09:45:00","10:00:00"], "09_45-10_00.csv")
fileOutput = "09_45-10_00.csv"
time_slots = ["09:45:00", "10:00:00"]
for elem in lines:       
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
                
                if not os.path.exists(os.path.join(outputPath, fileOutput)):
                        f1 = open(os.path.join(outputPath, fileOutput), "w")
                        f1.writelines(header)
                else:
                        f1 = open(os.path.join(outputPath, fileOutput), "a")

                if dayStart == dayEnd:
                        if timeStart < time_slots[0] and timeEnd > time_slots[0]:
                                newTimeStart = startSlot() # round to the nearest time slot  
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeStart, newTimeStart).replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem.replace(timeStart, newTimeStart))
                                        
                        elif timeStart >= time_slots[0] and timeStart < time_slots[1]:                                
                                if timeEnd > time_slots[1]:
                                        newTimeEnd = stopSlot() # round to the nearest time slot
                                        f1.writelines(elem.replace(timeEnd, newTimeEnd))
                                else:
                                        f1.writelines(elem)
                                                
                f1.flush()
                f1.close()
#####################################################################################

for i in range(10,24):
        time_slots = [str(i)+":00:00", str(i)+":15:00"]
        fileOutput = str(i)+"_00-" + str(i)+"_15" + ".csv"
        func(time_slots, fileOutput)
        

for i in range(10,24):
        time_slots = [str(i)+":15:00", str(i)+":30:00"]
        fileOutput = str(i)+"_15-" + str(i)+"_30" + ".csv"
        func(time_slots, fileOutput)


for i in range(10,24):
        time_slots = [str(i)+":30:00", str(i)+":45:00"]
        fileOutput = str(i)+"_30-" + str(i)+"_45" + ".csv"
        func(time_slots, fileOutput)


for i in range(10,23):
        time_slots = [str(i)+":45:00", str(i+1)+":00:00"]
        fileOutput = str(i)+"_45-" + str(i+1)+"_00" + ".csv"
        func(time_slots, fileOutput)

#####################################################################################
#func(["23:45:00","00:00:00"], "23_45-00_00.csv")
fileOutput = "23_45-00_00.csv"
time_slots = ["23:45:00", "00:00:00"]
for elem in lines:       
                dayStart = elem.split(",")[1].split(" ")[0]
                timeStart = elem.split(",")[1].split(" ")[1]
                dayEnd = elem.split(",")[2].split(" ")[0]
                timeEnd = elem.split(",")[2].split(" ")[1]
                
                if not os.path.exists(os.path.join(outputPath, fileOutput)):
                        f1 = open(os.path.join(outputPath, fileOutput), "w")
                        f1.writelines(header)
                else:
                        f1 = open(os.path.join(outputPath, fileOutput), "a")


                if dayStart == dayEnd:
                        if timeStart < time_slots[0] and timeEnd > time_slots[0]:
                                newTimeStart = startSlot() # round to the nearest time slot  
                                f1.writelines(elem.replace(timeStart, newTimeStart))
                                        
                        elif timeStart >= time_slots[0]:                                
                                f1.writelines(elem)
                         
                f1.flush()
                f1.close()
#####################################################################################


#################################################################
# add other days
inputPath2 = "otherDays.csv"

for i in range(0,10):
        start = "0" + str(i) + "_00"
        stop = "0" + str(i) + "_15"
        
        func2(start,stop)

for i in range(0,10):
        start = "0" + str(i) + "_15"
        stop = "0" + str(i) + "_30"
        
        func2(start,stop)

for i in range(0,10):
        start = "0" + str(i) + "_30"
        stop = "0" + str(i) + "_45"
        
        func2(start,stop)

for i in range(0,9):
        start = "0" + str(i) + "_45"
        stop = "0" + str(i+1) + "_00"
        
        func2(start,stop)


for i in range(19,24):
        start = str(i) + "_00"
        stop = str(i) + "_15"
        
        func3(start,stop)

for i in range(19,24):
        start = str(i) + "_15"
        stop = str(i) + "_30"
        
        func3(start,stop)

for i in range(19,24):
        start = str(i) + "_30"
        stop = str(i) + "_45"
        
        func3(start,stop)

for i in range(19,23):
        start = str(i) + "_45"
        stop = str(i+1) + "_00"
        
        func3(start,stop)

#####################################################################################
#func3("23_45","00_00")
start = "23_45"
stop = "00_00"
inputPath1 = "minutes\\" + start + "-" + stop + ".csv"
inputPath2 = "otherDays.csv"

f = open(inputPath1)
lines = f.readlines()[1:]
f.close()

f1 = open(inputPath2)
other = f1.readlines()[1:]
f1.close()

newLinesToWrite = []
allLines = []

for elem in other:
        case = elem.split(",")[0]
        dayStart = elem.split(",")[1].split(" ")[0]
        timeStart = elem.split(",")[1].split(" ")[1]
        dayEnd = elem.split(",")[2].split(" ")[0]
        timeEnd = elem.split(",")[2].split(" ")[1]

        if timeStart < start.replace("_", ":") +":00":
                newLinesToWrite.append(elem.replace(timeStart, start.replace("_", ":") +":00").replace(timeEnd, stop.replace("_", ":") +":00"))
        else:
                newLinesToWrite.append(elem.replace(timeEnd, stop.replace("_", ":") +":00"))
        
print(len(newLinesToWrite))

f2 = open(inputPath1, "w")
f2.writelines(header)
for elem in lines:
        allLines.append(elem)
for elem in newLinesToWrite:
        allLines.append(elem)

allLines.sort(key=fSort)
f2.writelines(allLines)
f2.flush()
f2.close()
#####################################################################################
