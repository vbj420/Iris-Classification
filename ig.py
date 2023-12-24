# STANDARDIZED DECISION TREE ALGORITHM 
# USING INFORMATION GAIN -- method  
# PRE -ASSUMPTION OF 2-BRANCH IN THE DATA
import math
f = open("flower_data.txt", "r")
dt  = {"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}

def find_entropy(lst) :
    s = sum(lst)
    entropy = 0
    for i in lst  :
        if s== 0 :
            return 0
        p = i/s
        if  p >0 :
          entropy += p*math.log2(p)
       # print(entropy)
    entropy *=- 1
    return entropy
    
    
while True :
    line  =  f.readline()
    if not line  :
        break
    line_parts = line.split(',')
    target_class = line_parts[-1].strip()
    #print(target_class)
    for k in dt.keys():
      if k == target_class:
          dt[k] += 1         
#print(dt)
l  = list(dt.values())
print(l)


#  find information gain
#  1) sepal length is provided min 4 and max 8
#  Consider two classes 4-6 6-8
f.close()

def get_p(attribute ,indexes, file="flower_data.txt") :
    f = open(file, "r")    
    L = []
    for i in indexes[:-1] :
        L.append([0,0,0])
    while True:
        line = f.readline()
        if not line:
            break
        line_parts = line.split(',')
        # Check if the line has enough parts to proceed
        if len(line_parts) >= 2:
            target_str = line_parts[attribute].strip()
            if target_str:
                target = float(target_str)
                for i in range(len(indexes)-1) :
                    if indexes[i] <= target <  indexes[i+1] :
                        if line_parts[-1].strip() == "Iris-setosa":
                            L[i][0] += 1
                        elif line_parts[-1].strip() == "Iris-versicolor":
                            L[i][1] += 1
                        elif line_parts[-1].strip() == "Iris-virginica":
                            L[i][2] += 1
    f.close()
    #print(L)
    return L    

def InfoGain(attribute,mini=2,maxi=5):
    ig1 = -10000
    ind = []
    for i in range(mini+1 ,maxi) :
        L  = get_p(attribute ,[mini,i,maxi])
        temp = find_entropy(l)
        t2= temp
        L2 = get_p(attribute,[mini,(mini+maxi)/2,maxi])
        #print(L,L2)
        for j in L2 :
            t = find_entropy(j)
            t2 -=t
        for j in L :
            t =find_entropy(j)
            temp -= t
        if temp > ig1  :
            ind =[mini,i,maxi]
            ig1 = temp
        elif t2 >ig1 :
            ind =[mini,(mini+maxi)/2,maxi]
            ig1 = t2
            
    print("Information Gain : " ,ig1)
    return ind , ig1



t= open("types.txt","r")
c=0
Info = []
attribute = []
while True :
    s = t.readline()
    if not s :
        break
    a = s.split(',')
    attribute.append(a[0].strip())
    mini = float(a[1])
    maxi = float(a[2])
    #print(attribute,mini,maxi)
    div,ig = InfoGain(c,math.floor(mini),math.ceil(maxi))
    c+=1
    Info.append([div,ig])
    
    
for i in range(0,4) :
    print(attribute[i],Info[i])
    t= Info[0][1]
    if Info[i][1] >  t :
        t = Info[i][1]
        branches = Info[i][0]
        root = attribute[i]
print("Root : ",root)
print("Highest Information gain : ",t,branches)
        



tempf1 = open("branch1.txt", "w+")
tempf2 = open("branch2.txt", "w+")
source = open("flower_data.txt", "r")
while True:
    line = source.readline()
    if not line:
        break
    line_parts = line.split(',')
    new_line= ""
    for i in range(len(line_parts)):
        if i !=3 :        
          new_line += line_parts[i]
          if i != len(line_parts)-1 :
             new_line += ','
    
    if len(line_parts) >= 4:
        factor = line_parts[3].strip()
        #print(factor)
        factor = float(factor)
        if branches[0] <= factor < branches[1] : 
             tempf1.write(new_line)
        elif branches[1] <= factor <= branches[2] : 
             tempf2.write(new_line)
             
        
    else:
        print()

source.close()
tempf1.close()
tempf2.close()









        
        
        