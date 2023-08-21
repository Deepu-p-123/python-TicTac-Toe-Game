import random




dict1={'usr':'x','cmp':'0'}
list1=[" "," "," "," "," "," "," "," "," "]
list2=[]
list3=[0,1,2,3,4,5,6,7,8]


def start():
    while True:

        input1=input("please select X or 0 ")

        if input1 == 'X':
            dict1={'usr':'X','cmp':'0'}
            break
        elif input1=='0':
            dict1={'usr':'0','cmp':'X'}  
            break 

        else:
            print("please choose a valid option") 
            
    return dict1


dict1=start() 

l1=list1    
def display():
    print(f"""
      
      {l1[0]}| {l1[1]}| {l1[2]} |
     -----------
      {l1[3]}| {l1[4]}| {l1[5]} |
     -----------
      {l1[6]}| {l1[7]}| {l1[8]} |
      
      """)
    

##check whether player win or not



# list1=[" "," "," "," "," "," "," "," "," "]
def case1(temp):
    c=0
    result=''
    for i in range(0,9):
        if list1[i]==temp:
            c=c+1
            if i==2 or i==5 or i==8:
                if c==3:
                    result='win'
                    break
                else:
                    c=0
        else:
            c=0
    return result        
            
            
def case2(temp):
    result=''
    c=0
    c1=[0,3,6,1,4,7,2,5,8]
    for i in c1:
        if list1[i]==temp:
            c=c+1
            if i==6 or i==7 or i==8:
                if c==3:
                    result='win'
                    break
                else:
                    
                    c=0
        else:
            c=0 
    return result                   
                    
def case3(temp):
    result=''
    c=0
    c1=[0,4,8,2,4,6]
    for i in c1:
        if list1[i]==temp:
            c=c+1
            
            if i==8 or i==6:
                if c==3:
                    result='win'
                    break
                else:
                    c=0
        else:
            c=0 
    return result

                   
    



def body():

    while True:
        x=int(input("enter the index: "))
        if x <9:
            

            if x not in list2:
                list2.append(x)
                list1[x]=dict1['usr']

                list3.remove(x) 

                ###check player win or lose##
                m=dict1['usr']

                usrrslt1=case1(m)
                usrrslt2=case2(m)
                usrrslt3=case3(m)
                if len(list2)!=9:

                    j=random.choice(list3)
                    list1[j]=dict1['cmp']
                    list2.append(j)
                    list3.remove(j)
                    n=dict1['cmp']
                    cmprslt1=case1(n)
                    cmprslt2=case2(n)
                    cmprslt3=case3(n)

                display() 
            else:
                list2.sort()
                print(f'please select index other than {list2}')  

            if cmprslt1 or cmprslt2 or cmprslt3 =='win':
                print("computer win")
                break

            elif usrrslt1 or usrrslt2 or usrrslt3 =='win':
                print("You win") 
                break 
              
        else:
            print("please enter a number less than 9") 
            
              
body()


   
   
    
    