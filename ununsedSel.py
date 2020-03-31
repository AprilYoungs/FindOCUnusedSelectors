import os
import re

#scan all the possible unused Objective-C selector

outPath = "./TestData/export" #result export directory
machOFilePath = "./TestData/TestDemo" #executable-file
linkmapPath = "./TestData/TestDemo-linkMap.txt" #linkMap.txt

# selectors to ignore from scan
ignoreMeths = [".cxx_destruct", ".cxx_construct"]
# prefix of your module, if you want to scan all module, set this to ""
prefix = "AY"


# [+|-]\[{}.*\]
# [+-]\[{}[a-zA-Z]\w*\s[\w:]+\]
methodPattern = re.compile('[+-]\[{}[a-zA-Z]\w*\s[\w:]+\]'.format(prefix))
def getLinkmapSymbols(linkpath):
    """
    Find all the Objective-C selector from linkMap,
    And return the selectors as a list
    """
    reachFiles = False
    reachSymbols = False
    reachSections = False
    fileMap = {}
    symoblList = []
    linkfile = open(linkpath, 'r',encoding="macroman")
    for line in linkfile.readlines():
        if line.startswith("#",0,len(line)):
            if "# Object files:" in line:
                reachFiles = True
            elif "# Sections:" in line:
                reachSections = True
            elif "# Symbols:" in line:
                reachSymbols = True
        else:
            if reachFiles == True and reachSections == False and reachSymbols == False :
                line = line.replace("\n","")
                index = line.find("]",0,len(line))
                if index != -1 :
                    ofilePath = line[index+2:]
                    oIndex = line[:index+1]
                    fileMap[oIndex] = ofilePath
            elif reachFiles == True and reachSections == True and reachSymbols == True :
                    symbolsArray = line.split("\t")
                    if len(symbolsArray) == 3 :
                        fileKeyAndName = symbolsArray[2]
                        symbolSize = int(symbolsArray[1],16)

                        fileKeyAndName = fileKeyAndName.replace("\n","")
                        index = fileKeyAndName.find("]",0,len(line))
                        if index != -1 :
                            oIndex = fileKeyAndName[:index+1]
                            symoblPart = methodPattern.findall(fileKeyAndName)
                            if len(symoblPart) > 0:
                                method = symoblPart[0]
                                symoblList.append(method)
                            
    linkfile.close()
    return symoblList

if os.path.isdir(outPath) == False:
    os.makedirs(outPath)

# export referenced(used) selectors to file
selrefsFile =  outPath+"/selrefs.txt" #referenced selectors
cmd = "otool -v -s __DATA __objc_selrefs "+ machOFilePath +" > "+selrefsFile
os.system(cmd)

selall = getLinkmapSymbols(linkmapPath)


# load used selectors
selrefsF = open(selrefsFile,encoding="utf8", errors='ignore')
selrefsList = []
pattern = "__objc_methname:"
length = len(pattern)
for line in selrefsF.readlines():
    index = line.find(pattern)
    if index != -1:
        method = line[index+length:-1]
        selrefsList.append(method)

selrefsF.close()   

output = open(outPath+"/Selectors.csv", 'w')
output.write("IsUsed, Methods\n")
for sel in selall:
    print("scanning... {0}".format(sel))
    selMth = sel
    selMth = selMth.replace("+",'')
    selMth = selMth.replace("-",'')
    selMth = selMth.replace("[",'')
    selMth = selMth.replace("]",'')
    selL = selMth.split(" ")
    if ignoreMeths.count(selL[1]) > 0:
        continue
    selMth = selL[1]
    isUse = False
    for selref in selrefsList:
        if  selref == selMth:
            isUse = True
            break 
    if not isUse:
        print("🤨unused...{0}".format(sel))
        output.write("{},{}\n".format(isUse, sel))
    else:
        output.write("{},{}\n".format(isUse, sel))
     
output.close()
print("Finished.\n File save to {}/Selectors.csv".format(outPath))
