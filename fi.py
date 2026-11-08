#                    1-masala
# def clean_title_text(text:str) -> str:
#     return text.title().strip()

# print(clean_title_text(input("Matn kiriting: "))

#                     2-masala
def calculatea_average_grade(grades:dict) -> float:
    sum = 0
    for i in grades.values():
        sum += i
    return sum/len(grades)
data ={}
for i in range(int(input("Neshta fan: "))):
    fan = input("Fan: ")
    ball = int(input("Ball: "))
    data[fan] = ball
print(calculatea_average_grade(data))