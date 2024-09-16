from typing import Dict, Tuple, Optional, List

PRICES: Dict[str, int] = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

OFFERS: Dict[str, int] = {
    'A': [(5,200), (3, 130)],
    'B': [(2, 45)]
}

DEALS: Dict[str, int] = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:



    # function to calculate the cost of a given item and quantity 
    def calculate_item_cost(sku: str, qty: int) -> Optional[int]:
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
        
    # count the items 
    item_counts: Dict[str, int] = {}

    if not isinstance(skus, str):
        return -1

    for sku in skus:
        item_counts[sku] = item_counts.get(sku, 0) + 1
    
    total = 0

    # calculate the total cost 
    for sku, qty in item_counts.items():
        item_cost = calculate_item_cost(sku, qty)
        if item_cost is None:
            return -1
        total += item_cost
    
    return total

    



    


