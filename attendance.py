import pickle
import os

current_att = list(pickle.load(open('pickle\\att.pkl','rb')))
all_att = []

if os.path.isfile('pickle\\all_att.pkl'):

    all_att = list(pickle.load(open('pickle\\all_att.pkl','rb')))
    if current_att not in all_att:
        all_att.append(current_att)
        pickle.dump(all_att,open('pickle\\all_att.pkl','wb'))

else:
    pickle.dump(current_att,open('pickle\\all_att.pkl','wb'))
    all_att.append(current_att)
    
for i in all_att:
    print(i)
