##syntax to write the function to calculate implied volatility for Call Option and Put Option would be —
##mibian.BS([Underlying Price, Call / Price Strike Price, Interest Rate, Days To Expiration], Call / Put Price)

# Contract # = '1C08 DUYD0
import mibian

c = mibian.BS([5.34, 5.6, 0, 64], callPrice= .19)
print('Call Vol: ' + str(c.impliedVolatility))
print()

p = mibian.BS([5.34, 5.6, 0, 64], callPrice= .19)
print('Put Vol: ' + str(p.impliedVolatility))
print()      

c = mibian.BS([5.34, 5.6, 0, 64], volatility = 33.203125)
print('Call Price: ' + str(c.callPrice))
print('Call Delta: ' + str(c.callDelta))
print('Call Theta: ' + str(c.callTheta))
print('Call Vega: ' + str(c.vega))
print('Call Gamma: ' + str(c.gamma))
print()
print()

p = mibian.BS([5.34, 5.6, 0, 64], volatility = 69.60)
print('Put Price: ' + str(p.callPrice))
print('Put Delta: ' + str(p.callDelta))
print('Put Theta: ' + str(p.callTheta))
print('Put Vega: ' + str(p.vega))
print('Put Gamma: ' + str(p.gamma))
print()
print()
