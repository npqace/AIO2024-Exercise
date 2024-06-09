import math
import random

def regression_loss():
    num_samples = input('Input number of samples (integer number) which are generated: ')

    # check if num_samples is a number
    if num_samples.isnumeric() == False:
        print('number of samples must be an integer number')
    
    num_samples = int(num_samples)
    loss_name = input('Input loss name: ')
    for i in range(num_samples):
        y_predict = random.uniform(0,10)
        y_target = random.uniform(0, 10)

        if loss_name.upper() == 'MAE':
            loss = abs(y_predict - y_target)
            print(f'loss name: MAE, sample {i+1}, pred: {y_predict}, target: {y_target}, loss: {loss}')
        elif loss_name.upper() == 'MSE':
            loss = (y_predict - y_target) ** 2
            print(f'loss name: MSE, sample {i+1}, pred: {y_predict}, target: {y_target}, loss: {loss}')
        elif loss_name.upper() == 'RMSE':
            loss = math.sqrt((y_predict - y_target) ** 2)
            print(f'loss name: RMSE, sample {i+1}, pred: {y_predict}, target: {y_target}, loss: {loss}')
    if loss_name.upper() == 'RMSE':
        print(f'final loss: {loss * math.sqrt(1/num_samples)}')

if __name__ == '__main__':
    regression_loss()