from typing import Dict, Tuple, Optional, List, Set

# these constants below can be placed inside the function as well (or inside a class if need be in the OOP scenario)
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
    
    # function to calculate the total group discounts 
    # a slightly inefficient algorithm (nested loops etc. - more than ideal time complexity), but extendable data structure for groups used  
    # more groups and conditions could be added 
    def calculate_group_discounts(adjusted_counts: Dict[str, int]) -> Dict[str, int]:

        total_discount = 0
        
        for group_items, size, group_price in GROUP_DISCOUNTS:
            item_prices = []

            for item in group_items:
                if item in adjusted_counts:
                    item_prices.extend([PRICES[item]] * adjusted_counts[item])
            
            item_prices.sort(reverse=True)
            num_groups = len(item_prices) // size
            normal_price = sum(item_prices)

            discount = num_groups * group_price
            remaining_items_start = num_groups * size
            remaining_price = sum(item_prices[remaining_items_start:])
            subtotal_discount = discount + remaining_price

            group_discount = normal_price - subtotal_discount

            total_discount += group_discount
    
        return total_discount


    # fist do the counting and place in dict
    item_counts = count_items(skus)

    if item_counts is None:
        return -1
    
    adjusted_counts = item_counts.copy()

    # adjust by applying any special deals and discounts etc.
    adjusted_counts = apply_deals(adjusted_counts)

    # calculate the final total cost 
    subtotal = sum(calculate_item_cost(item, qty) for item, qty in adjusted_counts.items())

    # calculate total discounts for groups and calculate the final price
    total_group_discounts = calculate_group_discounts(adjusted_counts)
    final_price = subtotal - total_group_discounts
    
    return final_price

    
# a few improvements could be made to this solution: 
# - not the most consistent solution, since I should have chosen one of the methods:
#   a) either calculate the raw total and then just subtract discounts
#   b) or modify the dict in place (or a copy of a dict) and then calculate the total
#  instead, I have kind of used a hybrid approach, which is not consistent. But I will submit it as it is due to time constraints
#  one of the functions applies deals, another calculates the discount to be subtracted

# testing can be more thorough
# currently I am just testing the results of the whole function
# but it would be more difficult to debug it if something is wrong in the individual functions
# maybe separating the individual discount functions and placing them outside of the checkout function (as if they are all just part of a class) would be more beneficial for debugging purposes

# some inefficiencies in algorithms that could potentially be improved
# overall, I have prioritised extendability over time complexity/efficiency or memory complexity
# i believe this solution is quite extendable and readable (i.e. it is easy to extend in the future)
# but if speed/efficiency is more important, this could be modified (maybe use of different data structure for more efficient data manipulation)


    


