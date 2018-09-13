import pickle
import sqlite3

all_att = pickle.load(open('pickle\\all_att.pkl', 'rb'))

##conn = sqlite3.connect('base_attendance.db')
##c = conn.cursor()

print('Registration No.\tDesignation\t\t\tIn-Time\t\t\t\tClass No.\n','_'*130)

########### FACULTY #####################################
for att in list(all_att):

    if list(att[1].values()) != []:
        print(list(att[1])[0],'\t\tfaculty\t\t\t',list(att[1].values())[0][1],'\t\t',att[4])


############## STUDENT #######################3333    
    for i in att[0].items():
        if i[1][0] == 'student':
            regno = i[0]
            desig = i[1][0]
            intime = i[1][1]
            print(regno, '\t\t',desig,'\t\t',intime, '\t\t',att[4])
            

