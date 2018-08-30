import pickle
import sqlite3

all_att = pickle.load(open('pickle\\all_att.pkl', 'rb'))

##conn = sqlite3.connect('base_attendance.db')
##c = conn.cursor()

print('Registration No.\tDesignation\t\t\tIn-Time\t\t\t\tFaculty\t\tAttendance Start Time\n','_'*130)

for att in list(all_att):
    for i in att[0].items():
        regno = i[0]
        desig = i[1][0]
        intime = i[1][1]
        print(regno, '\t\t',desig,'\t\t',intime, '\t\t', end = '')

    faculty = "" if list(att[1].items()) == [] else list(att[1].items())[0][1]
    attstart = att[2]
    print(faculty, '\t\t', attstart)
    #c.execute("INSERT INTO base_attendance VALUES ( ? , ? , ? , ? , ? )",(regno, desig, intime, faculty, attstart))


##c.execute(""" CREATE table base_attendance(
##                regno text,
##                desig text,
##                intime text,
##                faculty text,
##                attstart text
##                ) """)


#c.execute("SELECT * FROM base_attendance")
##print(c.fetchall())
##conn.commit()
##conn.close()
