import pandas as pd
import random

pd.set_option('display.max_colwidth', None)
prog_exe = ''


def parse_questions(choice, filepath):
    if choice == 'exl':
        return pd.read_excel(filepath)
    return pd.read_csv(filepath)


while prog_exe != 'n':
    try:
        choice = str(input('Type Exl or CSV')).lower()
        file_path = str(input('Insert Excel File Path + type (.xlsx/.csv)'))
        df = parse_questions(choice, file_path)
    except(FileNotFoundError,):
        print('File not found, insert correct path/filename')
        df = file_path = str(input('Insert Correct File Path/Name'))

    row_count = [x for x in range(1, len(df.index) + 1)]
    correct = [0]

    print('Total Questions = ', row_count[-1])

    while row_count:
        have_answered = ''
        check_answer = ''
        curr_number = random.randint(0, len(row_count))
        x = int(row_count[curr_number])
        curr_question = df.loc[df['No'] == x]
        print(curr_question['Question'].to_string(index=False))
        while have_answered != 'y':
            have_answered = str(input('Want to see answer? type "y"')).lower()
        print(curr_question['Answer'].to_string(index=False))
        print('From ', curr_question['Source'].to_string(index=False))
        print('Did you get it correct?')
        check_answer = input('Type "y" if correct or "n" if incorrect')
        if check_answer == 'y':
            correct[0] += 1
        row_count.remove(x)
        print('Next Questions ... ')
        print('-' * 20)
    print('Total Correct = ', correct[0], '/', len(df.index) + 1)
    prog_exe = str(input('Do you want to try again? type "n" to exit')).lower()