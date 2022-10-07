import io

letters = {"a" : "", "b" : "", "c" : "", "d" : "", "e" : "", "f" : "w", "g" : "", "h" : "", "i" : "", "j" : "",
 "k" : "", "l" : "", "m" : "", "n" : "", "o" : "", "p" : "", "q" : "", "r" : "c", "s" : "", "t" : "",
 "u" : "o", "v" : "", "w" : "", "x" : "", "y" : "", "z" : "", ".": ".", "/" : "/", "0":"0" ,"4":"4", "5":"5", "_": "_"}

def keisar(string):
    returned = ""
    for letter in string:
        returned += letters[letter]
    return returned

print(keisar("fff.rmo.ru/q4yyh_5dtt0c"))


"""with open('text.txt', 'w') as f:
    abc = "abcdefghijklmnopqrstuvwxyz"
    f.write("{")
    for letter in abc:
        f.write(f'"{letter}" : "", ')
    f.write("}")
    """