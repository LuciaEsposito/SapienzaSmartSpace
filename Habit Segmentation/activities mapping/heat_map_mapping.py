import os

activitiesName = ["Bed_to_Toilet", "Eating", "Enter_Home", "Housekeeping", "Leave_Home", "Meal_Preparation", "Relax", "Resperate", "Sleeping", "Wash_Dishes", "Work"]

inputPath = "output task" # activitiesName

activities = [0] * 96


def getSlot(starttime):
        if starttime >= "00:00:00" and starttime < "00:15:00":
                pos = 0
        elif starttime >= "00:15:00" and starttime < "00:30:00":
                pos = 1
        elif starttime >= "00:30:00" and starttime < "00:45:00":
                pos = 2
        elif starttime >= "00:45:00" and starttime < "01:00:00":
                pos = 3
        elif starttime >= "01:00:00" and starttime < "01:15:00":
                pos = 4
        elif starttime >= "01:15:00" and starttime < "01:30:00":
                pos = 5
        elif starttime >= "01:30:00" and starttime < "01:45:00":
                pos = 6
        elif starttime >= "01:45:00" and starttime < "02:00:00":
                pos = 7
        elif starttime >= "02:00:00" and starttime < "02:15:00":
                pos = 8
        elif starttime >= "02:15:00" and starttime < "02:30:00":
                pos = 9
        elif starttime >= "02:30:00" and starttime < "02:45:00":
                pos = 10
        elif starttime >= "02:45:00" and starttime < "03:00:00":
                pos = 11
        elif starttime >= "03:00:00" and starttime < "03:15:00":
                pos = 12
        elif starttime >= "03:15:00" and starttime < "03:30:00":
                pos = 13
        elif starttime >= "03:30:00" and starttime < "03:45:00":
                pos = 14
        elif starttime >= "03:45:00" and starttime < "04:00:00":
                pos = 15
        elif starttime >= "04:00:00" and starttime < "04:15:00":
                pos = 16
        elif starttime >= "04:15:00" and starttime < "04:30:00":
                pos = 17
        elif starttime >= "04:30:00" and starttime < "04:45:00":
                pos = 18
        elif starttime >= "04:45:00" and starttime < "05:00:00":
                pos = 19
        elif starttime >= "05:00:00" and starttime < "05:15:00":
                pos = 20
        elif starttime >= "05:15:00" and starttime < "05:30:00":
                pos = 21
        elif starttime >= "05:30:00" and starttime < "05:45:00":
                pos = 22
        elif starttime >= "05:45:00" and starttime < "06:00:00":
                pos = 23
        elif starttime >= "06:00:00" and starttime < "06:15:00":
                pos = 24
        elif starttime >= "06:15:00" and starttime < "06:30:00":
                pos = 25
        elif starttime >= "06:30:00" and starttime < "06:45:00":
                pos = 26
        elif starttime >= "06:45:00" and starttime < "07:00:00":
                pos = 27
        elif starttime >= "07:00:00" and starttime < "07:15:00":
                pos = 28
        elif starttime >= "07:15:00" and starttime < "07:30:00":
                pos = 29
        elif starttime >= "07:30:00" and starttime < "07:45:00":
                pos = 30
        elif starttime >= "07:45:00" and starttime < "08:00:00":
                pos = 31
        elif starttime >= "08:00:00" and starttime < "08:15:00":
                pos = 32
        elif starttime >= "08:15:00" and starttime < "08:30:00":
                pos = 33
        elif starttime >= "08:30:00" and starttime < "08:45:00":
                pos = 34
        elif starttime >= "08:45:00" and starttime < "09:00:00":
                pos = 35
        elif starttime >= "09:00:00" and starttime < "09:15:00":
                pos = 36
        elif starttime >= "09:15:00" and starttime < "09:30:00":
                pos = 37
        elif starttime >= "09:30:00" and starttime < "09:45:00":
                pos = 38
        elif starttime >= "09:45:00" and starttime < "10:00:00":
                pos = 39
        elif starttime >= "10:00:00" and starttime < "10:15:00":
                pos = 40
        elif starttime >= "10:15:00" and starttime < "10:30:00":
                pos = 41
        elif starttime >= "10:30:00" and starttime < "10:45:00":
                pos = 42
        elif starttime >= "10:45:00" and starttime < "11:00:00":
                pos = 43
        elif starttime >= "11:00:00" and starttime < "11:15:00":
                pos = 44
        elif starttime >= "11:15:00" and starttime < "11:30:00":
                pos = 45
        elif starttime >= "11:30:00" and starttime < "11:45:00":
                pos = 46
        elif starttime >= "11:45:00" and starttime < "12:00:00":
                pos = 47
        elif starttime >= "12:00:00" and starttime < "12:15:00":
                pos = 48
        elif starttime >= "12:15:00" and starttime < "12:30:00":
                pos = 49
        elif starttime >= "12:30:00" and starttime < "12:45:00":
                pos = 50
        elif starttime >= "12:45:00" and starttime < "13:00:00":
                pos = 51
        elif starttime >= "13:00:00" and starttime < "13:15:00":
                pos = 52
        elif starttime >= "13:15:00" and starttime < "13:30:00":
                pos = 53
        elif starttime >= "13:30:00" and starttime < "13:45:00":
                pos = 54
        elif starttime >= "13:45:00" and starttime < "14:00:00":
                pos = 55
        elif starttime >= "14:00:00" and starttime < "14:15:00":
                pos = 56
        elif starttime >= "14:15:00" and starttime < "14:30:00":
                pos = 57
        elif starttime >= "14:30:00" and starttime < "14:45:00":
                pos = 58
        elif starttime >= "14:45:00" and starttime < "15:00:00":
                pos = 59
        elif starttime >= "15:00:00" and starttime < "15:15:00":
                pos = 60
        elif starttime >= "15:15:00" and starttime < "15:30:00":
                pos = 61
        elif starttime >= "15:30:00" and starttime < "15:45:00":
                pos = 62
        elif starttime >= "15:45:00" and starttime < "16:00:00":
                pos = 63
        elif starttime >= "16:00:00" and starttime < "16:15:00":
                pos = 64
        elif starttime >= "16:15:00" and starttime < "16:30:00":
                pos = 65
        elif starttime >= "16:30:00" and starttime < "16:45:00":
                pos = 66
        elif starttime >= "16:45:00" and starttime < "17:00:00":
                pos = 67
        elif starttime >= "17:00:00" and starttime < "17:15:00":
                pos = 68
        elif starttime >= "17:15:00" and starttime < "17:30:00":
                pos = 69
        elif starttime >= "17:30:00" and starttime < "17:45:00":
                pos = 70
        elif starttime >= "17:45:00" and starttime < "18:00:00":
                pos = 71
        elif starttime >= "18:00:00" and starttime < "18:15:00":
                pos = 72
        elif starttime >= "18:15:00" and starttime < "18:30:00":
                pos = 73
        elif starttime >= "18:30:00" and starttime < "18:45:00":
                pos = 74
        elif starttime >= "18:45:00" and starttime < "19:00:00":
                pos = 75
        elif starttime >= "19:00:00" and starttime < "19:15:00":
                pos = 76
        elif starttime >= "19:15:00" and starttime < "19:30:00":
                pos = 77
        elif starttime >= "19:30:00" and starttime < "19:45:00":
                pos = 78
        elif starttime >= "19:45:00" and starttime < "20:00:00":
                pos = 79
        elif starttime >= "20:00:00" and starttime < "20:15:00":
                pos = 80
        elif starttime >= "20:15:00" and starttime < "20:30:00":
                pos = 81
        elif starttime >= "20:30:00" and starttime < "20:45:00":
                pos = 82
        elif starttime >= "20:45:00" and starttime < "21:00:00":
                pos = 83
        elif starttime >= "21:00:00" and starttime < "21:15:00":
                pos = 84
        elif starttime >= "21:15:00" and starttime < "21:30:00":
                pos = 85
        elif starttime >= "21:30:00" and starttime < "21:45:00":
                pos = 86
        elif starttime >= "21:45:00" and starttime < "22:00:00":
                pos = 87
        elif starttime >= "22:00:00" and starttime < "22:15:00":
                pos = 88
        elif starttime >= "22:15:00" and starttime < "22:30:00":
                pos = 89
        elif starttime >= "22:30:00" and starttime < "22:45:00":
                pos = 90
        elif starttime >= "22:45:00" and starttime < "23:00:00":
                pos = 91
        elif starttime >= "23:00:00" and starttime < "23:15:00":
                pos = 92
        elif starttime >= "23:15:00" and starttime < "23:30:00":
                pos = 93
        elif starttime >= "23:30:00" and starttime < "23:45:00":
                pos = 94
        elif starttime >= "23:45:00":
                pos = 95

        return pos


def create_dict():
        for filename in os.listdir(inputPath):
                f = open(os.path.join(inputPath,filename), "r")
                lines = f.readlines()
                starttime = lines[0].split("\t")[1].split(".")[0]
                endtime = lines[len(lines)-1].split("\t")[1].split(".")[0]
        
                posStart = getSlot(starttime)
                posEnd = getSlot(endtime)

                if posEnd >= posStart:
                        for i in range(posStart, posEnd+1):
                                activities[i] += 1
                else:
                        for i in range(posStart, 96):
                                activities[i] += 1
                        for i in range(0, posEnd+1):
                                activities[i] += 1
                f.close()                                
                
        print(activities)


create_dict()

# results
#activities = dict()
#activities["Bed_to_Toilet"] = [0, 4, 10, 2, 1, 4, 3, 2, 1, 1, 3, 5, 5, 3, 12, 9, 10, 10, 12, 8, 12, 9, 13, 13, 9, 3, 1, 3, 3, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 2]
#activities["Eating"] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 4, 7, 5, 6, 11, 7, 6, 2, 5, 18, 15, 19, 20, 21, 10, 8, 5, 6, 4, 4, 9, 5, 7, 5, 3, 3, 6, 9, 9, 5, 4, 3, 4, 3, 5, 7, 3, 3, 4, 8, 7, 7, 5, 2, 10, 16, 15, 12, 7, 9, 11, 8, 4, 7, 6, 4, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0]
#activities["Enter_Home"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1, 3, 4, 1, 2, 2, 4, 5, 5, 3, 8, 7, 5, 10, 16, 14, 11, 12, 10, 5, 6, 4, 16, 23, 15, 18, 10, 16, 15, 36, 13, 6, 20, 7, 3, 8, 4, 7, 5, 6, 6, 8, 7, 9, 6, 5, 3, 3, 1, 2, 0, 1, 1, 0, 3, 0, 1, 1, 1, 0, 1, 2, 0, 0, 0]
#activities["Housekeeping"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 4, 4, 5, 7, 5, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 4, 4, 4, 2, 2, 3, 2, 0, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#activities["Leave_Home"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 4, 8, 14, 15, 13, 10, 6, 3, 14, 6, 5, 8, 14, 9, 9, 17, 57, 11, 4, 6, 5, 5, 4, 6, 9, 8, 8, 10, 15, 24, 9, 4, 7, 10, 5, 6, 8, 8, 7, 5, 1, 5, 6, 9, 4, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#activities["Meal_Preparation"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 2, 6, 2, 5, 20, 24, 15, 32, 37, 21, 28, 48, 45, 49, 56, 43, 50, 53, 48, 54, 49, 46, 55, 49, 44, 37, 27, 21, 25, 21, 27, 37, 32, 24, 19, 21, 31, 41, 33, 37, 35, 33, 23, 23, 33, 36, 30, 36, 31, 37, 46, 51, 58, 51, 62, 69, 63, 68, 66, 59, 53, 46, 29, 29, 21, 4, 4, 4, 3, 2, 4, 5, 0, 3, 0, 0, 1, 1, 0]
#activities["Relax"] = [84, 47, 32, 22, 17, 14, 13, 8, 7, 5, 3, 2, 3, 3, 1, 1, 1, 1, 3, 7, 8, 16, 26, 38, 44, 65, 71, 59, 45, 52, 58, 68, 73, 83, 82, 98, 100, 95, 82, 76, 69, 67, 54, 60, 59, 55, 59, 51, 63, 69, 87, 81, 79, 90, 94, 102, 113, 115, 122, 127, 117, 116, 116, 126, 127, 134, 135, 141, 144, 140, 148, 150, 146, 164, 179, 183, 193, 206, 210, 225, 229, 230, 226, 224, 225, 226, 222, 212, 211, 192, 194, 172, 163, 147, 131, 109]
#activities["Resperate"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#activities["Sleeping"] = [151, 178, 199, 202, 205, 207, 210, 210, 214, 215, 221, 219, 220, 220, 226, 224, 225, 224, 224, 217, 217, 203, 197, 188, 172, 150, 140, 130, 113, 101, 87, 74, 59, 45, 30, 17, 6, 5, 5, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 4, 3, 2, 1, 1, 1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 3, 4, 7, 10, 12, 14, 22, 31, 47, 57, 64, 82, 98, 118]
#activities["Wash_Dishes"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 5, 2, 1, 6, 3, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 3, 4, 1, 3, 2, 2, 3, 3, 6, 5, 3, 1, 2, 5, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]
#activities["Work"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 3, 3, 5, 5, 3, 5, 3, 4, 3, 6, 6, 6, 6, 3, 5, 8, 7, 3, 4, 8, 6, 4, 6, 9, 9, 8, 8, 8, 3, 6, 6, 7, 10, 8, 5, 4, 8, 7, 13, 16, 13, 12, 7, 6, 8, 8, 8, 7, 4, 4, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 1]


