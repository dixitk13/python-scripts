__author__ = 'Dixit_Patel'


def get_valid_palindromes(words):
    lst = []
    for word in words:
        if word[::-1] == word:
            lst.append(word)
    print(lst.sort())
    return lst

if __name__ == "__main__":

    marks1 = ["carburetor", "bankruptcy", "consider", "loophole", "grotesque"]
    marks = ["encouragement", "eye", "devour", "license", "library", "customer", "susus", "penalty", "radar", "precipice"]
    mark = ["encouragement","eye","obsolete","berserk","devour","license","library","customer","susus","penalty","bicycle","malayalam","radar","precipice"]


    print(get_valid_palindromes(mark))