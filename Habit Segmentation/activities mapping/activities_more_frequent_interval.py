import operator


def getInterval(pos):
        if pos == 0:
                interval = "00:00-00:15"
        elif pos == 1:
                interval = "00:15-00:30"
        elif pos == 2:
                interval = "00:30-00:45"
        elif pos == 3:
                interval = "00:45-01:00"
        elif pos == 4:
                interval = "01:00-01:15"
        elif pos == 5:
                interval = "01:15-01:30"
        elif pos == 6:
                interval = "01:30-01:45"
        elif pos == 7:
                interval = "01:45-02:00"
        elif pos == 8:
                interval = "02:00-02:15"
        elif pos == 9:
                interval = "02:15-02:30"
        elif pos == 10:
                interval = "02:30-02:45"
        elif pos == 11:
                interval = "02:45-03:00"
        elif pos == 12:
                interval = "03:00-03:15"
        elif pos == 13:
                interval = "03:15-03:30"
        elif pos == 14:
                interval = "03:30-03:45"
        elif pos == 15:
                interval = "03:45-04:00"
        elif pos == 16:
                interval = "04:00-04:15"
        elif pos == 17:
                interval = "04:15-04:30"
        elif pos == 18:
                interval = "04:30-04:45"
        elif pos == 19:
                interval = "04:45-05:00"
        elif pos == 20:
                interval = "05:00-05:15"
        elif pos == 21:
                interval = "05:15-05:30"
        elif pos == 22:
                interval = "05:30-05:45"
        elif pos == 23:
                interval = "05:45-06:00"
        elif pos == 24:
                interval = "06:00-06:15"
        elif pos == 25:
                interval = "06:15-06:30"
        elif pos == 26:
                interval = "06:30-06:45"
        elif pos == 27:
                interval = "06:45-07:00"
        elif pos == 28:
                interval = "07:00-07:15"
        elif pos == 29:
                interval = "07:15-07:30"
        elif pos == 30:
                interval = "07:30-07:45"
        elif pos == 31:
                interval = "07:45-08:00"
        elif pos == 32:
                interval = "08:00-08:15"
        elif pos == 33:
                interval = "08:15-08:30"
        elif pos == 34:
                interval = "08:30-08:45"
        elif pos == 35:
                interval = "08:45-09:00"
        elif pos == 36:
                interval = "09:00-09:15"
        elif pos == 37:
                interval = "09:15-09:30"
        elif pos == 38:
                interval = "09:30-09:45"
        elif pos == 39:
                interval = "09:45-10:00"
        elif pos == 40:
                interval = "10:00-10:15"
        elif pos == 41:
                interval = "10:15-10:30"
        elif pos == 42:
                interval = "10:30-10:45"
        elif pos == 43:
                interval = "10:45-11:00"
        elif pos == 44:
                interval = "11:00-11:15"
        elif pos == 45:
                interval = "11:15-11:30"
        elif pos == 46:
                interval = "11:30-11:45"
        elif pos == 47:
                interval = "11:45-12:00"
        elif pos == 48:
                interval = "12:00-12:15"
        elif pos == 49:
                interval = "12:15-12:30"
        elif pos == 50:
                interval = "12:30-12:45"
        elif pos == 51:
                interval = "12:45-13:00"
        elif pos == 52:
                interval = "13:00-13:15"
        elif pos == 53:
                interval = "13:15-13:30"
        elif pos == 54:
                interval = "13:30-13:45"
        elif pos == 55:
                interval = "13:45-14:00"
        elif pos == 56:
                interval = "14:00-14:15"
        elif pos == 57:
                interval = "14:15-14:30"
        elif pos == 58:
                interval = "14:30-14:45"
        elif pos == 59:
                interval = "14:45-15:00"
        elif pos == 60:
                interval = "15:00-15:15"
        elif pos == 61:
                interval = "15:15-15:30"
        elif pos == 62:
                interval = "15:30-15:45"
        elif pos == 63:
                interval = "15:45-16:00"
        elif pos == 64:
                interval = "16:00-16:15"
        elif pos == 65:
                interval = "16:15-16:30"
        elif pos == 66:
                interval = "16:30-16:45"
        elif pos == 67:
                interval = "16:45-17:00"
        elif pos == 68:
                interval = "17:00-17:15"
        elif pos == 69:
                interval = "17:15-17:30"
        elif pos == 70:
                interval = "17:30-17:45"
        elif pos == 71:
                interval = "17:45-18:00"
        elif pos == 72:
                interval = "18:00-18:15"
        elif pos == 73:
                interval = "18:15-18:30"
        elif pos == 74:
                interval = "18:30-18:45"
        elif pos == 75:
                interval = "18:45-19:00"
        elif pos == 76:
                interval = "19:00-19:15"
        elif pos == 77:
                interval = "19:15-19:30"
        elif pos == 78:
                interval = "19:30-19:45"
        elif pos == 79:
                interval = "19:45-20:00"
        elif pos == 80:
                interval = "20:00-20:15"
        elif pos == 81:
                interval = "20:15-20:30"
        elif pos == 82:
                interval = "20:30-20:45"
        elif pos == 83:
                interval = "20:45-21:00"
        elif pos == 84:
                interval = "21:00-21:15"
        elif pos == 85:
                interval = "21:15-21:30"
        elif pos == 86:
                interval = "21:30-21:45"
        elif pos == 87:
                interval = "21:45-22:00"
        elif pos == 88:
                interval = "22:00-22:15"
        elif pos == 89:
                interval = "22:15-22:30"
        elif pos == 90:
                interval = "22:30-22:45"
        elif pos == 91:
                interval = "22:45-23:00"
        elif pos == 92:
                interval = "23:00-23:15"
        elif pos == 93:
                interval = "23:15-23:30"
        elif pos == 94:
                interval = "23:30-23:45"
        elif pos == 95:
                interval = "23:45-00:00"
        
        return interval


activities = dict()
activities["Bed_to_Toilet"] = [0, 4, 10, 2, 1, 4, 3, 2, 1, 1, 3, 5, 5, 3, 12, 9, 10, 10, 12, 8, 12, 9, 13, 13, 9, 3, 1, 3, 3, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 2]
activities["Eating"] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 4, 7, 5, 6, 11, 7, 6, 2, 5, 18, 15, 19, 20, 21, 10, 8, 5, 6, 4, 4, 9, 5, 7, 5, 3, 3, 6, 9, 9, 5, 4, 3, 4, 3, 5, 7, 3, 3, 4, 8, 7, 7, 5, 2, 10, 16, 15, 12, 7, 9, 11, 8, 4, 7, 6, 4, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0]
activities["Enter_Home"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1, 3, 4, 1, 2, 2, 4, 5, 5, 3, 8, 7, 5, 10, 16, 14, 11, 12, 10, 5, 6, 4, 16, 23, 15, 18, 10, 16, 15, 36, 13, 6, 20, 7, 3, 8, 4, 7, 5, 6, 6, 8, 7, 9, 6, 5, 3, 3, 1, 2, 0, 1, 1, 0, 3, 0, 1, 1, 1, 0, 1, 2, 0, 0, 0]
activities["Housekeeping"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 4, 4, 5, 7, 5, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 4, 4, 4, 2, 2, 3, 2, 0, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
activities["Leave_Home"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 4, 8, 14, 15, 13, 10, 6, 3, 14, 6, 5, 8, 14, 9, 9, 17, 57, 11, 4, 6, 5, 5, 4, 6, 9, 8, 8, 10, 15, 24, 9, 4, 7, 10, 5, 6, 8, 8, 7, 5, 1, 5, 6, 9, 4, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
activities["Meal_Preparation"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 2, 6, 2, 5, 20, 24, 15, 32, 37, 21, 28, 48, 45, 49, 56, 43, 50, 53, 48, 54, 49, 46, 55, 49, 44, 37, 27, 21, 25, 21, 27, 37, 32, 24, 19, 21, 31, 41, 33, 37, 35, 33, 23, 23, 33, 36, 30, 36, 31, 37, 46, 51, 58, 51, 62, 69, 63, 68, 66, 59, 53, 46, 29, 29, 21, 4, 4, 4, 3, 2, 4, 5, 0, 3, 0, 0, 1, 1, 0]
activities["Relax"] = [84, 47, 32, 22, 17, 14, 13, 8, 7, 5, 3, 2, 3, 3, 1, 1, 1, 1, 3, 7, 8, 16, 26, 38, 44, 65, 71, 59, 45, 52, 58, 68, 73, 83, 82, 98, 100, 95, 82, 76, 69, 67, 54, 60, 59, 55, 59, 51, 63, 69, 87, 81, 79, 90, 94, 102, 113, 115, 122, 127, 117, 116, 116, 126, 127, 134, 135, 141, 144, 140, 148, 150, 146, 164, 179, 183, 193, 206, 210, 225, 229, 230, 226, 224, 225, 226, 222, 212, 211, 192, 194, 172, 163, 147, 131, 109]
activities["Resperate"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
activities["Sleeping"] = [151, 178, 199, 202, 205, 207, 210, 210, 214, 215, 221, 219, 220, 220, 226, 224, 225, 224, 224, 217, 217, 203, 197, 188, 172, 150, 140, 130, 113, 101, 87, 74, 59, 45, 30, 17, 6, 5, 5, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 4, 3, 2, 1, 1, 1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 3, 4, 7, 10, 12, 14, 22, 31, 47, 57, 64, 82, 98, 118]
activities["Wash_Dishes"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 5, 2, 1, 6, 3, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 3, 4, 1, 3, 2, 2, 3, 3, 6, 5, 3, 1, 2, 5, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]
activities["Work"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 3, 3, 5, 5, 3, 5, 3, 4, 3, 6, 6, 6, 6, 3, 5, 8, 7, 3, 4, 8, 6, 4, 6, 9, 9, 8, 8, 8, 3, 6, 6, 7, 10, 8, 5, 4, 8, 7, 13, 16, 13, 12, 7, 6, 8, 8, 8, 7, 4, 4, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 1]

for k in sorted(activities.keys()):
        print("*******************************************************************\n")
        print(k)
        maxVal = max(activities[k])
        maxInterval = getInterval(activities[k].index(maxVal))
        print("Max value is " + str(maxVal) + " in interval " + maxInterval)
        
        minVal = min(activities[k])
        minInterval = getInterval(activities[k].index(minVal))
        #print("Min value is " + str(minVal) + " in interval " + minInterval)

        meanVal = sum(activities[k])/96
        #print("Mean value is " + str(meanVal))

        if maxVal > 20:
                threshold = maxVal - maxVal * 60 / 100
        else:
                threshold = maxVal - maxVal * 50 / 100
        
        moreFrequentIntervals = []
        for i in range(len(activities[k])):
                if activities[k][i] > threshold:
                        moreFrequentIntervals.append(getInterval(i))

        #print(moreFrequentIntervals)

        moreFrequentIntervalsMerged = []
        moreFrequentIntervalsMerged.append(moreFrequentIntervals[0])
        j=0
        for i in range(len(moreFrequentIntervals)-1):
                firstInterval = moreFrequentIntervalsMerged[j].split("-")[1]
                
                if i==len(moreFrequentIntervals)-1:
                        lastInterval = moreFrequentIntervals[0]
                        lastIntervalStart = lastInterval.split("-")[0]

                else:
                        lastInterval = moreFrequentIntervals[i+1]
                        lastIntervalStart = lastInterval.split("-")[0]

                if firstInterval == lastIntervalStart:
                        moreFrequentIntervalsMerged[j] = moreFrequentIntervalsMerged[j].replace(firstInterval, lastInterval.split("-")[1])
                else:
                        j += 1
                        moreFrequentIntervalsMerged.append(moreFrequentIntervals[i+1])

        if moreFrequentIntervalsMerged[-1].split("-")[1] == moreFrequentIntervalsMerged[0].split("-")[0]:
                moreFrequentIntervalsMerged[0] = moreFrequentIntervalsMerged[0].replace(moreFrequentIntervalsMerged[0].split("-")[0], moreFrequentIntervalsMerged[-1].split("-")[0])
                moreFrequentIntervalsMerged.remove(moreFrequentIntervalsMerged[-1])
        #print(moreFrequentIntervalsMerged)

        string = ""
        for elem in moreFrequentIntervalsMerged:
                string += elem
                string += "\t"
        print("Activity is more frequent in the intervals " + string)



                        
                
                                             
