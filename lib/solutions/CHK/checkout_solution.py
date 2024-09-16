from typing import Dict, Tuple, Optional, List

# these consts below can be placed inside the function as well (or inside a class if need be in the OOP scenario)
PRICES: Dict[str, int] = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10
}

OFFERS: Dict[str, List[Tuple[int, int]]] = {
    'A': [(5,200), (3, 130)],
    'B': [(2, 45)]
}

DEALS: Dict[str, Tuple[int, str, int]] = {
    'E': (2, 'B', 1),
    'F': (2, 'F', 1)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    if not isinstance(skus, str):
        return -1

    # function to count the item quantities and store in a dict
    def count_items(skus: str) -> Optional[Dict[str, int]]:
        item_counts: Dict[str, int] = {}

        for sku in skus:
            if sku not in PRICES:
                return None
            item_counts[sku] = item_counts.get(sku, 0) + 1
        
        return item_counts

    # function to calculate the cost of a given item and quantity 
    # apply the best offer also
    def calculate_item_cost(sku: str, qty: int) -> Optional[int]:
        item_price = PRICES[sku]
        offers = OFFERS.get(sku)
        remaining = qty
        total = 0

        if offers:
            best_offers = offers[:]
            best_offers.sort(reverse=True)
            for offer_qty, offer_price in best_offers:
                num_offers = remaining // offer_qty
                total += num_offers * offer_price
                remaining %= offer_qty

        total += remaining * item_price
        return total
    
    # applies any special deals buy x get y free
    # not a pure function (i.e. modifies the original input - since variables passed by reference)
    def apply_deals(item_counts: Dict[str, int]) -> Dict[str, int]:

        for deal_item, (buy_qty, free_item, free_qty) in DEALS.items():
            
            if deal_item in item_counts and free_item in item_counts:
                num_deals = item_counts[deal_item] // buy_qty

                if num_deals > 0:
                    total_free = num_deals * free_qty
                    item_counts[free_item] = max(0, item_counts.get(free_item, 0)-total_free)
        
        return item_counts
    
    # fist do the counting and place in dict
    item_counts = count_items(skus)

    if item_counts is None:
        return -1
    
    # applhy any special deals 
    item_counts = apply_deals(item_counts)

    # calculate the final total cost 
    total = 0
    
    for item, qty in item_counts.items():
        total += calculate_item_cost(item, qty)
    
    return total

    



    


