import math
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
    
def get_p(attribute ,indexes, file) :
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
def InfoGain(parent_ent,attribute,main_file,mini=2,maxi=5):
    ig1 = -10000
    ind = []
    l = parent_ent
    for i in range(mini+1 ,maxi) :
        L  = get_p(attribute,[mini,i,maxi],main_file)
        temp = l
        t2= temp
        L2 = get_p(attribute,[mini,(mini+maxi)/2,maxi],main_file)
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
        #print(L,ig1)
            
    print("Information Gain : " ,ig1)
    return ind , ig1






def Decisions(filename,roots) : 
    main_file = open(filename, "r")
    dt  = {"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}        
    while True :
        line  =  main_file.readline()
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
    parent_ent = find_entropy(l)
    print(parent_ent)
    
    if abs(parent_ent) == 0.0 :
        print("No branches")
        main_file = open(filename, "r")
        line  =  main_file.readline()
        line_parts = line.split(',')
        target_class = line_parts[-1].strip()
        print("Class: ",target_class)
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
        if c not in roots :
#            print(attribute,mini,maxi)
            div,ig = InfoGain(parent_ent,c,filename,math.floor(mini),math.ceil(maxi))
            c+=1
            Info.append([div,ig])
    for i in range(0,c) :
        print(attribute[i],Info[i])
        t= Info[i][1]
        root = attribute[i]
        branches = Info[i][0]
        if Info[i][1] > t :
            t = Info[i][1]
            branches = Info[i][0]
            root = attribute[i]

    print("Root : ",root)
    print("Highest Information gain : ",t,branches)    
    tempf1 = open("t3.txt", "w+")
    tempf2 = open("t4.txt", "w+")
    source = open(filename, "r")
    while True:
        line = source.readline()
        if not line:
            break
        line_parts = line.split(',')
        new_line= ""
        if root == 'sepal-length' :
          factor = 0
        elif root == 'sepal-width' :
            factor = 1
        elif root == 'petal-length' :
           factor = 2
        elif root == 'petal-width' :
              factor = 3

        for i in range(len(line_parts)):
            if i != factor :        
              new_line += line_parts[i]
              if i != len(line_parts)-1 :
                 new_line += ','
        
#        print(new_line)
        if branches[0] <= float(line_parts[factor]) < branches[1] : 
             tempf1.write(new_line)
        elif branches[1] <= float(line_parts[factor]) <= branches[2] : 
             tempf2.write(new_line)
        
        else:
            print()
    
    source.close()
    tempf1.close()
    tempf2.close()



            



Decisions("t2.txt", [3,2])

