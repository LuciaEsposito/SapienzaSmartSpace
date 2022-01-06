import os


linesToRemove = []
for activity in os.listdir("activities"):
        interval = #"23_00-05_15" # "minutes"

        inputPath1 = os.path.join("minutes", interval + ".csv")

        outputPath1 = inputPath1.replace(".csv", " " + activity.split(".")[0] + " filtered.csv")
        outputPath2 = inputPath1.replace(".csv", " " + activity.split(".")[0] + " filteredOut.csv")

        header = "case,timein,timeend,event,dayOfWeek,month\n"

        f = open(inputPath1, "r")
        lines = f.readlines()[1:]
        lenInterval = len(lines) 
        f.close()

        f1 = open(inputPath2, "r")
        lines2 = f1.readlines()[1:]
        lenActivity = len(lines2)
        f1.close()

        linesToWrite = []
        linesToWrite2 = []

        for elem in lines:
                if elem in lines2:
                        linesToWrite.append(elem)
                        linesToRemove.append(elem)
                else:
                        linesToWrite2.append(elem)  


        f2 = open(outputPath1, "w")
        f2.writelines(header)

        f2.writelines(linesToWrite)
        lenCorrespondence = len(linesToWrite)
        f2.flush()
        f2.close()


        f3 = open(outputPath2, "w")
        f3.writelines(header)

        f3.writelines(linesToWrite2)
        f3.flush()
        f3.close()

        print("Number of events in habit " + interval + ":\t " + str(lenInterval))
        print("Number of events in activity " + activity + ":\t " + str(lenActivity))
        print("\tNumber of events in activity that are present in the habit:\t " + str(lenCorrespondence))
        print("\t" + str(lenCorrespondence) + "/" + str(lenActivity) + " -> " + str(lenCorrespondence/lenActivity))
        print("\t" + str(lenCorrespondence) + "/" + str(lenInterval) + " -> " + str(lenCorrespondence/lenInterval) + " -> " + "{:.2f}".format(lenCorrespondence/lenInterval*100) + "% of the habit interval")
        print("\n")


linesNotMapped = []              
for elem in lines:
        if elem not in linesToRemove:
                linesNotMapped.append(elem)

f3 = open(inputPath1.replace(".csv", " not mapped.csv"), "w")
f3.writelines(header)

f3.writelines(linesNotMapped)
f3.flush()
f3.close()
