def is_panildrome(s):
    return s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1]

print(is_panildrome("A man a plan a canal Panama"))
print(is_panildrome("ani"))
print(is_panildrome("Hello"))