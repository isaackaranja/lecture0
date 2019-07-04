def hangman(secret_word):
    gess_remaing = 6
    gess = []
    while gess_remaing > 0:
        letter_gessed = input("input a letter:")
        gess.append(letter_gessed)
        if letter_gessed not in secret_word:
            gess_remaing = gess_remaing - 1
            j = is_name_gessed(secret_word, gess)
            p = word_gessed(secret_word, gess)
            c = available_letters(secret_word)
            return j
            return p
            return c
        else:
            gess_remaing = gess_remaing
            j = is_name_gessed(secret_word, gess)
            if j == True:
                p = word_gessed(secret_word, gess)
                c = available_letters(secret_word)
                return True
                return p
                return c
            else:
                return is_name_gessed(secret_word, gess)
                return word_gessed(secret_word, gess)
                return available_letters(secret_word)
