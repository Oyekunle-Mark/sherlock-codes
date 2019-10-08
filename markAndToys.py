def maximumToys(prices, k):
    # sort the prices
    sorted_prices = sorted(prices)
    spent = 0
    number_of_toys = 0

    # keep picking up toys until budget is exceeded
    for price in sorted_prices:
        spent += price

        # if spent is less than budget, increase the number of toys otherwise break out of the loop
        if spent < k:
            number_of_toys += 1
        else:
            break

    # return the number of toys mark can get for the budget
    return number_of_toys


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
