def get_list_stats(numbers):
    n = len(numbers)
    if n == 0:
        return None
    
    # Sum
    total = 0
    for num in numbers:
        total += num

    # Average
    avg = total / n
    
    # Min and Max
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    # Median
    sorted_nums = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]
        
    return total, avg, largest, smallest, median
