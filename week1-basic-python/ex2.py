import math
def is_number(n):
    try:
        float(n) # Type=casting the string to 'float'
                 # If string is not valid 'float',
                 # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True

def calc_activation_func():
    x = input('Input x: ')
    if is_number(x) == False:
        print('x must be a number')
    else:
        x = float(x) # convert x to float
        act_func_name = input('Input activation function (sigmoid | relu | elu): ')
        if act_func_name.lower() == 'sigmoid':
            print(f'sigmoid: f({x}) = {1 / (1 + math.exp(-x))}')
        elif act_func_name.lower() == 'relu':
            if x <= 0:
                print(f'relu: f({x}) = 0')
            else:
                print(f'relu: f({x}) = {x}')
        elif act_func_name.lower() == 'elu':
            if x <= 0:
                print(f'elu: f({x}) = {0.01 * (math.exp(x) - 1)}')
            else:
                print(f'elu: f({x}) = {x}')
        else:
            print(f'{act_func_name} is not supported')

if __name__ == '__main__':
    calc_activation_func()