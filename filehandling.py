# f=open('file.txt','w')
# # print(f)
# text=f.read()
# print(text)
# f.close()


# f = open('file.txt', 'r')
# text = f.read()   # add parentheses to actually read the file
# print(text)
# f.close()

# f=open('myfile.txt','w')
# text=f.write()
# print(text)
# # f.close()


# f=open('file.txt','a')
# text=f.write('hello world')
# # print(text)
# f.close()







import os# Check if the file exists before reading
if os.path.exists('file.txt'):
    f = open('file.txt', 'r')
    text = f.read()  # read the entire file content
    print(text)
    f.close()


f = open('file.txt', 'r')
text = f.read()  # read the entire file content