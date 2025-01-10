# Jan Berglund

# Veckouppgift 1
# Vecka 2, 8/1
# 2 Diskutera i grupp


# Defines a ticket price and how much
# money is available prior to purchase
ticket_price = 100 # biljettpris
initial_cash = 200 # pengar på fickan

# Calculate how much money is left post purchase
left_over_cash = initial_cash - ticket_price

print("Det blir " + str(left_over_cash) + " kronor över.")

# Calculate what half of what money is left will be
half_left_over = left_over_cash / 2

print("Hälften är: " + str(half_left_over) + " kr.")
