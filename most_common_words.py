def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        line = ""
        for i in f:
            line += i
        line = line.strip().split()
        line = [word.strip(".,") for word in line]
    return {word: line.count(word) for word in line if line.count(word) >= lower_limit}

print(most_common_words("comprehensions.txt", 3))