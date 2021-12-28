##syntax to write the function to calculate implied volatility for Call Option and Put Option would be —
##mibian.BS([Underlying Price, Call Price or Strike Price, Interest Rate, Days To Expiration], Call / Put Price)

# Contract # = '1C03 DV0E0
import mibian

c = mibian.BS([0, 0, .001, 26], callPrice= 6.2)
print('Call Vol: ' + str(c.impliedVolatility))
print()

p = mibian.BS([6.025, 6.2, .001, 26], callPrice= 6.2)
print('Put Vol: ' + str(p.impliedVolatility))
print()      

c = mibian.BS([6.025, 6.2, .001, 26], volatility = 500)
print('Call Price: ' + str(c.callPrice))
print('Call Delta: ' + str(c.callDelta))
print('Call Theta: ' + str(c.callTheta))
print('Call Vega: ' + str(c.vega))
print('Call Gamma: ' + str(c.gamma))
print()
print()

p = mibian.BS([6.025, 6.2, .001, 26], volatility = 500)
print('Put Price: ' + str(p.callPrice))
print('Put Delta: ' + str(p.callDelta))
print('Put Theta: ' + str(p.callTheta))
print('Put Vega: ' + str(p.vega))
print('Put Gamma: ' + str(p.gamma))
print()
print()
