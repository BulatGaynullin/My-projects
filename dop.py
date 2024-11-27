grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
k = sorted(students)
p0 = sum(grades[0]) / len(grades[0])
p1 = sum(grades[1]) / len(grades[1])
p2 = sum(grades[2]) / len(grades[2])
p3 = sum(grades[3]) / len(grades[3])
p4 = sum(grades[4]) / len(grades[4])
d = {
    k[0]: p0,
    k[1]: p1,
    k[2]: p2,
    k[3]: p3,
    k[4]: p4,
}
print(d)