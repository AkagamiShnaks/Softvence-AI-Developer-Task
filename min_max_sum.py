def miniMaxSum(arr):
    """
    Find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
    
    Args:
        arr: list of 5 integers
    
    Prints:
        Two space-separated integers: minimum sum and maximum sum
    """
    # Calculate total sum of all 5 numbers
    total_sum = sum(arr)
    
    # Find min and max elements
    min_element = min(arr)
    max_element = max(arr)
    
    # Minimum sum: exclude the largest element
    min_sum = total_sum - max_element
    
    # Maximum sum: exclude the smallest element
    max_sum = total_sum - min_element
    
    print(f"{min_sum} {max_sum}")

# Test with the sample input
if __name__ == "__main__":
    # Sample input: 1 2 3 4 5
    sample_input = [1, 2, 3, 4, 5]
    print("Sample test:")
    miniMaxSum(sample_input)
    
    # Interactive input
    print("\nEnter 5 space-separated integers:")
    try:
        user_input = input().strip()
        numbers = list(map(int, user_input.split()))
        
        if len(numbers) != 5:
            print("Error: Please provide exactly 5 integers")
        else:
            miniMaxSum(numbers)
    except ValueError:
        print("Error: Please enter valid integers")
    except EOFError:
        print("No input provided")
