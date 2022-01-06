import os


activities = ["Bed_to_Toilet", "Eating", "Enter_Home", "Housekeeping", "Leave_Home", "Meal_Preparation", "Relax", "Resperate", "Sleeping", "Wash_Dishes", "Work"]
inputPath1 = "output task\\Bed_to_Toilet" # \\activities
inputPath2 = "dataset_clustered_merge_successive_events.csv"

outputFolder = "activities"
if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
        
outputPath = outputFolder + "\\" + "Bed_to_Toilet.csv" # \\activities

header = "case,timein,timeend,event,dayOfWeek,month\n"

linesToWrite = []


def ord(elem):
        return elem.split(",")[1]



f = open(inputPath2, "r")
lines = f.readlines()[1:]
f.close()

f2 = open(outputPath, "w")
f2.writelines(header)


for filename in os.listdir(inputPath1):
        f1 = open(os.path.join(inputPath1,filename), "r")
        linesActivity = f1.readlines()
        start = linesActivity[0].split("\t")[0].replace("-","/") + " " + linesActivity[0].split("\t")[1]
        end = linesActivity[len(linesActivity)-1].split("\t")[0].replace("-","/") + " " + linesActivity[len(linesActivity)-1].split("\t")[1]
        print(filename)
        print("\t"+start)
        print("\t"+end)
        
        for elem in lines:
                if elem.split(",")[1] >= start.split(".")[0] and elem.split(",")[1] < end and elem.split(",")[1] != end.split(".")[0]:
                        print(elem)
                        linesToWrite.append(elem)
                elif elem.split(",")[2] >= start and elem.split(",")[2] <= end.split(".")[0]:
                        print(elem)
                        linesToWrite.append(elem)
                elif elem.split(",")[1] <= start.split(".")[0] and elem.split(",")[2] >= end.split(".")[0]:
                        print(elem)
                        linesToWrite.append(elem)
                elif elem.split(",")[1].split(" ")[0] > end:
                        break

        f1.close()

linesToWrite.sort(key=ord)
f2.writelines(linesToWrite)
f2.flush()
f2.close()
