from inStock import inStock
from poApplication import poApplication
from poInventoryBld import poInventoryBld
from poTransferOut import poTransferOut
from poInventorySum import poInventorySum
from poOutClinic import poOutClinic
from poReaction import poReaction
from poScrap import poScrap
from poTransferIn import poTransferIn
while True:
    Interface = int(input("请选择相应的接口：\n"
                 "1、inStock\n"
                 "2、poApplication\n"
                 "3、poInventoryBld\n"
                 "4、poInventorySum\n"
                 "5、poOutClinic\n"
                 "6、poReaction\n"
                 "7、poScrap\n"
                 "8、poTransferIn\n"
                 "9、poTransferOut\n"
                 "请输入您的选择："))
    if Interface == 1:
        inStock()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 2:
        poApplication()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 3:
        poInventoryBld()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 4:
        poInventorySum()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 5:
        poOutClinic()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 6:
        poReaction()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 7:
        poScrap()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 8:
        poTransferIn()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    elif Interface == 9:
        poTransferOut()
        E = input("按N退出，任意键继续.")
        if E == "N":
            break
    else:
        print("您选择的接口不存在.")
        E = input("按N退出，任意键继续.")
        if E == "N":
            break


