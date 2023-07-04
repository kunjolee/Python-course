# Positional arguments
# Keywords arguments
# You can't put a positional argument after a keyword or named argument (keyword parameters must go at the end)

def divided(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print('you fool')        


divided(divisor=15, dividend=0)