tksAdult=200 # $10 each
priceAdult = 10

tksChild=100 # $6 each
priceChild = 6


print("Movie Name: ")
print(f'Adult Tickets: {tksAdult: 3}' )
print("Child Tickets: ", tksChild)
print("Theater Profit: ")
print("Studio Profit: ")

print(f'Gross Profit: ${tksAdult * priceAdult + tksChild * priceChild : 7,.2f}')
grossProfit = (tksAdult * priceAdult) + (tksChild * priceChild)
print(f'Gross Profit: ${grossProfit: 7,.2f}')

'''
Can calculations like multiplication and addition be made during the
string formatting portion?

print (f'example {price1 + price2 : 10.2f'}
or
print (f'example {price1 * price2 : 10.2f'}

'''
