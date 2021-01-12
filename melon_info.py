"""Print out all the melons in our inventory."""


from melons import (melon_names, melon_seedlessness, melon_prices, melon_flesh_color,
                    melon_weight, melon_rind_color)


def print_melon(name, seedless, price, flesh, weight, rind):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'not seedless'
    if seedless:
        have_or_have_not = 'seedless'

    print(f'{name}s are {have_or_have_not}, cost ${price: .2f}, have {flesh} flesh, weigh about {weight} pounds and have {rind} rind.')


for i in melon_names:
    print_melon(melon_names[i],
                melon_seedlessness[i],
                melon_prices[i],
                melon_flesh_color[i],
                melon_weight[i],
                melon_rind_color[i]
                )
