# This program counts the occurrences of a specific element in a list.

def count_occurrences(lst, element):
    return lst.count(element)

# Example usage:
lst = [1, 2, 3, 4, 2, 2, 5]
element = 2
print(f"The element {element} occurs {count_occurrences(lst, element)} times in the list.")
