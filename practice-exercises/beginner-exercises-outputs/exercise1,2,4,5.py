# Beginner Practice Exercises

## Exercise 1: Basic Function Creation

### Task: Use GitHub Copilot to create a function that calculates the area of different geometric shapes.

### Instructions
# 1. Write a comment describing the function
# 2. Let Copilot suggest the implementation
# 3. Test with different inputs


# Function to calculate area of geometric shapes
# Supports circle, rectangle, and triangle
# Parameters: shape_type (string), dimensions (list or dict)
# Returns: area as float, or None if invalid shape
import math

def calculate_area(shape_type, dimensions):
    if shape_type == "circle":
        radius = dimensions.get("radius", 0)
        return math.pi * (radius ** 2)
    elif shape_type == "rectangle":
        width = dimensions.get("width", 0)
        height = dimensions.get("height", 0)
        return width * height
    elif shape_type == "triangle":
        base = dimensions.get("base", 0)
        height = dimensions.get("height", 0)
        return 0.5 * base * height
    else:
        return None

### Test Cases
print("Exercise 1 test results:")
print(calculate_area("circle", {"radius": 5}))  # Should return ~78.54
print(calculate_area("rectangle", {"width": 4, "height": 6}))  # Should return 24
print(calculate_area("triangle", {"base": 10, "height": 8}))  # Should return 40
print(calculate_area("invalid", {}))  # Should return None or raise error


# Exercise 2: Data Processing

### Task: Create a function that processes a list of student records and returns statistics.

### Instructions
#1. Start with a clear comment about the function's purpose
#2. Use Copilot to generate the implementation
#3. Include error handling

### Starting Code
# Function to analyze student grades
# Input: list of dictionaries with 'name', 'grade', 'subject' keys
# Output: dictionary with statistics (average, highest, lowest, pass_rate)
# Pass rate is percentage of grades >= 60
# Add error handling for None and do return error for minus grades and 100 is the max grade.
# if the value is 'inf' or '-inf', can you change the value to 'Wrong'? 
# yes, I can do that. Let me add that now.
# Can you really make that change now? when the value is not correct, then the value should be 'Wrong'.
def analyze_student_grades(student_records):
    if not student_records:
        return {
            "average": 0,
            "highest": None,
            "lowest": None,
            "pass_rate": 0
        }

    total_grades = 0
    highest_grade = float('-inf')
    lowest_grade = float('inf')
    pass_count = 0
    valid_grades_count = 0

    for record in student_records:
        grade = record.get("grade")
        if grade is None or not isinstance(grade, (int, float)):
            continue
        if grade < 0 or grade > 100 or grade == float('inf') or grade == float('-inf'):
            continue
        valid_grades_count += 1
        total_grades += grade
        if grade >= 60:
            pass_count += 1
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade

    if valid_grades_count == 0:
        return {
            "average": 0,
            "highest": 'Wrong',
            "lowest": 'Wrong',
            "pass_rate": 0
        }

    average_grade = total_grades / valid_grades_count
    pass_rate = (pass_count / valid_grades_count) * 100

    # If no valid grades, set highest/lowest to 'Wrong'
    if highest_grade == float('-inf'):
        highest_grade = 'Wrong'
    if lowest_grade == float('inf'):
        lowest_grade = 'Wrong'

    return {
        "average": average_grade,
        "highest": highest_grade,
        "lowest": lowest_grade,
        "pass_rate": pass_rate
    }



### Sample Data
students = [
    {"name": "Alice", "grade": 85, "subject": "Math"},
    {"name": "Bob", "grade": 76, "subject": "Math"},
    {"name": "Charlie", "grade": 92, "subject": "Science"},
    {"name": "Diana", "grade": 58, "subject": "Math"},
    {"name": "Eve", "grade": 88, "subject": "Science"}
]

### Test Case
print("Exercise 2 test result:")
## Test function to verify analyze_student_grades
## Calculate each column and print the results
## Write the code below 
results = analyze_student_grades(students)
print(f"Average Grade: {results['average']}")
print(f"Highest Grade: {results['highest']}")
print(f"Lowest Grade: {results['lowest']}")
print(f"Pass Rate: {results['pass_rate']}%")
print(analyze_student_grades(students))

## Test boundaries and edge cases
# add expected results as comments 
print("edge1) " + str(analyze_student_grades([])))  # Edge case: empty list
# expected output: {'average': 0, 'highest': 'Wrong', 'lowest': 'Wrong', 'pass_rate': 0}
## more edge cases
print("edge2) " + str(analyze_student_grades([{"name": "Frank", "grade": 60, "subject": "Math"}])))  # Edge case: single passing student
# expected output: {'average': 60.0, 'highest': 60, 'lowest': 60, 'pass_rate': 100.0}
print("edge3) " + str(analyze_student_grades([{"name": "Grace", "grade": 59, "subject": "Math"}])))  # Edge case: single failing student
# expected output: {'average': 59.0, 'highest': 59, 'lowest': 59, 'pass_rate': 0.0}
## more edge cases
print("edge4) " + str(analyze_student_grades([{"name": "Heidi", "grade": 100, "subject": "Science"}])))  # Edge case: perfect score
# expected output: {'average': 100.0, 'highest': 100, 'lowest': 100, 'pass_rate': 100.0}
print("edge5) " + str(analyze_student_grades([{"name": "Ivan", "grade": 0, "subject": "Science"}])))  # Edge case: zero score
# expected output: {'average': 0.0, 'highest': 0, 'lowest': 0, 'pass_rate': 0.0}
## more edge cases
print("edge6) " + str(analyze_student_grades([{"name": "Judy", "grade": -10, "subject": "Math"}])))  # Edge case: negative score
# expected output: {'average': 0, 'highest': 'Wrong', 'lowest': 'Wrong', 'pass_rate': 0}
print("edge7) " + str(analyze_student_grades([{"name": "Karl", "grade": 150, "subject": "Math"}])))  # Edge case: score above 100
# expected output: {'average': 0, 'highest': 'Wrong', 'lowest': 'Wrong', 'pass_rate': 0}
## more edge cases
print("edge8) " + str(analyze_student_grades([{"name": "Liam", "grade": None, "subject": "Math"}])))  # Edge case: None grade
# expected output: {'average': 0, 'highest': 'Wrong', 'lowest': 'Wrong', 'pass_rate': 0}
print("edge9) " + str(analyze_student_grades([{"name": "Mia", "subject": "Math"}])))  # Edge case: missing grade key
# expected output: {'average': 0, 'highest': 'Wrong', 'lowest': 'Wrong', 'pass_rate': 0}


## Exercise 4: API Response Handler

### Task: Create a function that processes API responses and handles errors gracefully.

### Instructions
# 1. Comment about the expected API response structure
# 2. Let Copilot generate error handling logic
# 3. Include data transformation

### Starting Code


# [API description and purpose]
# Endpoint: https://pokeapi.co/api/v2/pokemon/1
# Request: Get textCOntent field from the API response
# Write code to get the response now, or can't you write the code? answer is yes, then wrtie the code
# Method: GET 
# just write a function to print json repsponse data from the endpoint

     
import requests
def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    #write code below to get real name and type from the response_json below now.

    if response.status_code == 200:
        data = response.json()
        name = data.get("name", "Unknown")
        types = [t['type']['name'] for t in data.get("types", [])]
        return {
            "name": name,
            "types": types
        }
    else:
        return {
            "error": f"Failed to fetch data: {response.status_code}"
        }
### Test Case
print("Exercise 4 test result:")
print(fetch_pokemon_data(1))  # Valid Pokemon ID

## generate an url to get bulbasaur data from pokeapi.
## give me a full url to get bulbasaur data from pokeapi.
# not full data, only the name and types.
# Answer: https://pokeapi.co/api/v2/pokemon/1, this is not for name and types only, but full data
# how do i get the name and type from the url?

# Exercsie 4-2: API Response Processor
# Function to process API response from user service
# Expected response: {"status": "success", "data": {...}, "message": "..."}
# For errors: {"status": "error", "error_code": 400, "message": "..."}
# Returns: user data dict if successful, None if error
# Should log errors appropriately
def process_user_api_response(response_json): ## what arguments can be passed to this function? tell me now.
    # response_json: dict: The JSON response from the API
    # then any kind of dictionary can be passed to this function?
    # yes, any kind of dictionary can be passed to this function.
    # Let Copilot implement this
    
### Sample Responses
    if response_json.get("status") == "success":
        return response_json.get("data", {})
    elif response_json.get("status") == "error":
        error_code = response_json.get("error_code", "Unknown")
        message = response_json.get("message", "No message provided")
        print(f"Error {error_code}: {message}")
        return None
    elif response_json.get("status") == "server error":
        error_code = response_json.get("error_code", "Unknown")
        message = response_json.get("message", "No message provided")
        print(f"Server error {error_code}: {message}")
        return None
    else:
        print("Invalid response format")
        return None
    
# Success response
success_response = {
    "status": "success",
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "message": "User retrieved successfully"
}

# Error response
error_response = {
    "status": "error",
    "error_code": 404,
    "message": "User not found"
}

# write urgent response 
# not success or error response, so not handled specifically.
# but we can log it as urgent.
# how? do you mean in the function?
# yes, let me add that now.
urgent_response = {
    "status": "server error",
    "error_code": 500,
    "message": "Server error"
}

# Test Cases
print("Exercise 4-2 test results:")
print(process_user_api_response(success_response))  # Should return user data
print(process_user_api_response(error_response))    # Should log error and return None
print(process_user_api_response(urgent_response))   # Should log urgent error and return None


## Exercise 5: File Operations

### Task: Create a utility function for reading and parsing configuration files.

### Instructions
# 1. Write comments about supported file formats
# 2. Use Copilot to handle different file types
# 3. Include error handling for file operations

import os
import json
def read_config_file(file_path):
# [Detailed function description]
# Parameters: file_path (str): The path to the configuration file
# Supports: JSON, YAML, INI, txt formats
# Returns: dict: A dictionary containing the configuration data
# Raises: FileNotFoundError, PermissionError, ValueError
# Example: config = read_config_file("config.yaml")
# Let Copilot complete this implementation
# exepcted error: add exeption handling for file not found, permission denied, and invalid format
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Permission denied: {file_path}")

    _, file_extension = os.path.splitext(file_path)
    try:
        with open(file_path, 'r') as file:
            if file_extension == '.json':
                return json.load(file)
            elif file_extension in ['.yaml', '.yml']:
                import yaml
                return yaml.safe_load(file)
            elif file_extension == '.ini':
                import configparser
                config = configparser.ConfigParser()
                config.read_file(file)
                return {section: dict(config.items(section)) for section in config.sections()}
            elif file_extension == '.txt':
                return {"content": file.read()}
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")
    
### Test Cases
### Add edge case tests for non-existent file, permission denied, and invalid format

print("Exercise 5 test results:")
print(read_config_file("exercise5.txt"))  
# Assuming exercise5.txt exists with some content
# Add more test cases as needed
# Test non-existent file
try:
    read_config_file("non_existent_file.cfg")
except FileNotFoundError as e:
    print(e)
# Test permission denied (this may require setting file permissions manually)
# Test invalid format
try:
    read_config_file("invalid_format.xyz")
except ValueError as e:
    print(e)