# STANDARDIZED DECISION TREE ALGORITHM 
# USING INFORMATION GAIN -- method  
# PRE -ASSUMPTION OF 2-BRANCH IN THE DATA
import math
f = open("flower_data.txt", "r")
dt  = {"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}
#print(f.readline())
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

def get_p(attribute ,indexes) :
    f = open("flower_data.txt", "r")    
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
                
    #print(L)
    #print(C)
    return L    

mini  = 4
maxi = 8
ig1 = -10000
for i in range(mini+1 ,maxi) :
    L  = get_p(0 ,[mini,i,maxi])
    print(L,i)
    temp = find_entropy(l)
    for i in L :
        t =find_entropy(i)
        temp -= t
    print(temp)
    ig1 = max(ig1,temp)
    
print("Information Gain : " ,ig1)
    
    
    
    
    
    
    