# 1. rész - Írj egy programot, ami verem segítségével ellenőrzi, hogy
# a felhasználó által beírt szövegben minden zárójelnek van-e párja!
# Például:
# Be: (()((())()))    Ki: helyes
# Be: ()((())         Ki: helytelen

s = input("Kérem a zárójelezést (): ") # pl (()((())()))


def zarojel_par_nezes(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "Helytelen"
            stack.pop()

    return "Helyes" if not stack else "Helytelen"
print(zarojel_par_nezes(s))

# 2. rész - Írd meg úgy a programot, hogy a szögletes zárójeleket is figyelje!
# Be: (()[([])()])    Ki: helyes
# Be: ()[(]]          Ki: helytelen

s = input("Kérem a zárójelezést ([]): ") # pl (()[([])()])

def zarojel_es_szogletes_zarojel_nezes(s):
    stack = []
    parok = {')': '(', ']': '['}

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != parok[char]:
                return "Helytelen"
            stack.pop()

    return "Helyes" if not stack else "Helytelen"

print(zarojel_es_szogletes_zarojel_nezes(s))
