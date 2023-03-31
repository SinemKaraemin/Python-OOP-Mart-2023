def reverse_text(string):
    for ch in reversed(string):
        yield ch


for char in reverse_text("step"):
    print(char, end='')
