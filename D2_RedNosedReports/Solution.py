noOfSafeLevels = 0

def CheckSafety(levels):
    #are levels increasing
    levelsDec = all(int(levels[i]) >= int(levels[i + 1]) for i in range(len(levels) - 1))
    #are levels decreasing
    levelsInc = all(int(levels[i]) <= int(levels[i + 1]) for i in range(len(levels) - 1))
    #is the difference between levels at most 3
    levelDiff3 = all(abs(int(levels[i]) - int(levels[i+1])) <= 3 for i in range(len(levels) - 1) )
    #is the difference between levels at least 1
    levelDiff1 = all(abs(int(levels[i]) - int(levels[i+1])) >= 1 for i in range(len(levels) - 1) )
    if(levelsDec or levelsInc):
        if( levelDiff3 and levelDiff1):
            return True        
    return False


#Open and read input
with open('input.txt','r') as reports:
    for report in reports:
        #isReportSafe = False
        levels = report.split()
        if (CheckSafety(levels)):
            noOfSafeLevels += 1
reports.close()
print(noOfSafeLevels)

###############################################################################################################
#part2

newNoOfSafeLevels = 0

with open('input.txt','r') as reports:
    for i,report in enumerate(reports):
        isReportSafe = False
        levels = report.split()
        if (CheckSafety(levels)):
            newNoOfSafeLevels += 1
            isReportSafe = True
        else:
            for index,level in enumerate(levels):
                levels.pop(index)
                if(CheckSafety(levels)):
                    newNoOfSafeLevels += 1
                    isReportSafe = True
                    break
                else:
                    levels.insert(index,level)
    reports.close()
    print(newNoOfSafeLevels)    