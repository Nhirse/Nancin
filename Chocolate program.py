List1=["b1","g2","r3","b4","g5"]
List2=["g1","b2","r3","b5","r6","g7"]
List3=["r1", "b9", "g3", "r4", "r5", "g6", "b7"]


def move_to_1(list):
    for i in range(0, len(list)):
        print(list[i][0:1])
        if list[i][0:1] == "r":
            globals()["List1"].append(list[i])
            globals()[list].remove(list[i])
        if list[i][0:1] == "b":
            globals()["List2"].append(list[i])
            globals()[list].remove(list[i])
        if list[i][0:1] == "g":
            globals()["List3"].append(list[i])
            globals()[list].remove(list[i])


move_to_1(List1)
print(List1)
print(List2)
print(List3,"\n")
move_to_1(List2)
print(List1)
print(List2)
print(List3,"\n")
move_to_1(List3)
print(List1)
print(List2)
print(List3)

