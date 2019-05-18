
def humanize(text):
    text = text.replace(" ", "")
    digits = "0123456789"
    symbols = "+-*/="
    for c in text:
        if not (c in digits or c in symbols):
            return "invalid input"

    # text is invalid if there are 2 symbols in a row like "5*2+=2"
    prev_c_is_digit = False
    for c in text:
        if c in symbols and not prev_c_is_digit:
            return "invalid input"
        prev_c_is_digit = c in digits

    parts = []
    number_str = ""
    for c in text:
        if c in symbols:
            parts.append(number_str)
            number_str = ""
            parts.append(c)
        else:
            number_str += c
    if number_str != "":
        parts.append(number_str)

    print(parts)
    result = ""
    for part in parts:
        if part in symbols:
            result += special_symbol_to_string(part) + " "
        elif part.isdigit():
            result += int_to_text(int(part)) + " "
        else:
            result += f"(wrong part: {part}) "

    print("text: ", text)
    return result.strip()


def special_symbol_to_string(sym):
    if sym == "*":
        return "multiply by"
    elif sym == "/":
        return "divide by"
    elif sym == "+":
        return "plus"
    elif sym == "-":
        return "minus"
    elif sym == "=":
        return "equals"
    return "wrong symbol"


numbers_map_0_20 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers_map_20_90 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
big_numbers = ["quadrillion", "trillion", "billion", "million", "thousand", ""]


# converting integers in range 0-999 to text
def int_to_text_0_999(number):
    if number > 999 or number < 0:
        return "invalid number: " + number

    if number == 0:
        return "zero"

    hundreds = number // 100
    result = ""
    if not hundreds == 0:
        result += numbers_map_0_20[hundreds] + " hundred"
        if hundreds > 1:
            result += "s"

    last_two = number % 100
    if last_two == 0 and hundreds > 0:
        pass
    elif last_two < 20:
        result += " " + numbers_map_0_20[last_two]
    else:
        tens = last_two // 10
        ones = last_two % 10
        result += " " + numbers_map_20_90[tens - 2]
        if ones != 0:
            result += " " + numbers_map_0_20[ones]

    return result


# converting integers in range 0-1000000000000 to text
def int_to_text(number):
    if type(number) is not int or number < 0:
        return "invalid number"
    if number == 0:
        return "zero"

    division = 1000000000000000
    if number >= division * 1000:
        return "999+ quadrillions+"
    parts = []

    while division > 0:
        part = number // division
        part = part % 1000
        parts.append(part)
        division //= 1000

    result = ""
    index = 0
    for part in parts:
        if part > 0:
            result += int_to_text_0_999(part) + " " + big_numbers[index]
            if part > 1 and index + 1 != len(big_numbers):
                result += "s"
            result += " "
        index += 1

    result = result.replace("  ", " ").strip()

    return result
