def process_orders(orders):
    total = 0
    for o in orders:
        if o.get("status") == "cancelled":
            print("skip", o.get("id"))
            continue
        qty = int(o.get("qty", 0))
        price = float(o.get("price", 0))
        subtotal = qty * price
        if subtotal > 1000:
            subtotal *= 0.95
        total += subtotal
        print("order", o.get("id"), "subtotal", subtotal)
    print("total", total)
    return round(total, 2)