
##  FACULTY EXPLORE ##


import pickle
all_att = pickle.load(open('pickle\\all_att.pkl', 'rb'))

def unlock(regno):
    ##Face recog##
    return(True)


def explore(regno):
    print("Exploring")


k = 0  ##d
l = 30  ##d
allfac = []

for att in list(all_att):
    if k%2 == 0:  ##d
        c = l+k  ##d
    att[1] = {str(c):['faculty',1234]}   ##d
    print(att[1])                        ##d
    allfac.append(list(att[1].keys())[0])
    k+=1  ##d

choice = input("Enter Registration No.: ")
allfac = list(set(allfac))

if choice in allfac:
    allowed = unlock(choice)
    if allowed == True:
        print("Unlocked")
        explore(choice)
            











