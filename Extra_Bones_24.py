def test_word():
    question = input('You want check polygrome ? (y/n): ')
    question = question.lower()
    if question == "y":
        sample = input("Provide test word: \n>>>")
        sample = sample.lower()
        print(is_palindrome(sample))
        test_word()
    elif question == "n":
        print('Bye!')
        quit()
    else:
        print("Y for yes or N for no, please.")
        test_word()


def is_palindrome(x):
    y = x[::-1]

    if x == y:
        return True
    elif x != y:
        return False

test_word()


