import numpy as np

# Braodcasting mean apply operation on entire array

price=np.array([350,270,600,120,900,320])
discount=15
final_price=price - (price*discount/100)

print("New Prices ",final_price)

