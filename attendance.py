import pickle

all_att = pickle.load(open('pickle\\all_att.pkl', 'rb'))


print('Registration No.\tDesignation\t\t\tIn-Time\t\t\t\tFaculty\t\tAttendance Start Time')
print('___________________________________________________________________________________________________________________________________')
for att in list(all_att):
    for i in att[0].items():
        regno = i[0]
        desig = i[1][0]
        intime = i[1][1]
        print(regno, '\t\t',desig,'\t\t',intime, '\t\t', end = '')

    faculty = att[1]
    starttime = att[2]
    print(faculty, '\t\t', starttime)



    
