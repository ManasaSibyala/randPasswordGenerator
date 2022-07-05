import random;
import array;

Max_len = int(input("enter the length of password you want: "))
#representing as chars for easy cancatenation
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','y','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','$','%','^','&','*','(',')','#']
# combining the above character arrays to form a single arrays12
combined_array = lower_case+upper_case+numbers+symbols

#randomly selecting one character from each character set
symbols_rand = random.choice(symbols)
lower_rand = random.choice(lower_case)
upper_rand = random.choice(upper_case)
number_rand = random.choice(numbers)
#creating a temporary password combining the characters randomly selected

password1 = symbols_rand+lower_rand+upper_rand+number_rand

#we got only four random characters

for i in range(Max_len-4):
    password1 = password1+random.choice(combined_array)
#print(password1)    
#converting the temporary password to an array and shuffling it to prevent getting consistent pattern 

password1_arr = array.array('u',password1)
random.shuffle(password1_arr)

#transversing the temporary password array and appending the chars to form the password

password = " "
for x in password1_arr:
    password=password+x 
    
print(password)

