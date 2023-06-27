import sys

#It is possible to write programs that handle selected exception.
#In this example, the program will be executed until a input not numerical

while True:
    try:
        x = int(input('please, enter a number: '))
        break
    except ValueError:
        print('the value is not a valid number')

#the try clause - the code between try and except is executed
#if not occurs exception, the except clausule is skipped and the prgogram is finished
#if occurs exception, the except except clausule is executed

#a try may have more than one exception clausule, using "pass". exemple

while True:
    try:
        x = int(input('number 2: '))
        break
    except RuntimeError:
        pass
    except ValueError as exc:
        print('the value is not a valid number')
        print(type(exc))
        
#the try clausele may especify a variable after a excepiton name, like "exce"

while True:
    try:
        x = int(input('number 2: '))
        break
    except ValueError as exce:
        print('the value is not a valid number')
        print(type(exce))
        print(exc.args)
        
        
#The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


#for to execute this file: python .\8_erros_exceptions\3_handling_exceptions.py
