n_r = {  1: 'I', 2:'II',3:'III',4: 'IV',5: 'V',6: 'VI',7:'VII',8:'VIII',9: 'IX',
        10: 'X',20: 'XX',30:'XXX',40: 'XL',50: 'L',60:'LX',70: 'LXX',80: 'LXXX',90: 'XC',
        100: 'C',200:'CC',300:'CCC',400: 'CD',500: 'D',600: 'DC',700:'DCC',800:'DCCC',900: 'CM',
        1000: 'M', 2000: 'MM', 3000:'MMM'}

def Number_to_Romany_converter(number):
    if number < 1 or number > 4000:
        print('error number')
        return None
    number = str(number)
    digit_list = []
    for digit in number:
        digit_list.append(int(digit))
    digit_list.reverse()
    multiplx_number = 1
    numbers_list = []
    for digit in digit_list:
        numbers_list.append(digit*multiplx_number)
        multiplx_number = int(multiplx_number * 10)
    roman_code = ''
    numbers_list.reverse()
    for number in numbers_list:
        if number != 0 :
            roman_code += n_r[number]
    print(roman_code)
    return(roman_code)
Number_to_Romany_converter(4)