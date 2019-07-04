import string


def is_name_gessed(secret_word, gess):
    p = 0
    for i in gess:
        for k in secret_word:
            if i == k:
                p = p + 1
    return p == len(secret_word)

def word_gessed(secret_word,gess):
    if is_name_gessed(secret_word,gess) == True:
        return secret_word
    else:
        j = ''
        for i in secret_word:
            if i not in gess:
                j = j + '_ '
            else:
                j = j + i
        return j



def available_letters(secret_word):
    available_letters_left = ''
    all_letters = string.ascii_lowercase
    urgess = word_gessed(secret_word,gess)
    for i in urgess:
        if i in all_letters:
            all_letters = all_letters.replace(i,"")
    return available_letters_left + all_letters



def hangman(secret_word):
    gess_remaing = 6
    gess = []
    correct_gess = []
    while gess_remaing > 0:
        letter_gessed = input("input a letter:")
        gess.append(letter_gessed)
        if letter_gessed not in secret_word:
            gess_remaing = gess_remaing - 1
            print("Oops! That letter is not in my word:")
            print(word_gessed(secret_word, gess))
            if gess_remaing == 0:
                return "Sorry, you ran out of guesses. The word was " + secret_word + "."
        else:
            gess_remaing = gess_remaing
            correct_gess.append(letter_gessed)
            if is_name_gessed(secret_word, gess) == True:

                print(is_name_gessed(secret_word, gess))
                print(word_gessed(secret_word, gess))
                score = len(correct_gess) * gess_remaing
                print("Congratulations, you won! your score is")
                return score
            else:
                print("correct gess:")
                print(word_gessed(secret_word, gess))
    return word_gessed(secret_word, gess)


# name = "hellena"
# gess = ['t','p','h','a','n','l','k']
# n = is_name_gessed(name,gess)
# k = word_gessed(name,gess)
# h = available_letters(name)
# print(n)
# print(k)
# print(h)


name = "hellena"
hang = hangman(name)
print(hang)





