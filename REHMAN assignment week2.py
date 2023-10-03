#Dictionaries:
book = { }
book['thetitle'] = "the earth"
book['author'] = "honey"
book['year'] = "1999"
print(book)

book_author = book.get('author')
print ('name of author is', book_author)

book['year'] = "2023"
book['chapters'] = "chp1,chp2"
print(book)

del book['year']
print(book)

key=book.keys()
for keys in key:
    print(keys)

square_value = {num: num**2 for num in range(1,5)}
print(square_value)

merged_dictionary= {**book , **square_value}
print('merged values are', merged_dictionary)


#Sets
colors_set= {'red','blue','green'}
print(colors_set)
colors_set.add('yellow')
print(colors_set)
colors_set.discard('red')
print(colors_set)
countryset={'usa','india'}
union_of_set = colors_set | countryset
print(union_of_set)
intersection_of_set = colors_set & countryset
print(intersection_of_set)
difference=countryset.difference(colors_set)
print(difference)
subset = {'red','green'}
subsetis =subset.issubset(colors_set)
print(subsetis)
listis=list(countryset)
print(listis)
setis=set(listis)
print(setis)
SetComprehension={ y for y in range (1,15) if   y%3==0 }
print(SetComprehension)

#Tuples
tuple_student = {'ali','afar','zia','hamid','ahmad'}
print(tuple_student)
lists=list(tuple_student)
print(lists)
tuples=tuple(lists)
print(tuples)
newtuple = ('r','t','y')
x,y,z =newtuple
print(x,y,z)

#Nested Dictionaries
student_d = {
     'std 1': {'age':20, 'grade': 'C'},
     'std 2': {'age': 22, 'grade': 'A'},
     'stud 3': {'age':24, 'grade': 'D'}}
print(student_d)
nameofstudent = input('Enter name of students : ')
age_of_students=student_d[nameofstudent]['age']
print(age_of_students)
student_d['std 1']['grade'] = 'C'
print(student_d['std 1']['grade'])
for students,info in student_d.items():
    print(f"age is  {info['age']}, grades are  {info['grade']}")