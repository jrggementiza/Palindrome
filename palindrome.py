""" A simple program that asks you to enter a word and returns if its a palindrome or not """
import generic

def palindrome(word):
    first = word[0]
    last = word[-1]
    middle = word[1:-1]
    
    if len(word) == 1:
        print(f'{word} is Palindrome')
        return True
    elif len(word) == 2 and first == last:
        print(f'{word} is Palindrome')
        return True
    elif word == word[::-1]:
        print(f'{word} is Palindrome')
        return True
    else:
        print(f'{word} is Not Palindrome')
        return False


def word_input():
    while True:
        try:
            word = input('enter a word: ')
            assert len(word) > 1
        except AssertionError:
            print('no word entered! try again! : ')
        else:
            return word


def main():
    run_program = True
    while run_program == True:
        word = word_input()
        palindrome(word)
        run_program = generic.run_again('Would you like to enter another word? : ')


if __name__ == '__main__':
    main()

