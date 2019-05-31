# stringSplosion


def stringSplosion(string: str) -> str:
    if not string:
        return string

    res = ""
    for i in range(len(string)):
        res += string[0:i + 1]

    return res


print(stringSplosion("Code"))
print(stringSplosion("abc"))
print(stringSplosion("ab"))
