

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # first value in the value tuple is price of the item, second is the special offer if there is one (qty and the offer price)
    # sku -> (price, special_offer)
    # special offer is a tuple (qty, special_price) or None
    # Note: can be further refactored with the use of nested dicts for better readability
    price_table = {
        'A': (50, (3, 130)),
        'B': (30, (2, 45)),
        'C': (20, None),
        'D': (15, None)
    }

    def calculate_item_cost(sku, qty):
        if sku not in price_table:
            return None
        
        item_price = price_table[sku][0]
        special_offer = price_table[sku][1]

        if special_offer:
            offer_qty = special_offer[0]
            offer_price = special_offer[1]
            count = qty // offer_qty
            remaining = qty % offer_qty
            return (count * offer_price) + (remaining * item_price)
        else:
            return qty * item_price


    


