#PF-Prac-1
def add_string(str1):
    if(len(str1)<3):
        return str1
    if(str1.endswith("ing")):
        str=str1+"ly"
        return str
    else:
        str=str1+"ing"
        return str
str1="com"
print(add_string(str1))


#PF-Prac-2
def bracket_pattern(input_str):
    if(input_str.startswith(")") and input_str.endswith("(")):
        return False
    s1=input_str.count("(")
    s2=input_str.count(")")
    if(s1==s2):
        return True
    else:
        return False
input_str="(())("
print(bracket_pattern(input_str))


#PF-Prac-3
def create_new_dictionary(prices):
    new_dict={}
    for key in prices:
        if(prices[key]>200):
            new_dict.__setitem__(key,prices[key])
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))



#PF-Prac-4
def find_nine(nums):
    for i in range(0,len(nums)):
        if(nums[i]==9 and i<4):
            return True
    else:
        return False
nums=[1,9,4,5,6]
print(find_nine(nums))


#PF-Prac-5
def count_digits_letters(sentence):
    letter=0
    digit=0
    l=[]
    for i in sentence:
        if i.isalpha():
            letters += 1
           
        elif i.isnumeric():
            digit += 1
            
    l.append(letters)
    l.append(digit) 
    return l
sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))



#PF-Prac-6
def list123(nums):
    num=""
    for i in nums:
        num=num+str(i)
    if("123" in num):
        return True
    else:
        return False
  

nums=[1,2,5,4,3]
print(list123(nums))




#PF-Prac-7
def seed_no(number,ref_no):
    s=number
    while(number!=0):
        r=number%10
        s*=r
        number=number//10
    if(s==ref_no):
        return True
    else:
        return False
number=123
ref_no=738
print(seed_no(number,ref_no))



#PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=="D"):
            net_amount+=int(a[1])
        else:
            net_amount-=int(a[1])
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))


#PF-Prac-9
def generate_dict(number):
    new_dict={}
    for i in range(1,number+1):
        new_dict[i]=i**2
    
    return new_dict

number=20
print(generate_dict(number))



#PF-Prac-10
def string_both_ends(input_string):
	if(len(input_string)<2):
	    return -1
	else:
	    s=""
	    s=input_string[0:2]+input_string[len(input_string)-2:len(input_string)]
	    return s
input_string="w3w"
print(string_both_ends(input_string))


#PF-Prac-11
def find_upper_and_lower(sentence):
    up=0
    lo=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lo+=1
        if(i>="A" and i<="Z"):
            up+=1
    result_list=[]
    result_list.append(up)
    result_list.append(lo)

    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))



#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
	sentence_list=[]
	for i in subjects:
	    for j in verbs:
	        for k in objects:
	            sentence_list.append(i+" "+j+" "+k)

	
	return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))


#PF-Prac-15
def check_22(num_list):
    for i in range(0,len(num_list)-1):
        if(num_list[i]==2 and num_list[i+1]==2):
            return True
    else:
        return False
       
        
print(check_22([3,2,5,1,2,1,2,2]))



#PF-Prac-22
def diagonal_stars(number):
    for i in range(0,number):
        for j in range(i):
            print(".",end="")
        print("*")
       
number=6    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    sum=0
    temp=number
    while(number!=0):
        d=number%10
        sum+=d
        number=number//10
    if(temp%sum==0):
        return True
    else:
        return False
    
number=42
print(divisible_by_sum(number))



#PF-Prac-24

def find_gcd(num1,num2):
    if(num2==0):
        return num1
    else:
        return find_gcd(num2,num1%num2)
    
num1=800
num2=2800
print(find_gcd(num1,num2))


#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for i in word_list:
        count_list.append(len(i))
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))



#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))



#PF-Prac-27
def check_for_ten(num1,num2):
    if(num1==10 or num2==10 or num1+num2==10):
        return True
    else:
        return False
    
print(check_for_ten(10,9))



#PF-Prac-37
def sum_of_list(num_list):
    if(len(num_list)>1):
        return num_list[0] + sum_of_list(num_list[1:])
    else:
        return num_list[0]
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)


#PF-Prac-13
import math
def close_number(n1,n2,n3):
    if (math.fabs(n1-n2)==1 and math.fabs(n3-n2)>=2 and math.fabs(n3-n1)>=2):
        return True
    elif(math.fabs(n3-n2)==1 and math.fabs(n1-n2)>=2 and math.fabs(n3-n1)>=2):
        return True
    elif (math.fabs(n1-n3)==1 and math.fabs(n3-n2)>=2 and math.fabs(n2-n1)>=2):
        return True
    else:
        return False

print(close_number(5,4,2))



#PF-Prac-16
def rotate_list(input_list,n):
    output_list=[]
    for i in range(len(input_list)-n,len(input_list)):
        output_list.append(input_list[i])
    for i in range(0,len(input_list)-n):
        output_list.append(input_list[i])
   
    
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)



#PF-Prac-21
def check_numbers(num1,num2):
    num_list=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.append(i)
    
    return (num_list)

num1=2
num2=20
print(check_numbers(num1, num2))



#PF-Prac-32
def check_squares(number):
    for i in range(1,10000):
        for j in range(i+1,10000):
            if(i*i + j*j ==number):
                return True
    return False

number=68
print(check_squares(number))













