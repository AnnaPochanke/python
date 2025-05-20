#
# # WORKING WITH FILES - "Python for Linguists"
# ##
# 0. Opening a file
# open(file_path) method returns file object

# 1. scenario, opens a file in the current folder, your python script and analyzed file are in the same folder
# sample_file = open('testfile.txt')
# # 2 scenario, relative path
# - -> very often exceptions !!!
sample_file = open(
    'test2.txt')

# # # # Get the directory of the current script
# # # script_dir = os.path.dirname(os.path.abspath(_file

# # # # Construct the full path to the file
# # # file_path = os.path. join(script_dir, 'test', 'mestfile.txt')

# # # # Open the file (ensure the file exists at the specified path)
# # # try:
# # # sample_file = open(file_path)
# # # print("File opened successfully!")
# # # sample_file.close()
# # # # except FileNotFoundError:
# # # print(f"File not found: {file_path}")

# # #
# # sample_file.close()
# # except FileNotFoundError:
# # print(f"File not found: {file_path}")

# # : # 3. scenario - absolute path
# # ample_file = open(
# # r'C:\Users\rober\OneDrive\Dokumenty\UAM\PYTHON CODE\PYTHON PROGRAMMING\testfile.txt') # 2 scenario, using absolute pa

# # : # 1. Writting to a file

# # : # open / create file stream
# # outFile = open('testfile.txt', 'w', encoding='utf-8')
# # : # write to it
# # : outFile.write('some text!\n')
# # : outFile.write(' ... and some more text!\n')
# # outFile.close() # close file stream

# # : # 2. Writting once more to a file
# # #
# # #
# # #
# # #

# # #

# # #

# # # # 1. Writting to a file

# # # # open / create file stream
# # outFile = open('testfile.txt', 'w', encoding='utf-8')
# # # write to it
# # outFile.write('some text!\n')
# # outFile.write(' ... and some more text!\n')
# # outFile.close() # close file stream

# # # # # Open the file (ensure the file exists at the specified path)
# # # try:
# # sample_file = open(file_path)
# # print("File opened successfully!")
# # sample_file.close()
# # # except FileNotFoundError:
# # print(f"File not found: {file_path}")

# # # # 3. scenario - absolute path
# # sample_file = open(
# # r'C:\Users\rober\OneDrive\Dokumenty\UAM\PYTHON CODE\PYTHON PROGRAMMING\testfile.txt') # 2 scenario, using absolute path as

# I

# # # 2. Writting once more to a file

# # # open / create file stream
# # # 3. scenario - absolute path
# # sample_file = open(
# r'C:\Users\rober\OneDrive\Dokumenty\UAM\PYTHON CODE\PYTHON PROGRAMMING\testfile.txt') # 2 scenario, using absolute path as

# #

# # # 1. Writting to a file

# # # open / create file stream
# outFile = open('testfile1.txt', 'w', encoding='utf-8')
# # write to it
# outFile.write('some text! some text\n')
# outFile.write(' ... and some more text! mor more \n')
# outFile.close() # close file stream

# # # 2. Writting once more to a file

# # # open / create file stream
# # outFile = open('testfile.txt', 'w', encoding='utf-8')
# # # # now it will overwrite a file
# # outFile.write('once more some text!\n')
# # outFile.write(' ... and once more some more text!\n')
# # outFile.close() # close file stream

# # # 3. Appending text to a file

# # # 3. Appending text to a file

# # open / create file stream
# outFile = open('testfile.txt', 'a', encoding='utf-8')
# # now it will append text to a file
# outFile.write('once more some text!\n')
# outFile.write(' ... and once more some more text!\n')
# outFile.close() # close file stream

# # # 4. READING A FILE
# # # open file stream
# # inFile = open('testfile.txt', 'r', encoding='utf-8')
# # stuff = inFile.read() # read from it
# # inFile.close() # close stream
# # print(stuff) # print contents

# # # 5. READNG A FILE (LINE BY LINE ANALYSIS)
# # open file
# # inFile = open('testfile.txt', 'r', encoding='utf-8')
# # stuff = inFile.read() # read file contents

# # # 5. READNG A FILE (LINE BY LINE ANALYSIS)
# # open file
# inFile = open('testfile.txt', 'r', encoding='utf-8')
# stuff = inFile.read() # read file contents
# inFile.close() # close file
# lines = stuff.split('\n') # split into lines
# # print lines and lengths
# for line in lines:
# print(f'{line}, : {len(line)} characters')

# # # 5.1 READNG A FILE (LINE BY LINE ANALYSIS)
# # # # open file
# # inFile = open('testfile.txt', 'r', encoding='utf-8')
# # # read file contents (all lines) - returns list of lines
# # lines = inFile.read().splitlines()
# # inFile.close() # close file
# # # print(lines)
# # # print lines and lengths
# # for line in lines:
# print(f'{line}, : {len(line)} characters')

# # read file content
# # split into lines

# #
# #
# #

# #

# # # # 6. READING A FILE(LINE BY LINE ANALYSIS) - BETTER METHOD
# # # # open file:
# with open('testfile.txt', 'r', encoding='utf-8') as inFile:
# stuff = inFile.read()
# lines = stuff.split('\n')
# # print lines and lengths
# for line in lines:
# print(f'{line}, : {len(line)} characters')

# # # 6.1 READING A FILE (LINE BY LINE ANALYSIS) - BETTER METHOD
# # # # open file
# # with open('testfile.txt', 'r', encoding='utf-8') as inFile:
# lines = inFile.read().splitlines() # read file content + split into lines
# # print lines and lengths
# for line in lines:
# print(f'{line}, : {len(line)} characters')

# # ## 7. WRITTING TO A FILE - BETTER METHOD

# # # # open / create file stream
# # with open('testfile.txt', 'w', encoding='utf-8') as outFile:
# # write to it
# outcila wnital 'cama tavtlin'i
