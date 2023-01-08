
#type A - all rows stay same, updating any rows causes all others to be same
t = [[0]*3]*3
x=0
y=0
for i in range(1):
    t[i][0]=x
    x+=1
    t[i][1]=x
    x+=1
    t[i][2]=x
    x+=1

print(t)

#independent row creation - realistic 2D Array: 
#create a 3*3 grid
rows, cols = (3, 3)
board = ([["" for i in range(cols)] for j in range(rows)])