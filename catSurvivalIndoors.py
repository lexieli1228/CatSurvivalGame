import random as rand
import math

# 猫的生存参数
cSIDayCnt = -1
cSIStrength = -1
cSISkills = -1
cSISurvival = 1

# 场景参数
cSIIndoorPragma = 0
cSIOutdoorsPragma = 1
cSIFieldPragma = 2
cSIValleyPragma = 3

# 冰箱中食物的存量和打开状态
cSIFridgeState = 0
cSIChocolate = 2
cSICoffee = 2
cSIMilk = 10
cSIRaisin = 5
cSIChicken = 10
cSIFridgeFoodCnt = 29

# 猫目前进食状态
cSICurrChocolateDay = 0
cSICurrCoffeeDay = 0
cSICurrMilkDay = 0
cSICurrRaisinDay = 0
cSICurrChickenDay = 0

# 猫的特性
cSIMilkAllergy = -1

# 猫薄荷数量和食用状态
cSICatnip = 10
cSICurrCatnipDay = 0

# 打印结束状态
def cSIIndoorGameOver():
    global cSISurvival
    if cSIDayCnt >= 15 and cSISurvival == 1:
        print("早晨，门被敲响")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你抬起了头")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("是主人！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你活了！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("结局：苟王")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
    else:
        print("你死了")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("R.I.P.")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
    cSISurvival = 0
    return

# 每日场景的第二个选择
def cSIDaySecondChoice():
    global cSIStrength
    print("你尝试了一下，凭借平时的观察和聪明的头脑，你成功打开了窗户，但耗费了不少体力")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    cSIStrength -= 10
    print("你的体力值现在变成了{}".format(cSIStrength))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("看起来这已经是城市的边界了，街道上寂静无人，城市的远方就是户外")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你敏感的神经意识到这里不安全，你的动物本能促使你向远方进发")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你蹑手蹑脚地潜行，到达了边界，一边是麦田，一遍是山谷")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("天色逐渐破晓，现在，看起来你想悄无声息地回去也不太可能了。你决定做出一个选择")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你如何选择？")
    print("A.麦田")
    print("B.山谷")
    cSContinue = input("请选择：\n")
    while cSContinue != "A" and cSContinue != "a" and cSContinue != "B" and cSContinue != "b":
        cSContinue = input("请做出有效选择！\n")
    if cSContinue == "A" or cSContinue == "a":
        return cSIFieldPragma
    else:
        return cSIValleyPragma

# 每日场景的第一个选择
def cSIDayInfoChoice():
    print("今天是自力更生的第{}天".format(cSIDayCnt))
    print("你的体能值：{}".format(cSIStrength))
    print("你的技能值：{}".format(cSISkills))
    print("你如何选择？")
    print("A.扒开窗户看看，试着跳出")
    print("B.留在屋内，探索一下")
    cSContinue = input("请选择：\n")
    while cSContinue != "A" and cSContinue != "a" and cSContinue != "B" and cSContinue != "b":
        cSContinue = input("请做出有效选择！\n")
    if cSContinue == "B" or cSContinue == "b":
        return cSIIndoorPragma
    else:
        return cSIDaySecondChoice()

# 食用猫粮，每天的体力值会衰减 9，因为食物根本不够
def cSICatFood():
    global cSIStrength
    global cSISkills
    global cSISurvival
    global cSICurrCatnipDay
    cSICurrCatnipDay = 0
    cSIStrength -= 9
    if cSIStrength < 30:
        cSISurvival = 0
    print("你决定食用猫粮，尽管食物并不是很充足")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("由于食物过于匮乏")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的体力值现在变成了{}".format(cSIStrength))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")

# 食用鸡腿，连续吃三天后会盐超标，需要食用牛奶解渴
def cSIEatChicken():
    global cSIChicken
    global cSICurrChickenDay
    global cSIFridgeFoodCnt
    global cSISurvival
    global cSIStrength
    global cSICurrCatnipDay
    cSICurrCatnipDay = 0
    
    cSICurrChickenDay += 1
    cSIChicken -= 1
    cSIFridgeFoodCnt -= 1
    
    # 盐超标
    if cSICurrChickenDay >= 3:
        print("你吃了鸡腿")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但这让你感觉很不好")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你感到极力的口渴")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你体内的盐含量发生了超标")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSIStrength -= 10
        print("盐超标又没有合适的水源让你非常焦躁")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你的体力在进行迅速下降")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你的体力值现在变成了{}".format(cSIStrength))
        if cSIStrength <= 30:
            cSISurvival = 0
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你的极度缺水让你恍惚")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("昏沉的大脑让你本能地靠近水源，可是这屋内没有任何饮用水")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("即使有，也没有力气找了吧")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你摇摇晃晃")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你的视线变得模糊......")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            return
    
    # 前两天吃    
    print("你吃了鸡腿")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("但感觉怪怪的")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("好在是不饿了")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("但还是没什么精神。")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的体力值没有任何变化")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    return

# 食用牛奶，有50%可能触发不耐受，极大减少体力值
def cSIEatMilk():
    global cSIMilk
    global cSICurrMilkDay
    global cSICurrChickenDay
    global cSIFridgeFoodCnt
    global cSISurvival
    global cSIStrength
    global cSIMilkAllergy
    global cSICurrCatnipDay
    cSICurrCatnipDay = 0
    
    cSICurrChickenDay = 0
    cSICurrMilkDay += 1
    cSIMilk -= 1
    cSIFridgeFoodCnt -= 1
    
    if cSIMilkAllergy == -1:
        possibility = rand.randint(0, 2)
        cSIMilkAllergy = possibility % 2
    
    # 耐受
    if cSIMilkAllergy:
        print("你喝了一口")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("虽然口感有些奇怪")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但确实是能喝的东西")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        if cSICurrChickenDay > 0:
            cSICurrChickenDay = 0
            print("你食用鸡肉带来的口渴一扫而光")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            cSIStrength += 8
            print("你的体力得到了增长，变成了{}".format(cSIStrength))
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
        cSIStrength += 10
        print("你的体力得到了增长，变成了{}".format(cSIStrength))
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        return
    # 不耐受
    else:
        print("你喝了一口")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你隐隐约约感觉肚子里翻江倒海")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("这种感觉愈演愈烈")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        if cSICurrMilkDay > 2:
            cSISurvival = 0
            print("你又喝了一口")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            return
        print("但起码肚子里是有点东西，但在隐隐作痛，这让你感觉一般")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("不幸的是你变得虚弱了")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSIStrength -= 2
        if cSIStrength <= 30:
            print("你实在是过于虚弱")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你的视线变得模糊...")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
        return

# 食用葡萄干，引发肾衰，极大减少体力值，食用两次之后必死亡
def cSIEatRaisin():
    global cSIRaisin
    global cSICurrRaisinDay
    global cSICurrChickenDay
    global cSIFridgeFoodCnt
    global cSISurvival
    global cSIStrength
    global cSICurrCatnipDay
    cSICurrCatnipDay = 0
    cSIRaisin -= 1
    cSIFridgeFoodCnt -= 1
    cSICurrRaisinDay += 1
    print("你吃了一点")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("看起来无大碍")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的精神好了一些")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("破晓")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你觉得你在脱水")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你非常难受")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    cSIStrength -= 15
    print("你毫无办法，体力值降低了不少，变成了{}".format(cSIStrength))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    if cSIStrength < 30:
        print("你开始悔恨自己为什么要尝试这种东西")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但这种强烈的意识也在逐渐消失")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你很想活着")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但这时驱除肉体的痛苦貌似更着急")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("幸好，你的痛苦在逐渐消失，但你的意识也变得模糊")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSISurvival = 0
        return
    if cSICurrRaisinDay == 2:
        cSISurvival = 0
        print("你越来越难受")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你的精神在逐渐被削弱")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你想，这东西是有毒的")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("可是你并不知道，这不怪你")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但说什么也都没有用了吧......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
    return

# 食用巧克力或咖啡豆，必死无疑
def cSIEatChocolateOrCoffee():
    global cSIFridgeFoodCnt
    global cSISurvival
    global cSIStrength
    global cSICurrCatnipDay
    cSICurrCatnipDay = 0
    cSIFridgeFoodCnt -= 1
    print("你吃了一点")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("看起来无大碍")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的精神好了一些")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("突然")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你开始剧烈地呕吐")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("躺在地上挣扎")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    cSIStrength -= 60
    print("你毫无办法，体力值降低了不少，变成了{}".format(math.max(0, cSIStrength)))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    if cSIStrength < 30:
        print("你开始悔恨自己为什么要尝试这种东西")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但这种强烈的意识也在逐渐消失")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你很想活着")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但这时驱除肉体的痛苦貌似更着急")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("幸好，你的痛苦在逐渐消失，但你的意识也变得模糊")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSISurvival = 0
        return

# 冰箱里选食物
def cSIFridgeFoodChoice():
    global cSIStrength
    global cSISkills
    global cSISurvival
    global cSIChocolate
    global cSICoffee
    global cSIMilk
    global cSIRaisin
    global cSIChicken
    
    print("你发现了一些食物和饮品")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你并分不清里面大部分都是什么，大概都是主人吃的东西吧")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    
    if cSIChicken > 0:
        print("你发现了鸡腿，虽然看起来并不是给猫吃的")
    if cSIMilk > 0:
        print("你发现了某种奶制品，虽然闻起来味道有些奇怪")
    if cSIRaisin > 0:
        print("你发现了一些奇怪的颗粒，仿佛是什么水果的干")
    if cSIChocolate > 0:
        print("你发现了一些板状的固体食物，散发着有些诱人的混合气，你仔细闻了闻")
    if cSICoffee > 0:
        print("你发现了一些豆子，气味同样的诱人")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("饥肠辘辘，你打算探索新的食物")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("请你选择：")
    print("A.鸡腿")
    print("B.某种奶制品")
    print("C.尝试一下类似于水果干的颗粒")
    print("D.啃一口板状的固体食物，一旦能吃了就能撑很久")
    print("E.尝试一下豆子，如果能吃的话就能撑很久")
    cSContinue = input("请选择你今天的食物：\n")
    fridgeChoiceState = 0
    while fridgeChoiceState == 0:
        while cSContinue != "A" and cSContinue != "a" and cSContinue != "B" and cSContinue != "b" and cSContinue != "C" and cSContinue != "c" and cSContinue != "D" and cSContinue != "d" and cSContinue != "E" and cSContinue != "e":
            cSContinue = input("请做出有效选择！\n")
        # 鸡腿
        if cSContinue == "A" or cSContinue == "a":
            if cSIChicken > 0:
                fridgeChoiceState = 1
                cSIEatChicken()
            else:
                print("你发现这种食物被你吃光了，需要进行有效选择")
        # 奶制品
        elif cSContinue == "B" or cSContinue == "b":
            if cSIMilk > 0:
                fridgeChoiceState = 1
                cSIEatMilk()
            else:
                print("你发现这种食物被你吃光了，需要进行有效选择")
        # 水果干
        elif cSContinue == "C" or cSContinue == "c":
            if cSIRaisin > 0:
                fridgeChoiceState = 1
                cSIEatRaisin()
                return
            else:
                print("你发现这种食物被你吃光了，需要进行有效选择")
        # 巧克力
        elif cSContinue == "D" or cSContinue == "d":
            if cSIChocolate > 0:
                fridgeChoiceState = 1
                cSIEatChocolateOrCoffee()
                return
            else:
                print("你发现这种食物被你吃光了，需要进行有效选择")
        # 咖啡豆
        else:
            if cSICoffee > 0:
                fridgeChoiceState = 1
                cSIEatChocolateOrCoffee()
                return
            else:
                print("你发现这种食物被你吃光了，需要进行有效选择")

# 尝试打开冰箱
def cSIFridge():
    global cSIStrength
    global cSISkills
    global cSISurvival
    global cSIFridgeState
    # 冰箱已经被打开
    if cSIFridgeState != 0:
        cSIFridgeFoodChoice()
        return 
    
    # 打开冰箱
    cSIStrength -= 10
    cSISkills += 10
    cSIFridgeState = 1
    
    if cSIStrength < 30:
        cSISurvival = 0
        print("你尝试开了一下冰箱，但虚弱的你毫无办法")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你尝试跳高，可距离能用力把冰箱打开的距离还有一点")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你的视线变得模糊......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        return
   
    print("你拼尽全力，跳到了合适的高度，扒开了冰箱")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的体力值现在变成了{}".format(cSIStrength))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的技能值现在变成了{}".format(cSISkills))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("好欸！主人确实有一些囤货")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("你的体力值现在变成了{}".format(cSIStrength))
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("") 
    cSIFridgeFoodChoice()

# 选择今日吃草
def cSIPlant():
    global cSIStrength
    global cSISkills
    global cSISurvival
    global cSICatnip
    global cSICurrCatnipDay
    cSICatnip -= 1
    cSICurrCatnipDay += 1
    
    # 连续吃了太多猫薄荷，精神恍惚而亡
    if cSICurrCatnipDay >= 4:
        print("你吃了太多猫薄荷")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("它让你飘飘欲仙")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但你太久没有正常进食了...")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("今朝有酒今朝醉")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("这种情况下你也想不到太多")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("猫薄荷让你陷入了混沌")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但仿佛逐渐饥饿的感觉也没有了...")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("恍惚中，你好像回到了自己是一只小猫的时候")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("主人第一次拿猫薄荷给你，你兴奋地蹭着")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你多开心啊...")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSISurvival = 0
        print("......")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        return
    print("......")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    possibility = rand.randint(0, 2)
    # 上蹿下跳，消耗体力
    if possibility % 1:
        print("你陷入了兴奋")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你一点都不感觉饿了！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你获得了无上的力量！！！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你是方圆n里最威猛的大侠！！！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你是方圆n里最威猛的大侠！！！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("哈！！！")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("你上蹿下跳，消耗了一些体力")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSIStrength -= 5
        print("你的体力变成了{}".format(cSIStrength))
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        if cSIStrength <= 30:
            cSISurvival = 0
            print("但好像，你努力跳，也没办法跳起来了")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("猫薄荷的亢奋让你扭动")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你逐渐大脑一片空白，失去了意识......")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
        return
    # 昏睡
    else:
        print("你飘飘欲仙")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("嘴里咀嚼着，沉寂中昏睡")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("没有摄食其他食物，你的体力值在下降")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        print("但睡眠让你感觉良好")
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        cSIStrength -= 1
        print("你的体力变成了{}".format(cSIStrength))
        cSContinue = input("")
        while cSContinue != "":
            cSContinue = input("")
        if cSIStrength <= 30:
            cSISurvival = 0
            print("你觉得冷起来了")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
            print("你逐渐大脑一片空白，失去了意识......")
            cSContinue = input("")
            while cSContinue != "":
                cSContinue = input("")
        return 

# 室内逻辑    
def cSIIndoorLogic():
    global cSIFridgeFoodCnt
    global cSICatnip
    print("处于对环境的熟悉，你留在了室内")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("饥肠辘辘，你决定找一些食物")
    cSContinue = input("")
    while cSContinue != "":
        cSContinue = input("")
    print("摆在你面前有三个选择：")
    print("A.继续食用之前的猫粮")
    print("B.尝试打开冰箱")
    print("C.探索家里的植物")
    cSContinue = input("请选择：\n")
    indoorChoiceState = 0
    while indoorChoiceState == 0:
        while cSContinue != "A" and cSContinue != "a" and cSContinue != "B" and cSContinue != "b" and cSContinue != "C" and cSContinue != "c":
            cSContinue = input("请做出有效选择！\n")
        if cSContinue == "A" or cSContinue == "a":
            indoorChoiceState = 1
            cSICatFood()
        elif cSContinue == "B" or cSContinue == "b":
            if cSIFridgeFoodCnt > 0:
                indoorChoiceState = 1
                cSIFridge()
            else:
                print("可惜的是，冰箱里的食物已经被吃光了")
        else:
            indoorChoiceState = 1
            if cSICatnip > 0:
                cSIPlant()
            else:
                print("可惜的是，没有植物供你进行啃食")
        return

def cSIndoorMain(cSDayCnt, cSStrength, cSSkills):
    global cSIDayCnt
    global cSIStrength
    global cSISkills
    global cSISurvival
    cSIDayCnt = cSDayCnt
    cSIStrength = cSStrength
    cSISkills = cSSkills
    
    while cSISurvival == 1:
        currPlace = cSIDayInfoChoice()
        #已经跳到室外
        if currPlace != cSIIndoorPragma:
            return currPlace, cSISurvival, cSIDayCnt
        #留在室内
        cSIIndoorLogic()
        cSIDayCnt += 1
        #在室内到了第15天
        if cSIDayCnt == 15:
            cSIIndoorGameOver()
    cSIIndoorGameOver()
    return currPlace, cSISurvival, cSIDayCnt