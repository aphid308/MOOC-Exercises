def balanced_brackets(my_string: str):
    brackets = "([])"
    filtered = ""
    for char in my_string:
        filtered += char if char in brackets else ""

    if len(filtered) == 0:
        return True

    open_round = filtered[0] == '('
    closed_round = filtered[-1] == ")"
    open_square = filtered[0] == "["
    closed_square = filtered[-1] == "]"

    if not (open_round and closed_round) and not (open_square and closed_square):
        return False

    return balanced_brackets(filtered[1:-1])

# ok = balanced_brackets("(((())))")
# print(ok)
#
# # there is one closing bracket too many, so this produces False
# ok = balanced_brackets("()())")
# print(ok)
#
# # this one starts with a closing bracket, False again
# ok = balanced_brackets(")()")
# print(ok)
#
# # this produces False because the function only handles entirely nested brackets
# ok = balanced_brackets("()(())")
# print(ok)

ok = balanced_brackets("([([])])")
print(ok)

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)

# this is no good, the closing bracket doesn't match
ok = balanced_brackets("(()]")
print(ok)

# different types of brackets are mismatched
ok = balanced_brackets("([bad egg)]")
print(ok)