import io
from contextlib import redirect_stdout

from before import process_orders as b
from after import process_orders as a


def _run_and_capture(fn, orders):
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = fn(orders)
    return result, buf.getvalue()


def run():
    orders = [
        {"id": "1", "qty": "2", "price": "10"},
        {"id": "2", "qty": 1, "price": 2000},
        {"id": "3", "status": "cancelled", "qty": 10, "price": 999},
        {"id": "4", "qty": 0, "price": 100},
        {"id": "5", "price": 12.5},
    ]

    b_result, b_out = _run_and_capture(b, orders)
    a_result, a_out = _run_and_capture(a, orders)

    assert b_result == a_result, (b_result, a_result)
    assert b_out == a_out, (b_out, a_out)

    print("OK: comportamiento idéntico")


if __name__ == "__main__":
    run()
