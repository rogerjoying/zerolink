import operator
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(middle)
    print(avg)
    
drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])

student_tuples = [
('john', 'A', 15),
('jane', 'B', 12),
('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda x: x[2]))
print(sorted(student_tuples, key=operator.itemgetter(1)))

