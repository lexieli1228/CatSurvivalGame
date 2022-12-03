cSBeginningTextPath = "./catSurvivalBeginning.txt"
cSGuideTextPath = "./catSurvivalGuide.txt"

def cSIntroductionPrintFunc():
    cSBeginning = open(cSBeginningTextPath, 'r', encoding='utf8')
    cSBeginningLines = cSBeginning.readlines()
    cSBeginning.close()

    cSGuide = open(cSGuideTextPath, 'r', encoding='utf8')
    cSGuideLines = cSGuide.readlines()
    cSGuide.close()

    # 前导词
    for i in range(len(cSBeginningLines)):
        print(cSBeginningLines[i])
        if i < 2:
            cSContinue = input(cSGuideLines[0])
            while cSContinue != "":
                cSContinue = input(cSGuideLines[0])
        else:
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")