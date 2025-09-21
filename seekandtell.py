# with open('file.txt','r') as f:
#     f.seek(10)
#     data=f.read(5)
#     print(data)

# with open('file.txt','r') as f:
#     data=f.read(10)
#     current_position=f.tell()
#     f.seek(current_position)
#     print(f.read(5))

with open('sample.txt','w') as f:
    f.write("This is a new line.\n")
    f.truncate(8)
    with open('sample.txt','r') as f:
        print(f.read())