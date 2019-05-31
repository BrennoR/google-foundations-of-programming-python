# withoutString


# O(|base|*|remove|)
def withoutString(base: str, remove: str) -> str:
    if not base or not remove:
        return base

    arr = list(base)
    remove = remove.lower()
    i = 0
    while i < len(arr) - len(remove) + 1:
        if arr[i].lower() == remove[0]:
            found = True
            for j in range(1, len(remove)):
                if arr[i + j].lower() != remove[j]:
                    found = False
                    break

            if found:
                del arr[i: i + len(remove)]
                i -= 1
        i += 1

    return "".join(arr)


print(withoutString("Hello there", "llo"))
print(withoutString("eeeHello there", "e"))
print(withoutString("Hello there", "x"))

