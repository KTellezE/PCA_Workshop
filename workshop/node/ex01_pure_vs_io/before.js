function processOrders(orders) {
    let total = 0;
    for (const o of orders) {
    if (o.status === "cancelled") {
        console.log("skip", o.id);
        continue;
    }
    const qty = parseInt(o.qty ?? 0, 10);
    const price = parseFloat(o.price ?? 0);
    let subtotal = qty * price;
    if (subtotal > 1000) subtotal *= 0.95;
    total += subtotal;
    console.log("order", o.id, "subtotal", subtotal);
    }
    console.log("total", total);
  return Math.round(total * 100) / 100;
}

module.exports = { processOrders };