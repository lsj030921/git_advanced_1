# main.py
from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Dtermines if a number is even and return an even list.
    """
    # TODO: Implement even_list
    pass

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.
    """
    return sum(x*x for x in even_int_list)

# Main function
def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_ints = even_list(int_list)
    print(sum_of_squares_of_even(even_ints))

if __name__ == "__main__":
    main()