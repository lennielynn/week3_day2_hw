# <p>Write an anonymous function that sorts this list by the last name..
# Hint: Use the ".sort()" method and access the key"</b></p>

# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield',
# 'David hassELHOFF']`


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda last_n: last_n.split(" ")[-1].lower()[0])
print(author)