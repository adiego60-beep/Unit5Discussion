# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
## Unit 5 Implementation Summary

For this assignment, I implemented linear search and binary search algorithms in Python to compare how they locate values in different datasets.

I completed the linear search function by checking each element in order until the target was found or the list ended. I also implemented binary search using left, right, and middle indexes to repeatedly narrow the search range in a sorted list.

I tested both algorithms using a small dataset of student scores and a larger dataset containing 100,000 student record IDs. Both methods returned the correct indexes, but binary search required fewer comparisons when searching through the larger dataset.

I also tested edge cases involving an empty list, a single-element list, and a value at the end of a list. These tests demonstrated how both algorithms handled different search conditions.

For my real-world example, I created a student ID lookup scenario to show how searching algorithms could be used in a school information system.

Overall, this assignment helped me understand the differences between O(n) and O(log n) time complexity and why the organization of data matters when selecting a search algorithm.