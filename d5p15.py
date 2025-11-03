#Monthly sales (in units) for 3 products over 6 motns
import numpy as np
sales=np.array([
    [120,135,150,160,145,135],
    [80,95,100,110,105,115],
    [150,160,170 ,175,180,190]
])
total_sales=sales.sum(axis=1)
print("total sales:",total_sales)
avg_sales=sales.mean(axis=1)
print("Average sales:",avg_sales)
high_sales_month=sales.argmax(axis=1)+1
print("Highest sales:",high_sales_month)
best_product_index=total_sales.argmax()
print("best performing:",best_product_index)







