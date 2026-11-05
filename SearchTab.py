# def SearchTab(tab,k):
#     pos=[]
#     for i in range(len(tab)):
#         if tab[i]==k :
#             pos.append(i)


#     return pos



# notes=[12,13,14,15,1]
# print("serch",SearchTab(notes,1))

# Effectue la recherche associative dans un vecteur 
# Input : Une vecteur A[0..n – 1] et une clé de recherche K 
# Output : L’indice du premier élément de A égal à K ou –1 sinon 
def SearchTab (tab, k):
    i=0
    while (i < len(tab) and tab[i] != k):
        i = i+1 
    if i < len(tab):
        return i 
    else:
         return -1
          
   
           

notes=[12,13,14,15,1]
print("serch",SearchTab(notes, 100))