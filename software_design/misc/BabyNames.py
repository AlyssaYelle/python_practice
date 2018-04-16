import urllib.request

def name_exists(name,dic):
    return name in dic

def highest_rank(name,dic):
    x = [int(i) for i in dic[name]]
    return 1900 + (x.index(min(x))*10)

def all_rankings(name,dic):
    for i in dic[name]:
        print(str(1900 + dic[name].index(i)*10)+ ': ' + str(i) )
    return

def one_decade_names(dic,decade):
    names = []
    values = []
    idx = int(decade%100/10)
    for name,ls in dic.items():
        if((ls.index(ls[idx]) == idx) and (ls[idx] != 0)):
            names.append(name)
            values.append(ls[idx])
    new_dict = dict(zip(names,values))
    return sorted(new_dict.items(), key=lambda x:x[1])

def all_names_decades(dic):
    for idx in range(10):
        all_decade = [name for name,ls in dic.items() if ls[idx] !=0 and ls.count(0) == 0]
    return all_decade 

def more_popular(dic):
    keyy = []
    for key,value in dic.items():
        flag = True
        for i in range(len(value) - 1):
            if (value[i] == 0 or value[i+1] == 0):
                flag = False
            if(value[i] <= value[i+1]):
                flag = False
        if flag == True:
            keyy.append(key)
    return keyy
    
def less_popular(dic):
    k = []
    for key,value in dic.items():
        flag = True
        for i in range(len(value) - 1 ):
            if (value[i] == 0 or value[i+1] == 0):
                flag = False
            if(value[i] >= value[i+1]):
                flag = False
        if flag == True:
            k.append(key)
    return k

    
def main():
    try:
        data = urllib.request.urlopen('http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt').read()
        in_file = [str(line,encoding = 'utf8') for line in data.splitlines()]
    except HTTPError as ex:
        err_msg = ex.read()
    
    names = []
    values = []
    for line in in_file:
        ls = line.split()
        names.append(ls[0])
        del ls[0]
        values.append(ls)
    for i in range(len(values)):
        for j in range(len(values[i])):
            values[i][j] = int(values[i][j])
           
    name_dict = dict(zip(names,values))
    #user input
    while(True):
        print ('Options:')
        print ('Enter 1 to search for names.')
        print ('Enter 2 to display data for one name.')
        print ('Enter 3 to display all names that appear in only one decade.')
        print ('Enter 4 to display all names that appear in all decades.')
        print ('Enter 5 to display all names that are more popular in every decade.')
        print ('Enter 6 to display all names that are less popular in every decade.')
        print ('Enter 7 to quit. ')
        print()
        choice = int(input('Enter choice: '))
        
        #conditions to determine option
        if(choice == 1):
            name = input('Enter a name: ')
            if(name_exists(name,name_dict)):
                print("The matches with their highest ranking decade are: ")
                print(name + " " + str(highest_rank(name,name_dict)))
            else:
                print()
                print(name + ' does not appear in any decade.')
            print()
        elif(choice == 2):
            name = input('Enter a name: ')
            print(name + ": " + ' '.join(str(x) for x in name_dict[name]))
            if(name_exists(name,name_dict)):
                all_rankings(name,name_dict)
            else:
                print(name + ' does not appear in any decade.')
            print()
        elif(choice == 3):
            decade = int(input('Enter decade: '))
            # option 3
            d = one_decade_names(name_dict,1980)
            print("The names are in order of rank:")
            for i in d:
                print(i[0] + ': ' + str(i[1]))
            print()
        elif(choice == 4):
            print(str(len(all_names_decades(name_dict))) + ' names appear in every decade. The names are: ')
            for name in all_names_decades(name_dict):
                print(name)
            print()
        elif(choice == 5):
            print(str(len(more_popular(name_dict))) + " " + "names are more popular in every decade.")
            for name in more_popular(name_dict):
                print(name)
            print()
        elif(choice == 6):
            print(str(len(less_popular(name_dict))) + " " + "names are less popular in every decade.")
            for name in less_popular(name_dict):
                print(name)
            print()
        elif(choice == 7):
            print("Goodbye.")
            break
        else:
            print("Goodbye.")
            break
main()