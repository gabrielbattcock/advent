#day 6 of advent

file = open("buffer.txt")
buffer = file.read()

#ugly brute force
for i in range(len(buffer)):
    a = buffer[i-3]
    b = buffer[i-2]
    c = buffer[i-1]
    d = buffer[i]
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d and i>=3:
        print(a,b,c,d)
        print(i+1)
        break

#part two, getting better
for i in range(len(buffer)):
    if len(set([buffer[i-j] for j in range(14)]))==14 and i>13:
        print(i+1)
        break


#part one but cleaner
        
for i in range(len(buffer)):
    if len(set([buffer[i-j] for j in range(4)]))==4 and i>3:
        print(i+1)    
        break

