#day 6

file = open("command.txt")
command = file.read().split('\n')




folder = []

for item in command:
    if '$ cd' in item:
        if '..' not in item:
            folder.append(item.split('cd ')[1])
        
print()