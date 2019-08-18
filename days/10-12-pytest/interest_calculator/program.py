def main():
    try:
        principal_amount= float(input('How much money are you investing?'))
    except ValueError:
        print('Must be amount in numbers')
        main()
    
    years= int(input('For how many years?'))
    interest= float(input('What is the interest rate? (1% = 0.01)'))
    end_amount= calculate_interest(principal_amount, years, interest)
    print('At the end of your investment, you will have {} rands.'.format(end_amount))


def calculate_interest(principal_amount, years, interest):
    return round(principal_amount*(1+ interest)** years, 2)

def show_header():
    print('-------------------------')
    print('     Interest Calculator')
    print('-------------------------')

if __name__ == "__main__":
    main()

