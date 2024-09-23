item_prices = [10, 20, 30]  
item_quantities = [2, 1, 3] 
discount_rate = 10  
tax_rate = 5  

subtotal = sum([price * quantity for price, quantity in zip(item_prices, item_quantities)])

discount_amount = (discount_rate / 100) * subtotal
discounted_total = subtotal - discount_amount

tax_amount = (tax_rate / 100) * discounted_total
total_cost = discounted_total + tax_amount

print("Subtotal: $", round(subtotal, 2))
print("Discount: $", round(discount_amount, 2))
print("Total after discount: $", round(discounted_total, 2))
print("Tax: $", round(tax_amount, 2))
print("Total cost: $", round(total_cost, 2))
