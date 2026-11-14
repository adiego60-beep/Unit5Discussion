
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each item starting at index 0.
    for i in range(len(lst)):

        # Return the index when a match is found.
        if lst[i] == target:
            return i

    # If no match exists, return -1.
    # Linear search is O(n) because it may need to
    # examine every item before finishing.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Set the boundaries of the sorted list.
    left = 0
    right = len(lst) - 1

    # Continue while there are items left to search.
    while left <= right:

        # Find the middle position.
        mid = left + (right - left) // 2

        # Return the index if the target is found.
        if lst[mid] == target:
            return mid

        # Ignore the left half when the target is larger.
        elif lst[mid] < target:
            left = mid + 1

        # Ignore the right half when the target is smaller.
        else:
            right = mid - 1

    # Return -1 when no matching item exists.
    # Binary search is O(log n) because each iteration
    # eliminates approximately half the remaining items.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted list of student scores.
    small_scores = [55, 67, 72, 81, 90, 95]

    # Search for an existing score.
    existing_score = 81

    print("Scores:", small_scores)
    print("Searching for:", existing_score)

    print("Linear search index:",
          linear_search(small_scores, existing_score))
    print("Binary search index:",
          binary_search(small_scores, existing_score))

    # Both searches should return index 3.
    # The score 81 is stored at that position.

    # Search for a score that is not in the list.
    missing_score = 76

    print("\nSearching for missing score:", missing_score)
    print("Linear search index:",
          linear_search(small_scores, missing_score))
    print("Binary search index:",
          binary_search(small_scores, missing_score))

    # Both searches should return -1 because
    # the score 76 is not in the dataset.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create 100,000 sorted student record IDs.
    large_scores = list(range(1, 100001))

    # Choose a value near the end of the list.
    large_target = 99999

    print("Dataset size:", len(large_scores))
    print("Searching for:", large_target)

    # Run both algorithms on the same dataset.
    linear_result = linear_search(large_scores, large_target)
    binary_result = binary_search(large_scores, large_target)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both searches return index 99998.
    # Linear search checks items sequentially and may
    # require almost 100,000 comparisons.
    # Binary search repeatedly cuts the remaining
    # search range in half, requiring far fewer checks.

    print("\nPerformance Analysis:")
    print("Linear search: O(n)")
    print("Binary search: O(log n)")
    print("Binary search scales better for large sorted datasets.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list.
    # Both searches return -1 because no values exist.
    empty_scores = []

    print("\nEmpty list:")
    print("Linear:", linear_search(empty_scores, 81))
    print("Binary:", binary_search(empty_scores, 81))

    # Edge Case 2: Single-element list.
    # Both searches return index 0 when the value matches.
    single_score = [81]

    print("\nSingle-element list:")
    print("Linear:", linear_search(single_score, 81))
    print("Binary:", binary_search(single_score, 81))

    # Edge Case 3: Target at the last position.
    # Linear search checks every element before finding it.
    # Binary search can eliminate several elements at once.
    print("\nLast-position search:")
    print("Linear:", linear_search(small_scores, 95))
    print("Binary:", binary_search(small_scores, 95))

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================

    print("\n=== REAL-WORLD APPLICATION ===")

    # A school administrator needs to locate a student
    # record using a unique student ID.
    student_ids = [1001, 1005, 1012, 1020, 1033, 1045]
    target_id = 1033

    print("Student IDs:", student_ids)
    print("Searching for student ID:", target_id)

    print("Linear search index:",
          linear_search(student_ids, target_id))
    print("Binary search index:",
          binary_search(student_ids, target_id))

    # Both algorithms find the student at index 4.
    # Linear search works even if the IDs are unsorted.
    # Binary search is faster on large sorted ID lists.
    # However, maintaining sorted data may require
    # additional preparation when new records are added.

    print("\nSearch Comparison:")
    print("Linear search works with sorted or unsorted data.")
    print("Binary search requires sorted data.")
    print("Linear search is useful for small or changing lists.")
    print("Binary search is useful for large sorted collections.")


if __name__ == "__main__":
    main()
