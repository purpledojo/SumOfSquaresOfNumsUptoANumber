# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num = input("Give number")
if int(num) <= 0:
    print("Error")
else:
    a = []
    for r in range( int(num)):
        
        ans = r * r
        a.append(ans)
        
    w = sum(a)
    print (w)