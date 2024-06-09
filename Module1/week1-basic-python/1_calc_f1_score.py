def calc_f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int')
    elif not isinstance(fp, int):
        print('fp must be int')
    elif not isinstance(fn, int):
        print('fn must be int')
    elif tp <= 0 or fp <= 0 or fn <= 0:
        print('tp, fp, fn must be greater than zero')
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * (precision * recall) / (precision + recall)

        print(f'Precision is {precision}')
        print(f'Recall is {recall}')
        print(f'f1-score is {f1_score}')

print('Example 1')
calc_f1_score(tp=2, fp=3, fn=4)

print('\nExample 2')
calc_f1_score(tp='a', fp=3, fn=4)

print('\nExample 3')
calc_f1_score(tp=2, fp='a', fn=4)

print('\nExample 4')
calc_f1_score(tp=2, fp=3, fn='a')

print('\nExample 5')
calc_f1_score(tp=2, fp=3, fn=0)

print('\nExample 6')
calc_f1_score(tp=2.1, fp=3, fn=0)

print(round(calc_f1_score(2, 4, 5), 2))