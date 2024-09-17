from typing import Dict, Tuple, Optional, List, Set

# these consts below can be placed inside the function as well (or inside a class if need be in the OOP scenario)

PRICES: Dict[str, int] = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
}

OFFERS: Dict[str, List[Tuple[int, int]]] = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(5, 45), (10, 80)],
    'K': [(2, 150)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(2, 90),(3, 130)]
}

DEALS: Dict[str, Tuple[int, str, int]] = {
    'E': (2, 'B', 1),
    'F': (2, 'F', 1),
    'N': (3, 'M', 1),
    'R': (3, 'Q', 1),
    'U': (3, 'U', 1)
}

# for better extendability in the future 
GROUP_DISCOUNTS: List[Tuple[Set[str], int, int]] = [({'S', 'T', 'X', 'Y', 'Z'}, 3, 45)]

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
    def apply_deals(adjusted_counts: Dict[str, int]) -> Dict[str, int]:

        for deal_item, (buy_qty, free_item, free_qty) in DEALS.items():

            if deal_item in adjusted_counts:
                if deal_item == free_item:
                    total_qty = adjusted_counts[free_item]
                    min_size = buy_qty + free_qty
                    num_deals = total_qty // min_size
                    remaining = total_qty % min_size

                    adjusted_counts[free_item] = (num_deals * buy_qty) + remaining
                else:
                    if free_item in adjusted_counts:
                        num_deals = adjusted_counts[deal_item] // buy_qty
                        total_free = num_deals * free_qty
                        adjusted_counts[free_item] = max(0, adjusted_counts.get(free_item, 0)-total_free)
        
        return adjusted_counts
    
    # applies any group discounts that may be present 
    # not a pure function (i.e. modifies the original input - since variables passed by reference)
    def apply_group_discounts(adjusted_counts: Dict[str, int]) -> Dict[str, int]:
        
        # slightly inefficient algorithm due to nested loops
        # but good in terms of extendability of the group discount options 
        for group_items, count, group_price in GROUP_DISCOUNTS:
            item_prices = []

            for item in group_items:
                if item in adjusted_counts:
                    item_prices.extend([PRICES[item]] * adjusted_counts[item])
            
            item_prices.sort()


    
    # fist do the counting and place in dict
    item_counts = count_items(skus)

    if item_counts is None:
        return -1
    
    adjusted_counts = item_counts.copy()

    # adjust by applying any special deals and discounts etc.
    adjusted_counts = apply_deals(adjusted_counts)
    adjusted_counts = apply_group_discounts(adjusted_counts)

    # calculate the final total cost 
    total = 0
    
    for item, qty in adjusted_counts.items():
        total += calculate_item_cost(item, qty)
    
    return total

    



    






