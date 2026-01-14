#Files
#Reading files

f = open('/workspaces/Phyton-Fundamentals/Exercises/day-01/Python-essential-training/10 working-with-files/test.txt', 'r')
print(f)

print(f.readline())

print(f.readlines())

f = open('/workspaces/Phyton-Fundamentals/Exercises/day-01/Python-essential-training/10 working-with-files/test.txt', 'r')
for line in f.readlines():
    print(line.strip())


#Write files 
f = open('/workspaces/Phyton-Fundamentals/Exercises/day-01/Python-essential-training/10 working-with-files/test.txt', 'w')
print(f)

f.write('Line 1\n')
f.write('Line 2\n')

f.close()

#Append files
f = open('/workspaces/Phyton-Fundamentals/Exercises/day-01/Python-essential-training/10 working-with-files/test.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()

with open('/workspaces/Phyton-Fundamentals/Exercises/day-01/Python-essential-training/10 working-with-files/test.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')
    
print(f)