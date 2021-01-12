"""Print out all the melons in our inventory."""


from melons import (melon_names, melon_seedlessness, melon_prices, melon_flesh_color,
                    melon_weight, melon_rind_color)


def print_melon(name, seedless, price, flesh, weight, rind):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'Not Seedless'
    if seedless:
        have_or_have_not = 'Seedless'

    print(f'{name}s are {have_or_have_not} and cost ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i],
                melon_seedlessness[i],
                melon_prices[i],
                melon_flesh_color[i],
                melon_weight[i],
                melon_rind_color[i]
                )
