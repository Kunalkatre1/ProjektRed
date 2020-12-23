import sys
from random import randint

if __name__ == "__main__":

    count = 0
    _min = int(sys.argv[1])
    _max = int(sys.argv[2])
    selected_no = randint(_min, _max)

    print(selected_no)

    while 1:
        try:
            count += 1
            num = int(input('Enter your guess: '))
            if num == selected_no and count > 2:
                print(
                    f'You guessed the correct no. {selected_no}. It took {count} attempts for you to guess this no.')
                break
            elif num == selected_no and count < 2:
                print(
                    f'Congratulations! You guessed no. at first attempt. No. guessed by you is {selected_no}')
                break
            else:
                continue
        except ValueError:
            print("Please enter a valid integer")
            continue
