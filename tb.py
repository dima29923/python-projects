import random

answers = ['yolo!!!.','no what yo thinking!.','maybe bra!.','definitly.','ARE YOU CRAZY!','OMG NO!!!']


print('''
Welcome to the magic 8 ball! Enter your questions below:''')

while True:
        question = input('> ')

        answer = random.choice(answers)
        print(answer)
