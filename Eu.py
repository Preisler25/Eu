class Orszagok:
    def __init__(self, list):
        self.nev = list[0]
        self.join_date = list[1]
        self.join_y = int(list[1].split(".")[0])
        self.join_m = int(list[1].split(".")[1])
        self.join_d = int(list[1].split(".")[2])

def makingObjects():
    list = []
    temp = ImportFormTXT()
    for i in temp:
        list.append(Orszagok(i.split(";")))
    return list

def ImportFormTXT():
    f = open("Eucsatlakozas.txt", "r", encoding="UTF8").read()
    lines = f.split("\n")
    return lines

def formatDM(map):
    temp = f"{map}"
    temp = temp[1:-1]
    temp = temp
    temp = temp.split(",")
    for i in temp:
        temp_y = i.split(":")[0].strip()
        temp_num = i.split(":")[1].strip()
        print(f"\t{temp_y} - {temp_num} ország")


def feladat4(list):
    temp = 0
    for i in list:
        if i.join_y == 2007:
            temp += 1
    return temp

def feladat5(list):
    for i in list:
        if i.nev == "Magyarország":
            return i.join_date

def feladat6(list):
    for i in list:
        if i.join_m == 5:
            return "volt"
    return "nem volt"

def feladat7(list):
    temp = list[0]
    for i in list:
        if temp.join_y < i.join_y or temp.join_y == i.join_y and temp.join_m < i.join_m or temp.join_y == i.join_y and temp.join_m == i.join_m and temp.join_d < i.join_d:
            temp = i
    return temp.nev

def feladat8(list):
    date_map = dict()
    for i in list:
        if i.join_y in date_map:
            date_map[i.join_y] += 1
        else:
            date_map[i.join_y] = 1
    formatDM(date_map)

def main():
    orszag_list = makingObjects()
    print(f"3.feladat: Az Eu tagállamainak száma: {len(orszag_list)} db")
    print(f"4.feladat: 2007-ben {feladat4(orszag_list)} orszag csatlakozott.")
    print(f"5.feladat: Magyar ország csatlakozásának dátuma: {feladat5(orszag_list)}")
    print(f"6.feladat: Májusban {feladat6(orszag_list)} csatlakozás!")
    print(f"7.feladat: Legutoljára csatlakozott ország: {feladat7(orszag_list)}")
    print(f"8.feladat: Statisztika")
    feladat8(orszag_list)
main()