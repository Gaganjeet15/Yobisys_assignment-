def flatten(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, recurse into it
            yield from flatten(element)
        else:
            # If it's not a list, yield the element
            yield element

# Example usage:
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
for item in flatten(nested):
    print(item)