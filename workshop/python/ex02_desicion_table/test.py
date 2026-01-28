import itertools
from before import shipping_cost as b
from after import shipping_cost as a


def run():
    countries = ["MX", "US", "CA"]
    weights = [0.5, 1, 2, 5, 6]
    flags = [(False, False), (True, False), (False, True), (True, True)]

    for c, w, (ex, mem) in itertools.product(countries, weights, flags):
        assert b(c, w, ex, mem) == a(c, w, ex, mem), (c, w, ex, mem)

    print("OK: comportamiento idéntico")


if __name__ == "__main__":
    run()