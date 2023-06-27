#on the folder we have a work.txt file

#to open a file, lets use Open() function
#the open() open a file and return a file object
file = open('./7_writing_reading_files/work1.txt','w',encoding='utf-8')
file.close()

# the options to secound argumento are :
# r = open for reading
# w = open for writing
# x = open for exclusive creation
# a open for writing, appending to the end of file if it exists
# b = binary mode
# t = text mode
# + = open for updating (read e writing)

#Let's use the with keywork to. Its'same try catch in others langauges
#open the file for reading
with open('./7_writing_reading_files/work.txt','r',encoding='utf-8') as f:
    #reader all file content
    reader_data = f.read()
    print(reader_data)
f.closed


#other way to do
with open('./7_writing_reading_files/work.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)
f.close()


#to execute type py .\7_writing_reading_files\workingFiles.py on terminal