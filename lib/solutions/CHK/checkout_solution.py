from typing import Dict, Tuple, Optional, List

PRICES: Dict[str, int] = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

OFFERS: Dict[str, List[Tuple[int, int]]] = {
    'A': [(5,200), (3, 130)],
    'B': [(2, 45)]
}

DEALS: Dict[str, Tuple[int, str, int]] = {
    'E': (2, 'B', 1)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    if not isinstance(skus, str):
        return -1

    # function to count the item quantities 
    def count_items(skus: str) -> Optional[Dict[str, int]]:
        item_counts: Dict[str, int] = {}

        for sku in skus:
            if sku not in PRICES:
                return None
            item_counts[sku] = item_counts.get(sku, 0) + 1
        
        return item_counts

    # function to calculate the cost of a given item and quantity 
    def calculate_item_cost(sku: str, qty: int) -> Optional[int]:
        item_price = PRICES[sku]
        offers = OFFERS.get[sku]
        remaining = qty
        total = 0

        if offers:
            pass

        total += remaining * item_price
        return total
        

    
    total = 0

    # calculate the total cost 
    for sku, qty in item_counts.items():
        item_cost = calculate_item_cost(sku, qty)
        if item_cost is None:
            return -1
        total += item_cost
    
    return total

    



    


