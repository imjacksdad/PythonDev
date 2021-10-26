
#write one line of text
with open('readmeline.txt', 'w') as f:
    f.write('readme')

    f.write('\n')
    f.writelines('\n')

#Write each item in a list to a seperate line in the text file.
lines = ['Readme', 'How to write text files in Python']
with open('readmelist.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

#Write each item in a list all on the same line in the text file.
lines = ['Readme', 'How to write text files in Python']
with open('readmelines.txt', 'w') as f:
    f.writelines(lines)

#Append the text to the bottom of the file.
more_lines = ['', 'Append text files', 'The End']
with open('readmemorelines.txt', 'a') as f:
    f.writelines('\n'.join(more_lines))
