# datatype
number = 3
string = "Python"
list = ['one', 2, 'three', 4]   # 원소 값 바꿈
dictionary = {'name':'john', 'phone':'01011112222'} # 키:값 으로 구성
tuple = ('a', 1, 'b', 2)    # 원소 값 못바꿈
set = {'apple', 'banana', 'orange'}
bool = True


# if
money = True
if money:
    print("돈이 있다.")
else:
    print("돈이 없다")

score = int(input("점수 입력 : "))

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
else :
    print("C")


# while
count = 3
while count > 0:
    print(f"Count : {count}")
    count -= 1


# for
students = [{'name':'Park', 'score':80}, {'name':'Lee', 'score':70}, {'name':'Han', 'score':60}]
for student in students:
    if student['score'] >= 80:
        print("A")
    elif student['score'] >= 70:
        print("B")
    else :
        print("C")


# for range
for count in range(1, 11):
    print(f"countdown. {count}")


# function
def func(arg1, arg2):
    return arg1 + arg2
