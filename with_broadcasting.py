
# without using loops 
# It will br fast and easy for large dataset 

import numpy as np

prices = np.array([100,200,300,400,600,900,7000])

discount = 10

final_prices = prices - (prices * discount/100)

print(final_prices)