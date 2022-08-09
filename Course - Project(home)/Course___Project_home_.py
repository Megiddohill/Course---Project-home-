
def get_name():
    name = input("What is your name? Enter 'End' to quit: ")
    return name

def get_hours():
    hours = int(input("Enter hours worked this week: ")) #Create a function that will input and return total hours and is called inside the loop.
    return hours

def get_wage():
    wage = float(input("Enter your hourly wage: ")) #Create a function that will input and return the hourly rate and is called inside the loop.
    return wage

def get_tax():
    tax = float(input("Enter income tax_rate: ")) #Create a function that will input and return the income tax rate and is called inside the loop.
    return tax

def gross_pay(hours, wage): # Gross pay
    gross = hours * wage
    return gross

def taxed(gross, tax): #Amount in Taxes
    amount_taxed = gross * tax
    return amount_taxed

def net_pay(gross, amount_taxed): # Net Pay
    net = gross - amount_taxed
    return net

def print_data(name, hours, wage, tax, amount_taxed, gross, net):
    print(name, f'{hours:,.2f}', f'{wage:,.2f}', f'{tax:,.2f}', f'{amount_taxed:,.2f}', f'{gross:,.2f}', f'{net:,.2f}')

def print_totals(Tot_emp, tot_hours, tot_gross, tot_taxed, tot_net ):
    print()
    print(f'Total number of employees: {tot_emp}')
    print(f'Total number of hours: {tot_hours:,.2f}')
    print(f'Total gross wage: {tot_gross:,.2f}')
    print(f'Total taxes deducted: {tot_taxed:,.2f}')
    print(f'Total net pay: {tot_net:,.2f}')

if __name__ == "__main__":
    tot_emp = 0
    tot_hours = 0.00
    tot_gross = 0.00
    tot_taxed = 0.00
    tot_net = 0.00


    while True:
    
        name = get_name()
        if (name.upper() == "END"):
            break
        hours = get_hours()
        wage = get_wage()
        tax = get_tax()
        gross = gross_pay(hours, wage)
        amount_taxed = taxed(gross, tax)
        net = net_pay(gross, amount_taxed)
        print_data(name, hours, wage, tax, amount_taxed, gross, net)
        tot_emp += 1
        tot_hours += hours
        tot_gross += gross
        tot_taxed += amount_taxed
        tot_net += net

        print_totals(tot_emp, tot_hours, tot_gross, tot_taxed, tot_net )

    
