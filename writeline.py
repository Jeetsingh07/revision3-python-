f=open('myfile.txt','w')
lines=['line\n',"line2\n","line3\n "]
f.writelines(lines)
f.close()

f=open('myfile.txt','w')
lines=['line\n',"line2\n","line3\n "]
for line in lines:
    f.write(line)
f.close()