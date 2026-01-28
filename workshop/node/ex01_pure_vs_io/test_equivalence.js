const assert = require("node:assert/strict");
const { processOrders: b } = require("./before");
const { processOrders: a } = require("./after");

const orders = [
    { id: "1", qty: "2", price: "10" },
    { id: "2", qty: 1, price: 2000 },
    { id: "3", status: "cancelled", qty: 10, price: 999 },
    { id: "4", qty: 0, price: 100 },
    { id: "5", price: 12.5 },
];

assert.equal(b(orders), a(orders));
console.log("OK: comportamiento idéntico");