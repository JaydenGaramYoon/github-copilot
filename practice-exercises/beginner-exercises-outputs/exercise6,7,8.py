## Exercise 6: Class Design

### Task: Create a simple class for managing a shopping cart.

### Instructions
# 1. Start with a class comment describing its purpose
# 2. Let Copilot suggest methods and properties
# 3. Include input validation

### Starting Code

# Shopping cart class for e-commerce application
# Should track items, quantities, and calculate totals
# Include methods for add, remove, update quantity, and get total

class ShoppingCart:
    def __init__(self):
    # Shopping cart class for e-commerce application
    # Methods: track items, quantities, and calculate totals
    # Include methods for add, remove, update quantity, and get total
    # make input validtion logic
    
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if not isinstance(name, str) or not name:
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    def update_quantity(self, name, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if name in self.items:
            self.items[name]['quantity'] = quantity
    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total
    
    

# how do i use the class to manage a shopping cart?
# add more test cases for edge cases
# add detailed expected results for each test case
# add test cases to test input validation
# add test case to test "raise ValueError("Item name must be a non-empty string.")
# add test case to test "raise ValueError("Price must be a non-negative number.")
# add test case to test "raise ValueError("Quantity must be a non-negative integer.")
# add test case to test adding item with zero quantity
# add test case to test updating item quantity to zero
# add test case to test removing item not in cart

cart = ShoppingCart()
cart.add_item("Apple", 0.5, 3)
cart.add_item("Banana", 0.3, 2)
print("Total:", cart.get_total())  # Expected: 2.1
cart.update_quantity("Apple", 5)
print("Total after updating Apple quantity:", cart.get_total())  # Expected: 3.1
cart.remove_item("Banana")
print("Total after removing Banana:", cart.get_total())  # Expected: 2.5
cart.update_quantity("Apple", 0)
print("Total after updating Apple quantity to 0:", cart.get_total())  # Expected: 0.0
cart.add_item("Orange", 0.4)
print("Total after adding Orange:", cart.get_total())  # Expected: 0.4
cart.add_item("Grapes", 1.0, 0)
print("Total after adding Grapes with 0 quantity:", cart.get_total())  # Expected: 0.4
# cart.add_item("", 1.0, 1)  # Should raise ValueError
# cart.add_item("Mango", -1.0, 1)  # Should raise
# cart.add_item("Pineapple", 1.0, -2)  # Should raise ValueError
    

## Exercise 7: Algorithm Implementation

### Task: Implement a binary search algorithm with Copilot's help.

### Instructions
# 1. Write a clear comment about the algorithm
# 2. Specify time complexity requirements
# 3. Include edge case handling

### Starting Code

# Binary search implementation
# Search for target in sorted array
# Time complexity: O(log n)
# Returns: index of target if found, -1 if not found
# Handles empty arrays and single-element arrays
def binary_search(arr, target):
    # Let Copilot implement the algorithm
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
# how do I test this function?
    return -1
# Test cases
print(binary_search([], 5))  # Expected: -1 (empty array)
print(binary_search([3], 3))  # Expected: 0 (single-element array, found)
print(binary_search([1, 2, 3, 4, 5], 3))  # Expected: 2 (found)
print(binary_search([1, 2, 3, 4, 5], 6))  # Expected: -1 (not found)
print(binary_search([1, 3, 5, 7, 9], 1))  # Expected: 0 (found at start)
print(binary_search([1, 3, 5, 7, 9], 9))  # Expected: 4 (found at end)
print(binary_search([2, 4, 6, 8, 10], 5))  # Expected: -1 (not found)
# how does algorithm perform on large datasets? 
print(binary_search(list(range(1000000)), 999999))  # Expected: 999999 (found)
# how does algorithm perform in real system? for example, in youtube, facebook, etc. /suggest prompts to make it more practical.
# Make it more practical for real-world applications like searching in large databases or user lists
# Let's say we want to search for a user ID in a sorted list of user IDs
user_ids = list(range(1, 1000001))  # Simulating a sorted
target_user_id = 543210
result_index = binary_search(user_ids, target_user_id)
print(f"User ID {target_user_id} found at index: {result_index}")  # Expected: 543209 (found)
# Let's say you watched a food video on youtube and you want to search for a recipe in a sorted list of recipes
recipes = ["Apple Pie", "Banana Bread", "Chocolate Cake", "Doughnuts", "Eclairs"]
target_recipe = "Chocolate Cake"
recipe_index = binary_search(recipes, target_recipe)
print(f"Recipe '{target_recipe}' found at index: {recipe_index}")  # Expected: 2 (found)


# Exercise 7-2: Recommendation Algorithm
# Task:Create a very simple test recommendation algorithm in Python. 
# Requirements:
# - User watch history is a list of tags.
# - Video data is a dictionary: {id: [tags]}.
# - Compute a recommendation score based on how many tags match the user's history.
# - Sort videos by score and return a recommended list.
# The code must be runnable.
# the output must be printed.
# Make it handle factors like video popularity, user ratings, and viewing time and the output must be printed.
# Not ID, each object in the individual video data must be printed as a list of video IDs sorted by recommendation score.
def recommend_videos(user_history, video_data, popularity_data, rating_data, viewing_time_data):
    recommendations = []
    for video_id, tags in video_data.items():
        score = sum(1 for tag in tags if tag in user_history)
        score += popularity_data.get(video_id, 0) * 0.1  # Popularity weight
        score += rating_data.get(video_id, 0) * 0.2      # Rating weight
        score += viewing_time_data.get(video_id, 0) * 0.05  # Viewing time weight
        recommendations.append((video_id, score))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [video_id for video_id, score in recommendations]

# Example usage more praactical
user_history = ["K-pop"]
video_data = {
    1: ["K-pop", "Music"],
    2: ["Cooking", "Food"],
    3: ["Travel", "Vlog"],
    4: ["K-pop", "Dance"]
    }

popularity_data = {
    1: 1000,
    2: 500,
    3: 300,
    4: 800
    }
rating_data = {
    1: 4.5,
    2: 4.0,
    3: 3.5,
    4: 4.8
    }
viewing_time_data = {
    1: 200,
    2: 150,
    3: 100,
    4: 250
    }
recommended_videos = recommend_videos(user_history, video_data, popularity_data, rating_data, viewing_time_data)
print("Recommended video IDs sorted by recommendation score:", recommended_videos)

## Exercise 8: Test Generation

### Task: Use Copilot to generate unit tests for a simple function.

### Instructions
# 1. First, implement a function to test
# 2. Write a comment about what tests are needed
# 3. Let Copilot generate test cases
# Must pass all the test caeses
# Must the output of the test cases must be printed

### Starting Code
# Fibonacci function implementation
# Must pass all the test caeses
# Must the output of the test cases must be printed
def fibonacci(n):
    if n < 0:
        return 0  # Edge case: negative input
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Generate comprehensive unit tests for the fibonacci function
# Include edge cases: negative numbers, zero, one, and larger numbers
# Test both correctness and performance considerations
import unittest

class TestFibonacci(unittest.TestCase):
    # Let Copilot generate test methods
    # add compheresive explanation for each test case
    def test_fibonacci_negative(self):
        print("Test negative input: fibonacci(-5) =", fibonacci(-5))
        self.assertEqual(fibonacci(-5), 0)  # Edge case: negative input should return 0
    def test_fibonacci_zero(self):
        print("Test zero input: fibonacci(0) =", fibonacci(0))
        self.assertEqual(fibonacci(0), 0)  # Edge case: fibonacci(0) should return 0
    def test_fibonacci_one(self):
        print("Test one input: fibonacci(1) =", fibonacci(1))
        self.assertEqual(fibonacci(1), 1)  # Edge case: fibonacci(1) should return 1
    def test_fibonacci_small(self):
        print("Test small input: fibonacci(5) =", fibonacci(5))
        self.assertEqual(fibonacci(5), 5)  # Test case: fibonacci(5) should return 5
    def test_fibonacci_medium(self):
        print("Test medium input: fibonacci(10) =", fibonacci(10))
        self.assertEqual(fibonacci(10), 55)  # Test case: fibonacci(10) should return 55
    def test_fibonacci_large(self):
        print("Test large input: fibonacci(20) =", fibonacci(20))
        self.assertEqual(fibonacci(20), 6765)  # Test case: fibonacci(20) should return 6765
    def test_fibonacci_performance(self):
        import time
        start_time = time.time()
        result = fibonacci(30)  # Performance test for larger input
        end_time = time.time()
        print(f"Test performance: fibonacci(30) = {result}, time = {end_time - start_time:.4f} seconds")
        self.assertTrue(end_time - start_time < 1)  # Should complete within 1 second


## Run the tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
