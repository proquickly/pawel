def cartesian_product(lists):
    # Start with an empty result containing one empty list
    result = [[]]

    for current_list in lists:
        new_result = []
        for item in current_list:
            for product in result:
                new_result.append(product + [item])
        result = new_result

    return result


# Example usage
lists = [['a', 'b'], ['1', '2'], ['X', 'Y']]
product = cartesian_product(lists)

# Print the results
print("Cartesian product:")
for p in product:
    print(p)

# Print the total number of combinations
print(f"\nTotal number of combinations: {len(product)}")
