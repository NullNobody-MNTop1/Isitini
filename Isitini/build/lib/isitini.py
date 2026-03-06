from time import sleep as s

def Intis(num, mes, inputmes, sendBool = False, useMessage = True, timer = 0.0):
    while True:
        try:
            num = int(num)
            if sendBool:
                return True
            else:
                return num
        except ValueError:
            if not sendBool:
                if useMessage:
                    print(mes)
                    s(timer)
                num = input(inputmes)
            else:
                return False

def Floatis(num, mes, inputmes, sendBool = False, useMessage = True, timer = 0.0):
    while True:
        try:
            num = float(num)
            if sendBool:
                return True
            else:
                return num
        except ValueError:
            if not sendBool:
                if useMessage:
                    print(mes)
                    s(timer)
                num = input(inputmes)
            else:
                return False
            
def Stris(num, mes, inputmes, sendBool = False, useMessage = True, timer = 0.0):
    while True:
        try:
            num = float(num)
            if not sendBool:
                if useMessage:
                    print(mes)
                    s(timer)
                num = input(inputmes)
            else:
                return False
        except ValueError:
            if sendBool:
                return True
            else:
                return num
            
def Boolis(num, mes, inputmes, sendBool = False, useMessage = True, timer = 0.0):
    while True:
        try:
            num = bool(num)
            if sendBool:
                return True
            else:
                return num
        except ValueError:
            if not sendBool:
                if useMessage:
                    print(mes)
                    s(timer)
                num = input(inputmes)
            else:
                return False