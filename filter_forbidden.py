def filter_forbidden(string: str, forbidden: str):
    return "".join([char for char in string if char not in forbidden])
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)