def get_coords():
    dummy=False
    while dummy==False:
        textfile = open('output.txt').read()
        if textfile!="": dummy=True
        #stupid=0
    coords = parse_line(textfile)
    #textfile.close()
    textfile = open('output.txt','w')
    textfile.write("")
    textfile.close()
    return [float(x) for x in coords]
    
def parse_line(line):
    #line = line.replace('\n','')
    a = line.split(',')

    #s = [x for x in line]
    #s.append(line[0])
    #s.append(line[1])
    #s.append(line[2])
    #print a
    return a

'''def make_list(text_file):
    i = 0
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    for line in file(text_file):
        s = ""
        s = parse_line(line)
        '' make each data set correspond to a different letter, each letter is a different touch pozt''
        while (i < 5):
            if i == 0:
                a = s
                print a
                i = 1
                break
            elif i == 1:
                b = s
                print b
                i = 2
                break
            elif i == 2:
                c = s
                print c
                i = 3
                break
            elif i == 3:
                d = s
                print d
                i = 4
                break
            elif i == 4:
                e = s
                print e
                i = 10
                break '''
    
#def clear_file(text_file):
    #text_file.truncate()


'''make_list('responses.txt')'''




