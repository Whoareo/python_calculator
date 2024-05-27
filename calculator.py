def total(elements: list[int]) -> int | float:
    result: int = 0
    for element in elements:
        result += element
    return result


def multiple(elements: list[int]) -> int | float:
    result: int = 1
    for element in elements:
        result *= element
    return result


def split_string(string: str) -> list[str] | None:
    if "+" in string:
        return string.split("+")
    else:
        print("Vui lòng nhập xâu hợp lệ.")
        exit(0)


def process(array: list[str]) -> int | None:
    for index, number in enumerate(array):
        if number.isnumeric():
            array[index]: int = int(number)
        elif "x" in number:
            array[index]: int = multiple([int(element) for element in number.split("x")])
        elif "*" in number:
            array[index]: int = multiple(([int(element) for element in number.split("*")]))
        else:
            print("Lỗi.")
            exit(0)
    else:
        return total(array)


user_input: str = input("Nhập phép tính: ")
numbers: list[str] = split_string(user_input)

print("Kết quả: ", process(numbers))
