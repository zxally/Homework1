-----------Ex1 - String ----------------
Enter text and display it one by one

text = input("Enter your text please : ")
for cha in text:
    print(cha)


------------------Ex2 - String------------
Enter text and display number of letter

text = input("Enter your text mor : ")
for i in range(len(text)):
    print(i)


--------------------Ex3 - String-----------------
Enter text and check if it contains capital letter or not
Display "Yes" if capital
display "No" if all lowercase letter


text=input("Enter your text: ")
result="No"
for i in range (len(text)):
    if text[i].upper()==text[i]:
        result="Yes"
print(result)



----------------Ex4 - String -------
We have text = "3 4 5 6"
Q1 - display number 1 by one without space
Q2 - Sum all number (Total: 18)

text = input("Enter your number : ")
index = 0 
space = ""
for i in range(len(text)) :
    if text[i] == " ":
        space += ""
    else: 
        space += text[i]
        index += int(text[i])
print(space)
print("Total :", index)


-------------Ex5 - String ------------
Q1
text = input("Enter your number here : ")
odd_count = 0
even_count = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Odd count:", odd_count)
print("Even count:", even_count)

Q2
text = input("Enter your number here : ")
sum = 0
for i in range(len(text)):
    sum += int(text[i])
print(sum)

Q3
text = input("Enter your number here : ")
sum_even = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        sum_even += int(text[i])
print(sum_even)

Q4
text = input("Enter your number here : ")
lastindex = len(text) - 1
result = ""
for i in range(len(text)):
    result += text[lastindex-i]
print(result)



----------------Ex6 - Number-----------
Enter number and check 
if odd number print "Odd" otherwise print "Even"

Number = int(input("Enter your number : "))
if Number % 2 != 0:
    print("odd")
else:
    print("even")


----------------Ex7 - number----------------
Enter number in range 10 - 20 until you enter other number out of range
display "Continue" if number in range 10 - 20
display "Out of range" if number difference from range 10 - 20


isnotfound = True
while isnotfound:
    Number = int(input("Enter your number : "))
    if Number >= 10 and Number <= 20 :
        print("Continue")
    else:
        isnotfound = False
print("Out of rang")


--------------------Ex8 - String--------------
We have text = "9394884039"
Q1 - How many number 8 in string



text = input("Enter your num  ; ")
count8 = 0

for i in range (len(text)):
    if text[i] == "8":
        count8 += 1
print(count8)


Q2 - What is first index of letter 8


text = "9394884039"
index = 0
isfound = False
while not isfound:
    if int(text[index]) == 8:
        isfound = True
    else:
        index += 1
print(index)


        

---------------------Ex9 - String-------------------------
We have string = "3 4 5 6"
Q1 - Remove space and keep result = "3456"
Q2 - Multiple each letter by 2 result = "6 8 10 12"


text = input("Enter your num : ")
none_space = ""
total= 0
for i in range(len(text)):
    if text[i] != " ":
        none_space += text[i]
        total += int(text[i]) * 2
        print(total)
    else:
        none_space += ""
print(none_space)




------------------Ex10 - Number----------------
Enter 5 numbers and find maximum and minimum value


BigNumber = 0
SmallNumber = 0
for i in range(5):
    number = int(input("Enter number : "))
    if BigNumber == 0 and SmallNumber == 0:
        BigNumber = number
        SmallNumber = number
    else:
        if number > BigNumber:
            BigNumber = number
        if number < SmallNumber:
            SmallNumber = number
print("BigNumber : ", BigNumber)
print("SmallNumber : ", SmallNumber)