def tong(phan_tu) -> int | float:
    result: int = 0
    for element in phan_tu:
        result += element
    return result


def tich(phan_tu) -> int | float:
    result: int = 1
    for element in phan_tu:
        result *= element
    return result


user_input: str = input("Nhập phép tính: ")
numbers: list[str]
if "+" in user_input:
    numbers: list[str] = user_input.split("+")
elif "x" in user_input:
    numbers: list[str] = user_input.split("x")
elif "*" in user_input:
    numbers: list[str] = user_input.split("*")
else:
    print("Loi")
    exit(0)

for index, number in enumerate(numbers):
    if number.isnumeric():
        numbers[index]: int = int(number)
    else:
        print("Loi")
        exit(0)
else:
    if "+" in user_input:
        print(tong(numbers))
    else:
        print(tich(numbers))
