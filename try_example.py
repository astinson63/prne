

try:
    x = 5 / 0
except Exception as e:
    print(f'This is an exception error: {e}')
else:
    print('this is run if there are no exceptions')
finally:
    print('this is always run at the end')
    
    