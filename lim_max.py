def sort_dict(d, type="keywise", order="asc"):
    """
    Sorts a dictionary by keys or values in ascending or descending order.
    
    Args:
        d: The dictionary to sort
        type: The type of sorting - 'keywise' or 'valuewise'
        order: The order of sorting - 'asc' or 'desc'
        
    Returns:
        A new sorted dictionary
    """
    reverse = order.lower() == "desc"
    
    if type.lower() == "keywise":
        # Sort by keys
        sorted_items = sorted(d.items(), key=lambda x: x[0], reverse=reverse)
    else:  # valuewise
        # Sort by values
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=reverse)
    
    # Create a new dictionary from the sorted items
    return dict(sorted_items)

def sums_by_quarter(monthly_values):
    """
    Calculates sums of values by quarters from a list of monthly values.
    
    Args:
        monthly_values: A list of 12 numbers representing monthly values
        
    Returns:
        A list of 4 numbers representing quarterly sums
    """
    if len(monthly_values) != 12:
        return []
        
    quarterly_sums = []
    
    # Process each quarter (3 months at a time)
    for i in range(0, 12, 3):
        quarter_sum = sum(monthly_values[i:i+3])
        quarterly_sums.append(quarter_sum)
        
    return quarterly_sums

def count_frequency(names):
    """
    Counts the frequency of each name in a list and returns a sorted dictionary.
    
    Args:
        names: A list of name strings
        
    Returns:
        A dictionary with names as keys and their counts as values, sorted alphabetically
    """
    # Count occurrences of each name
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
    # Sort the dictionary by keys
    sorted_counts = dict(sorted(name_counts.items()))
    
    return sorted_counts

def get_path_description(path):
    """
    Returns a description of the selected path using conditional expressions.
    
    Args:
        path: A string representing the selected path
        
    Returns:
        A string description of the path
    """
    return (
        "This is the main path" if path == "main" else
        "This is the alternative path" if path == "alt" else
        "This is the emergency path" if path == "emergency" else
        "This is the default path" if path == "default" else
        "Unknown path"
    )

def forest_adventure(path):
    """
    Simulates a forest adventure with different path choices.
    
    Args:
        path: A string representing the chosen path ('left', 'center', or 'right')
        
    Returns:
        A string describing the outcome of the chosen path
    """
    if path == "left":
        return "You found a treasure chest!"
    elif path == "center":
        return "You discovered a magical fountain."
    elif path == "right":
        return "You encountered friendly forest creatures."
    else:
        return "Invalid path choice. Please choose 'left', 'center', or 'right'."

