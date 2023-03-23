#the switch statement is a optional the if
#instead of using if..elif..elif...elif 

status = 400

match status:
    case 400:
        print('Error 400')
    case 404:
        print('Erro 404')
    case 500:
        print('Error 500')
    case _:
        print('none option') #in case of none option above
        
        