# --------------
##File path for the file 
file_path 



#Code starts here

def read_file(path):
    read_file.p=path
    file=open(read_file.p,mode="r")
    return file.readline()

sample_message = read_file(file_path)
print(sample_message)
     
   


# --------------
#Code starts here

def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quot=(int(message_b)//int(message_a))
    
    #Returning the quotient in string format
    return str(quot)

#Calling the function to read file  
message_1=read_file(file_path_1)
print(message_1)
#Calling the function to read file
message_2=read_file(file_path_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)




# --------------
#Code starts here

def substitute_msg(message_c):
    if message_c=="Red":
        sub='Army General'
    elif message_c=="Green":
        sub="Data Scientist"
    elif message_c=="Blue":
        sub="Marine Biologist"
    return sub
def read_file(path):
     file=open(path,mode="r")
     return file.readline()
     
     
     

message_3=read_file(file_path_3)
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)











# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(path):
    read_file.p=path
    file=open(read_file.p,mode="r")
    return file.readline()

message_4 = read_file(file_path_4)
print(message_4)
message_5 = read_file(file_path_5)
print(message_5)
    
def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    Final_msg=" ".join(c_list)
    return Final_msg

    

secret_msg_3=compare_msg(message_4,message_5)






# --------------
#Code starts here
def read_file(path):
    read_file.p=path
    file=open(read_file.p,mode="r")
    return file.readline()

message_6=read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list=message_f.split()
    even_word=lambda x:len(x)%2==0
    b_list=list(filter(even_word,a_list))
    final_msg=" ".join(b_list)
    return final_msg



secret_msg_4=extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]




secret_msg=" ".join(message_parts)
print(secret_msg)

def write_file(secret_msg,path):
    file=open(path,mode="a+")
    file.write(secret_msg)
    file.close()
final_path= user_data_dir + '/secret_message.txt'

write_file(secret_msg,final_path)
print(secret_msg)


#Code starts here



