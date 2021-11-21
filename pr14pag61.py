s1 = (input("Introdu primul sir de caractere: "))
s2 = (input("Introdu al doilea sir de caractere: "))
a = set()
c = []
d = set()
for i in s1:
    for x in s2:
        a.add(i)
        a.add(x)
        if i == x:
            c.extend([i])
        if (i in s1) and (i not in s2 ):
            d.add(i)
print("Care se intalnesc cel putin in unul dintre siruri ", a)
print("Ce se intalnesc in abmele ", c)
print("Ce se intalnesc doar in primul sir ", d)