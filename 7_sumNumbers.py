# sumNumbers


# Time - O(N), Space - O(1) [ignoring sum variable]
def sumNumbers(string: str) -> int:
    if not string:
        return 0

    sum = 0
    i = 0
    while i < len(string):
        if string[i].isdigit():
            tmp = string[i]
            i += 1
            while i < len(string) and string[i].isdigit():
                tmp += string[i]
                i += 1
            sum += int(tmp)
        else:
            i += 1

    return sum


print(sumNumbers("abc123xyz"))
print(sumNumbers("aa11b33"))
print(sumNumbers("7 11"))
