class file():
    # print the decode text in the file(message.txt)
    @staticmethod
    def outputinfile(message):
        f=open("E:/4th Sem/Advance Programming/Python lab/Advanceprogramming/message.txt",'w')
        f.write(message)
        f.close()
    # take input from the file for preview
    @staticmethod
    def datafromfile(choice=1):
        if choice==2:
            address="E:/4th Sem/Advance Programming/Python lab/Advanceprogramming/message.txt"
        elif choice==1:
            address="E:/4th Sem/Advance Programming/Python lab/Advanceprogramming/cipher.txt"
        f=open(address,"r")
        chiper_text=f.readline().replace("\n","")
        f.close()
        return chiper_text
    #take input from file to decrypt
    @staticmethod
    def datafromfile2(address):
        f=open(address,"r")
        chiper_text=f.readline().replace("\n","")
        f.close()
        return chiper_text

     # display the encode text in file(chiper.txt)
    @staticmethod
    def displayfile(chiper):
        f=open("E:/4th Sem/Advance Programming/Python lab/Advanceprogramming/cipher.txt",'w')
        f.write(chiper)
        f.close()
    
class raps_file(file):
    # display the encode text in file(chiper.txt)
    @staticmethod
    def displayfile(chiper,key_list,key_list2):
        f=open("E:/4th Sem/Advance Programming/Python lab/Advanceprogramming/cipher.txt",'w')
        f.write(chiper+"\n")
        for i in range(len(key_list)):
            f.write(str(key_list[i])+"\t"+str(key_list2[i])+"\t")
        f.close()

    # take input from the file
    @staticmethod 
    def datafromfile(address):
        key_list,key_list2=[],[]
        f=open(address,'r')
        chiper=f.readline().replace("\n","")
        keys=f.readline().split()
        for i in range(len(keys)):
            if i%2==0:
                key_list.append(int(keys[i]))
            else:
                key_list2.append(int(keys[i]))

        return chiper,key_list,key_list2 

class playfair_file(file):
    pass

class caesar_file(file):
    pass