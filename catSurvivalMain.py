import catSurvivalIntroduction as cIntroduction
import catSurvivalIndoors as cIndoors
import catSurvivalWheatField as cField
import catSurvivalValley as cValley

import random as rand

# 0：室内，1：麦田，2：山谷（未选择）
cIndoorPragma = 0
cOutdoorsPragma = 1
cFieldPragma = 2
cValleyPragma = 3

# 从第三天开始游戏，初始状态在室内
cSkills = 0
cStrength = 80  
cDayCnt = 3
cSurvival = 1
cPlace = cIndoorPragma 
cSubPlace = 0

cIntroduction.cSIntroductionPrintFunc()

def cSGameOver():
    print("游戏结束。防沉迷防上瘾（作者求生）")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("灵感来源：")
    print("北京大学2022年秋季学期《舌尖上的植物学》课程")
    print("单机游戏\"终结的世界与你和我\"")

def cSGame():
    global cPlace
    global cSurvival
    global cDayCnt
    while cSurvival == 1:
        # 室内
        if cPlace == cIndoorPragma:
            currPlace, currStatus, currDay = cIndoors.cSIndoorMain(cSDayCnt=cDayCnt, cSStrength=cStrength, cSSkills=cSkills)
            cPlace = currPlace
            cSurvival = currStatus
            cDayCnt = currDay
        # 麦田
        elif cPlace == cFieldPragma:
            print("field here!")
            return
        # 山谷
        elif cPlace == cValleyPragma:
            print("valley here!")
            return
    cSGameOver()

cSGame()