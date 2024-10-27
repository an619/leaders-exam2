def to_snake_case(s):
    s = s.replace(" ", "")
    result = s[0].lower()
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for l in s[1:]:
        if l in upper:
            result += "_" + l.lower()
        else:
            result += l.lower()
    return result

print(to_snake_case("aniBani"))
print(to_snake_case("TestControler"))
print(to_snake_case("MoviesAndBooks"))
print(to_snake_case("App7 Test"))
print(to_snake_case("1"))