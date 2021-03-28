from os import listdir
from os.path import isfile, join, split

inputDir = "./IP"
outputDir = "./OP"

fileList = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]

for fileName in fileList:
    inputFile = open(join(inputDir, fileName),"r")
    readText = inputFile.readlines()
    inputFile.close()

    print("Finished Reading File no. " + str(fileList.index(fileName)) + " : " + str(join(inputDir, fileName)))
    print("Writing File no. " + str(fileList.index(fileName)) + " : " + str(join(outputDir, fileName)))

    outputFile = open(join(outputDir, fileName),"a")

    processedText = ["|Name|Type|Value|Description|\n","|:---|:---|:---|:---|\n"]

    for line in readText:
        if(readText.index(line) == 0):
            outputFile.write(processedText[0])
        elif(readText.index(line) == 1):
            outputFile.write(processedText[1])
        elif(readText.index(line) > 1 and line.find("dummy8")==-1):            
            unProcessedLine = line.split("|")
            del unProcessedLine[0]

            if(unProcessedLine[2] == '' and unProcessedLine[3] != ''):
                unProcessedLine[2] = '[' + unProcessedLine[3] + ']'            

            elif(unProcessedLine[2] != '' and unProcessedLine[3] != ''):
                unProcessedLine[2] = unProcessedLine[2] + ' [' + unProcessedLine[3] + ']'

            del unProcessedLine[3]
            processedLine = '|'+unProcessedLine[0]+'|'+unProcessedLine[1]+'|'+unProcessedLine[2]+'|'+unProcessedLine[3]+'|'+unProcessedLine[4]
            outputFile.write(processedLine)
    outputFile.close()
    
    print("Finished writing File no. " + str(fileList.index(fileName)) + " : " + str(join(outputDir, fileName)))


