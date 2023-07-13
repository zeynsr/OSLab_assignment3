import random
words_bank = ['tree','book','python','sadjad','linux','oslab','windows','java','mac']
word = random.choice(words_bank)
test_time = len(word)
user_true_chars = []
while True:
    win = 1
    for char in word :
        if char in user_true_chars:
            print(char, end = '')
        else :
            print('- ', end = '')
            win = -1
    if win == 1:
        print('\nyou win')
        break
    user_char = input('\nenter a character :')
    if user_char in word :
        user_true_chars.append(user_char)
        print('✅')
    else:
        test_time -= 1
        print('❌')

    if test_time == 0:
        print('Game Over !')
        break
