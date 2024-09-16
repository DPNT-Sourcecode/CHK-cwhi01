

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # first value in the value tuple is price of the item, second is the special offer if there is one (qty and the offer price)
    price_table = {
        'A': (50, (3, 130)),
        'B': (30, (2, 45)),
        'C': (20, None),
        'D': (15, None)
    }


