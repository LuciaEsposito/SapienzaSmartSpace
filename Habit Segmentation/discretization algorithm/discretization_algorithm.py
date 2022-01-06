import operator
import os
import subprocess
from shutil import copy2


structuredness = []
simplicity = []

path = "minutes"
temp_path = "temp"

script = "script_inductive_miner.txt"
batch_path = "ProM_CLI.bat"

MIN_NUM_INTERVALS = 6 # stopping criterion
MIN_DIFF = 420 # stopping criterion          


#################################################################

def mergeIntervals(filename1, filename2):

    file1 = os.path.join(path, filename1)
    file2 = os.path.join(path, filename2)

    header = "case,timein,timeend,event,dayOfWeek,month\n"

    outputname = newIntervalFilename(filename1, filename2)
    print("Merging " + filename1 + " and " + filename2 + " -> " + outputname)
    fileOutput = os.path.join(temp_path, outputname)
    f = open(fileOutput, "w")

    f1 = open(file1, "r")
    lines = f1.readlines()[1:]
    f2 = open(file2, "r")
    lines2 = f2.readlines()[1:]

    linesTot = []
    linesToWrite = []
    linesToRemove = []

    for elem in lines:
        linesTot.append(elem)

    for elem in lines2:
        linesTot.append(elem)

    linesTot.sort(key=sortintervals)

    # merge two subsequent equal events into one event
    for i in range(len(linesTot)-1):
        if linesTot[i].split(",")[2] == linesTot[i+1].split(",")[1] and linesTot[i].split(",")[3] == linesTot[i+1].split(",")[3]:              
                new_line = linesTot[i].replace(linesTot[i].split(",")[2], linesTot[i+1].split(",")[2])
                
                linesToRemove.append(linesTot[i])
                linesToRemove.append(linesTot[i+1])

                linesToWrite.append(new_line)

    for elem in linesTot:
        if elem not in linesToRemove:
                linesToWrite.append(elem)

    linesToWrite.sort(key=sortintervals)

    f.writelines(header)
    f.writelines(linesToWrite)

    f.flush()
    f.close()
    f1.close()
    f2.close()    

    return outputname


    
def sortintervals(elem):
    return elem.split(",")[1]


#################################################################

def newIntervalFilename(filename1, filename2):
    interval1 = filename1.split("-")[0]
    interval2 = filename2.split("-")[1]

    newInterval = interval1 + "-" + interval2
    newName = newInterval
    return newName

#################################################################

def changeNoiseThreshold(filename):
    noise_threshold = ["0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
    for elem in noise_threshold:
        output = subprocess.run([batch_path, "-f", script, filename, elem], text=True, capture_output=True)
        structVal = float(output.stdout.split("structuredness")[1])
        simplVal = (float(output.stdout.split("numPlaces")[1])+float(output.stdout.split("numTransitions")[1]))/float(output.stdout.split("numArcs")[1])
        print(filename + " -> noise threshold: " + elem + ", structuredness: " + str(structVal))
        if structVal != -1.0:
            break
        
    if structVal == -1.0:
        output = subprocess.run([batch_path, "-f", script, filename], text=True, capture_output=True)
        structVal = float(output.stdout.split("structuredness")[1])
        simplVal = (float(output.stdout.split("numPlaces")[1])+float(output.stdout.split("numTransitions")[1]))/float(output.stdout.split("numArcs")[1])


    print("structuredness: " + str(structVal) + ", simplicity: " + str(simplVal))
    return structVal, simplVal    

#################################################################

def discretize(diff,temp_diff):
    numIntervals = len(diff)

    while numIntervals > MIN_NUM_INTERVALS:
        print("\n*************************************************************************")
        print(str(numIntervals) + " / " + str(MIN_NUM_INTERVALS))


        minValue = 1000
        for k in temp_diff.keys():
            diffVal = temp_diff[k][2]
            if diffVal < minValue:
                minValue = diffVal
                minSimpl = temp_diff[k][1]
                tempIntervalMin = k
	
        i=0
        for f in enumerate(os.listdir(temp_path)):
            filename = os.path.join(temp_path, f[1])
            if tempIntervalMin in filename:
                filenameMin = os.listdir(temp_path)[i]
                break

            i += 1

        print("Min value is " + str(temp_diff[tempIntervalMin][0]) + "\t" + str(temp_diff[tempIntervalMin][1]) + "\t" + str(temp_diff[tempIntervalMin][2]) + " -> " + filenameMin)


        if minValue > MIN_DIFF:
            break
        '''
        if minSimpl < 0.68:
            temp_temp_diff = temp_diff.copy()
            while(len(temp_temp_diff)>1):
                temp_temp_diff.pop(filenameMin.split(".")[0])
                minValue = 1000
                for k in temp_temp_diff.keys():
                    diffVal = temp_temp_diff[k][2]
                    if diffVal < minValue:
                        minValue = diffVal
                        minSimpl = temp_temp_diff[k][1]
                        tempIntervalMin = k
                i=0
                for f in enumerate(os.listdir(temp_path)):
                    filename = os.path.join(temp_path, f[1])
                    if tempIntervalMin in filename:
                        filenameMin = os.listdir(temp_path)[i]
                        break

                    i += 1

                print("Min value is " + str(temp_temp_diff[tempIntervalMin][0]) + "\t" + str(temp_temp_diff[tempIntervalMin][1]) + "\t" + str(temp_temp_diff[tempIntervalMin][2]) + " -> " + filenameMin)
                if minSimpl >= 0.68:
                    break
                
            if minValue > MIN_DIFF or minSimpl < 0.68:
                break
        '''
        

        # copy the merged file from "/temp" to "/minutes"
        num_files = len(next(os.walk(temp_path))[2])
        i=0
        for f in enumerate(os.listdir(temp_path)):
            filename = os.path.join(temp_path, f[1])
            if tempIntervalMin in filename:
                merged_file = os.listdir(temp_path)[i]
                if i == 0:
                    pred_merged_file = os.listdir(temp_path)[num_files-1]
                    next_merged_file = os.listdir(temp_path)[i+1]
                elif i == num_files-1:
                    pred_merged_file = os.listdir(temp_path)[i-1]
                    next_merged_file = os.listdir(temp_path)[0]
                else:
                    pred_merged_file = os.listdir(temp_path)[i-1]
                    next_merged_file = os.listdir(temp_path)[i+1]
                break
            i += 1

        merged_file_path = os.path.join(temp_path, merged_file)
        copy2(merged_file_path, os.path.join(path, merged_file))
        print("Copy " + merged_file_path + " in " + os.path.join(path, merged_file))


        # remove from "/minutes" the two intervals that form the merged file
        num_files = len(next(os.walk(path))[2])
        i=0
        for f in enumerate(os.listdir(path)):
            filename = os.path.join(path, f[1])
            if tempIntervalMin in filename:
                if i == 0:
                    removed_file1 = os.listdir(path)[num_files-1]
                    removed_file2 = os.listdir(path)[i+1]
                elif i == num_files-1:
                    removed_file1 = os.listdir(path)[i-1]
                    removed_file2 = os.listdir(path)[0]
                else:
                    if tempIntervalMin.split("-")[0].split("_")[0] > "15" and tempIntervalMin.split("-")[1].split("_")[0] < "09" :
                        removed_file1 = os.listdir(path)[i+1]
                        removed_file2 = os.listdir(path)[i+2]
                    else:
                        removed_file1 = os.listdir(path)[i-1]
                        removed_file2 = os.listdir(path)[i+1]
                break
    
            i += 1       

        os.remove(os.path.join(path, removed_file1))
        os.remove(os.path.join(path, removed_file2))
        print("\t'minutes' remove " + removed_file1)
        print("\t'minutes' remove " + removed_file2)
          

        # update diff dictionary
        diff[tempIntervalMin] = temp_diff[tempIntervalMin]
        diff.pop(removed_file1.split(".")[0])
        diff.pop(removed_file2.split(".")[0])

        #print("Update diff")
        #print(diff)
        
        
        # remove from "/temp" the merged file and the two neighboring intervals
        os.remove(os.path.join(temp_path, pred_merged_file))
        os.remove(os.path.join(temp_path, merged_file))
        os.remove(os.path.join(temp_path, next_merged_file))
        print("\t'temp' remove " + pred_merged_file)
        print("\t'temp' remove " + merged_file)
        print("\t'temp' remove " + next_merged_file)

        
        # update temp_diff dictionary
        temp_diff.pop(pred_merged_file.split(".")[0])
        temp_diff.pop(merged_file.split(".")[0])
        temp_diff.pop(next_merged_file.split(".")[0])
        #print("Update temp_diff")
        #for f in enumerate(os.listdir(temp_path)):
        #    filename = os.path.join(temp_path, f[1])
        #    print(filename + " -> " + str(temp_diff[f[1].split(".")[0]]))
            
        #print(temp_diff)
        

        numIntervals -= 1



        num_files = len(next(os.walk(path))[2])
        i=0
        for f in enumerate(os.listdir(path)):
            filename = os.path.join(path, f[1])
            if tempIntervalMin in filename:
                current_file = os.listdir(path)[i]
                if i == 0:
                    predFilename = os.listdir(path)[num_files-1]
                    nextFilename = os.listdir(path)[i+1]
                elif i == num_files-1:
                    predFilename = os.listdir(path)[i-1]
                    nextFilename = os.listdir(path)[0]
                else:
                    predFilename = os.listdir(path)[i-1]
                    nextFilename = os.listdir(path)[i+1]
                break
            i += 1


        mergedFile1 = mergeIntervals(predFilename, current_file)        
        mergedFile2 = mergeIntervals(current_file, nextFilename)

 
        filename1 = os.path.join(temp_path, mergedFile1)
        output1 = subprocess.run([batch_path, "-f", script, filename1], text=True, capture_output=True)
        temp_diff[mergedFile1.split(".")[0]] = []
        if float(output1.stdout.split("structuredness")[1]) == -1.0:
            (newStruct, newSimpl) = changeNoiseThreshold(os.path.join(temp_path, mergedFile1))
            temp_diff[mergedFile1.split(".")[0]].append(newStruct)
            temp_diff[mergedFile1.split(".")[0]].append(newSimpl)
        else:
            temp_diff[mergedFile1.split(".")[0]].append(float(output1.stdout.split("structuredness")[1]))
            temp_diff[mergedFile1.split(".")[0]].append((float(output1.stdout.split("numPlaces")[1])+float(output1.stdout.split("numTransitions")[1]))/float(output1.stdout.split("numArcs")[1]))

        if temp_diff[mergedFile1.split(".")[0]][0] != -1.0:
            temp_diff[mergedFile1.split(".")[0]].append(temp_diff[mergedFile1.split(".")[0]][0] - 100*temp_diff[mergedFile1.split(".")[0]][1])
        else:
            temp_diff[mergedFile1.split(".")[0]].append(1000)
        print(mergedFile1 + ": " + str(temp_diff[mergedFile1.split(".")[0]][0]) + ", " + str(temp_diff[mergedFile1.split(".")[0]][1]) + ", " + str(temp_diff[mergedFile1.split(".")[0]][2]))

        filename2 = os.path.join(temp_path, mergedFile2)
        output2 = subprocess.run([batch_path, "-f", script, filename2], text=True, capture_output=True)
        temp_diff[mergedFile2.split(".")[0]] = []
        if float(output2.stdout.split("structuredness")[1]) == -1.0:
            (newStruct, newSimpl) = changeNoiseThreshold(os.path.join(temp_path, mergedFile2))
            temp_diff[mergedFile2.split(".")[0]].append(newStruct)
            temp_diff[mergedFile2.split(".")[0]].append(newSimpl)
        else:
            temp_diff[mergedFile2.split(".")[0]].append(float(output2.stdout.split("structuredness")[1]))
            temp_diff[mergedFile2.split(".")[0]].append((float(output2.stdout.split("numPlaces")[1])+float(output2.stdout.split("numTransitions")[1]))/float(output2.stdout.split("numArcs")[1]))

        if temp_diff[mergedFile2.split(".")[0]][0] != -1.0:
            temp_diff[mergedFile2.split(".")[0]].append(temp_diff[mergedFile2.split(".")[0]][0] - 100*temp_diff[mergedFile2.split(".")[0]][1])
        else:
            temp_diff[mergedFile2.split(".")[0]].append(1000)
        print(mergedFile2 + ": " + str(temp_diff[mergedFile2.split(".")[0]][0]) + ", " + str(temp_diff[mergedFile2.split(".")[0]][1]) + ", " + str(temp_diff[mergedFile2.split(".")[0]][2]))



        #for f in enumerate(os.listdir(temp_path)):
        #    filename = os.path.join(temp_path, f[1])
        #    print(filename + " -> " + str(temp_diff[f[1].split(".")[0]]))
            
        print(temp_diff)
        print(diff)
                  

    #print("Best interval is " + MAX_FILE.split(".")[0] + " with structuredness "  + str(MAX_VALUE))

#################################################################


for f in enumerate(os.listdir(path)): 
    filename = os.path.join(path, f[1])
    output = subprocess.run([batch_path, "-f", script, filename], text=True, capture_output=True)

    if float(output.stdout.split("structuredness")[1]) == -1.0:
        (newStruct, newSimpl) = changeNoiseThreshold(filename)
        structuredness.append(newStruct)
        simplicity.append(newSimpl)
    else:
        structuredness.append(float(output.stdout.split("structuredness")[1]))
        numPlaces = float(output.stdout.split("numPlaces")[1])
        numTransitions = float(output.stdout.split("numTransitions")[1])
        numArcs = float(output.stdout.split("numArcs")[1])
        simplicity.append((numPlaces+numTransitions)/numArcs)

print(structuredness)    
print(simplicity)


diff = dict()
i=0
for f in enumerate(os.listdir(path)):
    filename = f[1].split(".")[0]
    diff[filename] = []
    diff[filename].append(structuredness[i])
    diff[filename].append(simplicity[i])
    if diff[filename][0] != -1.0:
        diff[filename].append(diff[filename][0]-100*diff[filename][1])
    else:
        diff[filename].append(1000)
    i += 1
print(diff)


minValue = 1000
for k in diff.keys():
    diffVal = diff[k][2]
    if diffVal < minValue:
        minValue = diffVal
        intervalMin = k
	
i=0
for f in enumerate(os.listdir(path)):
    filename = os.path.join(path, f[1])
    if intervalMin in filename:
        filenameMin = os.listdir(path)[i]

    i += 1

print("Min value is " + str(diff[intervalMin][0]) + "\t" + str(diff[intervalMin][1]) + "\t" + str(diff[intervalMin][2]) + " -> " + filenameMin)



for index in range(0,len(simplicity)):
    if index == len(simplicity)-1:
        currentFile = os.listdir(path)[index]
        nextFilename = os.listdir(path)[0]
    else:
        currentFile = os.listdir(path)[index]
        nextFilename = os.listdir(path)[index+1]
        
    mergeIntervals(currentFile, nextFilename)


temp_struct = []
temp_simpl = []

for f in enumerate(os.listdir(temp_path)): 
    filename = os.path.join(temp_path, f[1])
    output = subprocess.run([batch_path, "-f", script, filename], text=True, capture_output=True)

    if float(output.stdout.split("structuredness")[1]) == -1.0:
        (newStruct, newSimpl) = changeNoiseThreshold(filename)
        temp_struct.append(newStruct)
        temp_simpl.append(newSimpl)
    else:
        temp_struct.append(float(output.stdout.split("structuredness")[1]))   
        numPlaces = float(output.stdout.split("numPlaces")[1])
        numTransitions = float(output.stdout.split("numTransitions")[1])
        numArcs = float(output.stdout.split("numArcs")[1])
        temp_simpl.append((numPlaces+numTransitions)/numArcs)

print(temp_struct)
print(temp_simpl)

temp_diff = dict()
i=0
for f in enumerate(os.listdir(temp_path)):
    filename = f[1].split(".")[0]
    temp_diff[filename] = []
    temp_diff[filename].append(temp_struct[i])
    temp_diff[filename].append(temp_simpl[i])
    if temp_diff[filename][0] != -1:
        temp_diff[filename].append(temp_diff[filename][0]-100*temp_diff[filename][1])
    else:
        temp_diff[filename].append(1000)
    i += 1
print(temp_diff)


minValue = 1000
for k in temp_diff.keys():
    diffVal = temp_diff[k][2]
    if diffVal < minValue:
        minValue = diffVal
        tempIntervalMin = k
	
i=0
for f in enumerate(os.listdir(temp_path)):
    filename = os.path.join(temp_path, f[1])
    if tempIntervalMin in filename:
        tempFilenameMin = os.listdir(temp_path)[i]

    i += 1

print("Min value is " + str(temp_diff[tempIntervalMin][0]) + "\t" + str(temp_diff[tempIntervalMin][1]) + "\t" + str(temp_diff[tempIntervalMin][2]) + " -> " + tempFilenameMin)



#diff = {'00_00-00_15 220': [100.0, 0.7195121951219512, 28.048780487804876], '00_15-00_30 220': [59.0, 0.6956521739130435, -10.565217391304344], '00_30-00_45 220': [94.0, 0.7352941176470589, 20.470588235294116], '00_45-01_00 220': [224.0, 0.7567567567567568, 148.32432432432432], '01_00-01_15 220': [304.0, 0.7432432432432432, 229.67567567567568], '01_15-01_30 220': [5808.0, 0.7631578947368421, 5731.684210526316], '01_30-01_45 220': [100.0, 0.74, 26.0], '01_45-02_00 220': [144.0, 0.7291666666666666, 71.08333333333334], '02_00-02_15 220': [50.0, 0.76, -26.0], '02_15-02_30 220': [100.0, 0.7608695652173914, 23.91304347826086], '02_30-02_45 220': [40.0, 0.75, -35.0], '02_45-03_00 220': [234.0, 0.75, 159.0], '03_00-03_15 220': [216.0, 0.75, 141.0], '03_15-03_30 220': [64.0, 0.75, -11.0], '03_30-03_45 220': [3044.0, 0.7558139534883721, 2968.4186046511627], '03_45-04_00 220': [108.0, 0.76, 32.0], '04_00-04_15 220': [48.0, 0.7058823529411765, -22.588235294117652], '04_15-04_30 220': [142.0, 0.75, 67.0], '04_30-04_45 220': [68.0, 0.734375, -5.4375], '04_45-05_00 220': [1656.0, 0.7432432432432432, 1581.6756756756756], '05_00-05_15 220': [106.0, 0.7567567567567568, 30.324324324324323], '05_15-05_30 220': [162.0, 0.7027027027027027, 91.72972972972973], '05_30-05_45 220': [204.0, 0.696969696969697, 134.3030303030303], '05_45-06_00 220': [26632.5, 0.7884615384615384, 26553.653846153848], '06_00-06_15 220': [2106.0, 0.7450980392156863, 2031.4901960784314], '06_15-06_30 220': [176.0, 0.6627906976744186, 109.72093023255815], '06_30-06_45 220': [103.0, 0.6979166666666666, 33.20833333333334], '06_45-07_00 220': [196.0, 0.6458333333333334, 131.41666666666666], '07_00-07_15 220': [568.0, 0.6964285714285714, 498.3571428571429], '07_15-07_30 220': [136.0, 0.6568627450980392, 70.31372549019608], '07_30-07_45 220': [136.0, 0.6727272727272727, 68.72727272727273], '07_45-08_00 220': [318.0, 0.6530612244897959, 252.69387755102042], '08_00-08_15 220': [256.0, 0.65, 191.0], '08_15-08_30 220': [264.0, 0.625, 201.5], '08_30-08_45 220': [176.0, 0.625, 113.5], '08_45-09_00 220': [286.0, 0.6730769230769231, 218.69230769230768], '09_00-09_15 220': [414.0, 0.7049180327868853, 343.5081967213115], '09_15-09_30 220': [166.0, 0.6896551724137931, 97.03448275862068], '09_30-09_45 220': [232.0, 0.6634615384615384, 165.65384615384616], '09_45-10_00 220': [252.0, 0.6698113207547169, 185.0188679245283], '10_00-10_15 220': [369.0, 0.6792452830188679, 301.07547169811323], '10_15-10_30 220': [956.0, 0.6730769230769231, 888.6923076923077], '10_30-10_45 220': [252.0, 0.6309523809523809, 188.9047619047619], '10_45-11_00 220': [210.0, 0.6530612244897959, 144.69387755102042], '11_00-11_15 220': [208.0, 0.6413043478260869, 143.8695652173913], '11_15-11_30 220': [368.0, 0.7063492063492064, 297.3650793650794], '11_30-11_45 220': [110.0, 0.6666666666666666, 43.33333333333334], '11_45-12_00 220': [1128.0, 0.7068965517241379, 1057.3103448275863], '12_00-12_15 220': [438.0, 0.6938775510204082, 368.61224489795916], '12_15-12_30 220': [507.0, 0.7090909090909091, 436.0909090909091], '12_30-12_45 220': [384.0, 0.648936170212766, 319.1063829787234], '12_45-13_00 220': [102.0, 0.67, 35.0], '13_00-13_15 220': [118.0, 0.6382978723404256, 54.170212765957444], '13_15-13_30 220': [240.0, 0.6530612244897959, 174.69387755102042], '13_30-13_45 220': [97.0, 0.648936170212766, 32.1063829787234], '13_45-14_00 220': [261.0, 0.65, 196.0], '14_00-14_15 220': [172.0, 0.6463414634146342, 107.36585365853658], '14_15-14_30 220': [370.0, 0.7131147540983607, 298.6885245901639], '14_30-14_45 220': [260.0, 0.660377358490566, 193.96226415094338], '14_45-15_00 220': [220.0, 0.6530612244897959, 154.69387755102042], '15_00-15_15 220': [300.0, 0.6477272727272727, 235.22727272727275], '15_15-15_30 220': [246.0, 0.6282051282051282, 183.17948717948718], '15_30-15_45 220': [141.0, 0.6413043478260869, 76.86956521739131], '15_45-16_00 220': [628.0, 0.6916666666666667, 558.8333333333334], '16_00-16_15 220': [228.0, 0.6632653061224489, 161.67346938775512], '16_15-16_30 220': [256.0, 0.68, 188.0], '16_30-16_45 220': [460.0, 0.6785714285714286, 392.1428571428571], '16_45-17_00 220': [354.0, 0.7096774193548387, 283.0322580645161], '17_00-17_15 220': [170.0, 0.7131147540983607, 98.68852459016394], '17_15-17_30 220': [276.0, 0.6836734693877551, 207.6326530612245], '17_30-17_45 220': [198.0, 0.648936170212766, 133.1063829787234], '17_45-18_00 220': [169.0, 0.7033898305084746, 98.66101694915254], '18_00-18_15 220': [200.0, 0.6052631578947368, 139.4736842105263], '18_15-18_30 220': [230.0, 0.6222222222222222, 167.77777777777777], '18_30-18_45 220': [610.0, 0.6875, 541.25], '18_45-19_00 220': [222.0, 0.6351351351351351, 158.48648648648648], '19_00-19_15 220': [315.0, 0.6666666666666666, 248.33333333333334], '19_15-19_30 220': [113.0, 0.6666666666666666, 46.33333333333334], '19_30-19_45 220': [92.0, 0.6704545454545454, 24.954545454545453], '19_45-20_00 220': [170.0, 0.675, 102.5], '20_00-20_15 220': [435.0, 0.65, 370.0], '20_15-20_30 220': [188.0, 0.6818181818181818, 119.81818181818183], '20_30-20_45 220': [86.0, 0.6666666666666666, 19.333333333333343], '20_45-21_00 220': [184.0, 0.6818181818181818, 115.81818181818183], '21_00-21_15 220': [288.0, 0.6842105263157895, 219.57894736842104], '21_15-21_30 220': [268.0, 0.69, 199.0], '21_30-21_45 220': [192.0, 0.6875, 123.25], '21_45-22_00 220': [307.5, 0.7410714285714286, 233.39285714285714], '22_00-22_15 220': [264.0, 0.6585365853658537, 198.14634146341461], '22_15-22_30 220': [76.0, 0.6756756756756757, 8.432432432432435], '22_30-22_45 220': [336.0, 0.6829268292682927, 267.7073170731707], '22_45-23_00 220': [954.0, 0.723404255319149, 881.6595744680851], '23_00-23_15 220': [168.0, 0.6666666666666666, 101.33333333333334], '23_15-23_30 220': [97.0, 0.6888888888888889, 28.111111111111114], '23_30-23_45 220': [141.0, 0.717391304347826, 69.26086956521739], '23_45-00_00 220': [144.0, 0.6911764705882353, 74.88235294117648]}
#temp_diff = {'00_00-00_30 220': [264.0, 0.6666666666666666, 197.33333333333334], '00_15-00_45 220': [279.0, 0.7209302325581395, 206.90697674418607], '00_30-01_00 220': [462.0, 0.7619047619047619, 385.8095238095238], '00_45-01_15 220': [150.0, 0.7352941176470589, 76.47058823529412], '01_00-01_30 220': [1053.0, 0.77, 976.0], '01_15-01_45 220': [3208.0, 0.75, 3133.0], '01_30-02_00 220': [146.0, 0.7285714285714285, 73.14285714285715], '01_45-02_15 220': [1178.0, 0.75, 1103.0], '02_00-02_30 220': [264.0, 0.75, 189.0], '02_15-02_45 220': [156.0, 0.7575757575757576, 80.24242424242425], '02_30-03_00 220': [67.0, 0.7258064516129032, -5.58064516129032], '02_45-03_15 220': [408.0, 0.7631578947368421, 331.6842105263158], '03_00-03_30 220': [1044.0, 0.7840909090909091, 965.5909090909091], '03_15-03_45 220': [252.0, 0.7678571428571429, 175.21428571428572], '03_30-04_00 220': [1336.0, 0.7641509433962265, 1259.5849056603774], '03_45-04_15 220': [74.0, 0.7758620689655172, -3.5862068965517295], '04_00-04_30 220': [142.0, 0.75, 67.0], '04_15-04_45 220': [198.0, 0.7571428571428571, 122.28571428571429], '04_30-05_00 220': [28912.0, 0.7653061224489796, 28835.469387755104], '04_45-05_15 220': [100.0, 0.75, 25.0], '05_00-05_30 220': [146.0, 0.7549019607843137, 70.50980392156863], '05_15-05_45 220': [588.0, 0.6847826086956522, 519.5217391304348], '05_30-06_00 220': [384.0, 0.6888888888888889, 315.1111111111111], '05_45-06_15 220': [1020.0, 0.7166666666666667, 948.3333333333334], '06_00-06_30 220': [704.0, 0.7232142857142857, 631.6785714285714], '06_15-06_45 220': [310.0, 0.696078431372549, 240.39215686274508], '06_30-07_00 220': [282.0, 0.6413043478260869, 217.8695652173913], '06_45-07_15 220': [110.0, 0.5875, 51.25], '07_00-07_30 220': [510.0, 0.6595744680851063, 444.04255319148933], '07_15-07_45 220': [99.0, 0.6382978723404256, 35.170212765957444], '07_30-08_00 220': [117.0, 0.6595744680851063, 51.04255319148936], '07_45-08_15 220': [246.0, 0.6458333333333334, 181.41666666666666], '08_00-08_30 220': [198.0, 0.6354166666666666, 134.45833333333334], '08_15-08_45 220': [408.0, 0.660377358490566, 341.9622641509434], '08_30-09_00 220': [136.0, 0.65, 71.0], '08_45-09_15 220': [1254.0, 0.680327868852459, 1185.967213114754], '09_00-09_30 220': [387.0, 0.6698113207547169, 320.0188679245283], '09_15-09_45 220': [4355.0, 0.726027397260274, 4282.397260273972], '09_30-10_00 220': [180.0, 0.625, 117.5], '09_45-10_15 220': [546.0, 0.7142857142857143, 474.57142857142856], '10_00-10_30 220': [107.0, 0.6634615384615384, 40.65384615384616], '10_15-10_45 220': [264.0, 0.625, 201.5], '10_30-11_00 220': [291.0, 0.6304347826086957, 227.95652173913044], '10_45-11_15 220': [452.0, 0.7033898305084746, 381.66101694915255], '11_00-11_30 220': [240.0, 0.6, 180.0], '11_15-11_45 220': [552.0, 0.6666666666666666, 485.33333333333337], '11_30-12_00 220': [206.0, 0.6382978723404256, 142.17021276595744], '11_45-12_15 220': [4389.0, 0.7530864197530864, 4313.691358024691], '12_00-12_30 220': [134.0, 0.6842105263157895, 65.57894736842105], '12_15-12_45 220': [575.0, 0.6730769230769231, 507.6923076923077], '12_30-13_00 220': [120.0, 0.6698113207547169, 53.01886792452831], '12_45-13_15 220': [224.0, 0.6727272727272727, 156.72727272727275], '13_00-13_30 220': [123.0, 0.6770833333333334, 55.29166666666666], '13_15-13_45 220': [384.0, 0.7096774193548387, 313.0322580645161], '13_30-14_00 220': [182.0, 0.6363636363636364, 118.36363636363637], '13_45-14_15 220': [336.0, 0.6190476190476191, 274.0952380952381], '14_00-14_30 220': [264.0, 0.6363636363636364, 200.36363636363637], '14_15-14_45 220': [470.0, 0.6521739130434783, 404.7826086956522], '14_30-15_00 220': [636.0, 0.7096774193548387, 565.0322580645161], '14_45-15_15 220': [132.0, 0.6730769230769231, 64.6923076923077], '15_00-15_30 220': [242.0, 0.6276595744680851, 179.2340425531915], '15_15-15_45 220': [240.0, 0.6326530612244898, 176.73469387755102], '15_30-16_00 220': [300.0, 0.6458333333333334, 235.41666666666666], '15_45-16_15 220': [125.0, 0.6568627450980392, 59.31372549019608], '16_00-16_30 220': [282.0, 0.6792452830188679, 214.0754716981132], '16_15-16_45 220': [176.0, 0.8333333333333334, 92.66666666666666], '16_30-17_00 220': [333.0, 0.6333333333333333, 269.6666666666667], '16_45-17_15 220': [192.0, 0.6309523809523809, 128.9047619047619], '17_00-17_30 220': [116.0, 0.6634615384615384, 49.65384615384616], '17_15-17_45 220': [777.0, 0.7318840579710145, 703.8115942028985], '17_30-18_00 220': [154.0, 0.6949152542372882, 84.50847457627118], '17_45-18_15 220': [145.0, 0.6944444444444444, 75.55555555555556], '18_00-18_30 220': [270.0, 0.65625, 204.375], '18_15-18_45 220': [396.0, 0.7307692307692307, 322.9230769230769], '18_30-19_00 220': [180.0, 0.6666666666666666, 113.33333333333334], '18_45-19_15 220': [267.0, 0.6282051282051282, 204.17948717948718], '19_00-19_30 220': [-1.0, 0.6785714285714286, 1000], '19_15-19_45 220': [162.0, 0.631578947368421, 98.84210526315789], '19_30-20_00 220': [328.0, 0.6375, 264.25], '19_45-20_15 220': [1290.0, 0.6909090909090909, 1220.909090909091], '20_00-20_30 220': [300.0, 0.6914893617021277, 230.85106382978722], '20_15-20_45 220': [202.0, 0.6375, 138.25], '20_30-21_00 220': [110.0, 0.6931818181818182, 40.68181818181817], '20_45-21_15 220': [128.0, 0.696078431372549, 58.3921568627451], '21_00-21_30 220': [426.0, 0.6938775510204082, 356.61224489795916], '21_15-21_45 220': [318.0, 0.67, 251.0], '21_30-22_00 220': [216.0, 0.7083333333333334, 145.16666666666666], '21_45-22_15 220': [985.0, 0.7380952380952381, 911.1904761904761], '22_00-22_30 220': [608.0, 0.7192982456140351, 536.0701754385965], '22_15-22_45 220': [84.0, 0.6951219512195121, 14.487804878048792], '22_30-23_00 220': [119.0, 0.71, 48.0], '22_45-23_15 220': [198.0, 0.7358490566037735, 124.41509433962264], '23_00-23_30 220': [143.0, 0.7053571428571429, 72.46428571428571], '23_15-23_45 220': [320.0, 0.6625, 253.75], '23_30-00_00 220': [308.0, 0.7203389830508474, 235.96610169491527], '23_45-00_15 220': [418.0, 0.6931818181818182, 348.6818181818182]}

discretize(diff,temp_diff)
