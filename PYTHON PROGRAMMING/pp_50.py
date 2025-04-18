# Write a program that will filter a list of tuples. For testing purposes, a list of
# tuples is given:
L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)]


def get_price_filtered_list(filtering_criterion: int, items: list[tuple[str, int]]) -> list[tuple[str, int]]:

    # Function returns filtered list - all items that have price lower or equall than filtering_criterion should be filtered out.

    # Parameters:
    # filtering_criterion: number indicating the maximal price to be filtered out
    # items: iterable

    # Returns:
    # filtered list of tuples (product together with its price)

    price_filtered = []
    for item in items:
        if item[1] > filtering_criterion:
            price_filtered.append(item)
    return price_filtered


print(get_price_filtered_list(filtering_criterion=15, items=L1))
