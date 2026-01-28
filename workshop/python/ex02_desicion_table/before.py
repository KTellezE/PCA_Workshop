def shipping_cost(country, weight_kg, is_express, is_member):
    if weight_kg <= 0:
        raise ValueError("weight")

    cost = 0

    if country == "MX":
        cost = 99 if weight_kg <= 1 else 149 if weight_kg <= 5 else 249
        if is_express:
            cost += 80
    elif country == "US":
        cost = 7 if weight_kg <= 1 else 11 if weight_kg <= 5 else 19
        if is_express:
            cost += 10
    else:
        cost = 15 if weight_kg <= 1 else 25 if weight_kg <= 5 else 40
        if is_express:
            cost += 15

    if is_member:
        cost *= 0.9

    return round(cost, 2)