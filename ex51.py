def maximum(T):
    max=T[0]
    for i in range(10):
        if max<T[i]:
            max=T[i]
    return max
  
def minimum(tab):
    min=tab[0]
    for i in range(10):
       if min>tab[i]:
          min=tab[i]
    return min
    
def reversed(T):
    reversed_tab=[]
    for i in range(9,-1,-1):
     reversed_tab.append(T[i])
    return reversed_tab
    
T=[]
for i in range(10):
    T.append (int(input("entrer la valeur:")))

print("le maximum est:",maximum(T))
print("le minimum est:",minimum(T))
print("le tableau renverser est:",reversed(T))
              
