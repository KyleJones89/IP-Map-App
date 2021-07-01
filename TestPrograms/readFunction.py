#[+]Prototype of being able to read a file that contains a set of lines that contain first, an IP address and then a system name[+]



#[+]Read Line [+]

with open('test.txt') as f:
    read_data = f.read()

print (read_data)
#[+]Split the list into lines that are held in a list[+]

#thislist=[]
thislist=read_data.splitlines()


#[+]Split a member of the list into a list inside the line.[+]

#print("This is line 1" + thislist[0])
#print("This is line 2" + thislist[1])
#transposeline=[]

transposeline = thislist[0].split()

print('this is line split part 1 ' +transposeline[0])

