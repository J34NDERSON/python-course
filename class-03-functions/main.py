def my_sum(num1, num2):
    total = num1 + num2
    return total

print(my_sum(2, 3))

def calc_avg(grade1, grade2, grade3):
    avg = (grade1 + grade2 + grade3) / 3
    return avg


grade1 = float(input("digite a grade 1:"))
grade2 = float(input("digite a grade 2:"))
grade3 = float(input("digite a grade 3:"))



# print(calc_avg(10, 10, 10))
print(calc_avg(grade1, grade2, grade3))