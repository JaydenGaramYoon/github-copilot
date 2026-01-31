// Exercise 3: String Manipulation

// Task: Create a function that validates and formats phone numbers.

/// Instructions
// 1. Write descriptive comments about the expected behavior
// 2. Use Copilot to implement the logic
// 3. Handle various input formats

// Starting Code

// # [Detailed function description]
// # Parameters: [parameter descriptions with types]
// # Returns: [return value description]
// # Raises: [exception descriptions]
// # Example: [usage example]

function formatPhoneNumber(phoneNumber){
// Function to validate and format phone numbers
// Parameter: phoneNumber (string): The input phone number
// Returns: string: Formatted phone number in the format (XXX) XXX-XXXX
// Console log: Return null and console log error if input is not a string or if the number is less than 10 digits
// Add log to handle null, undefined, or non-string inputs    
    if (typeof phoneNumber !== 'string') {
        console.error("Invalid input: Input must be a string.");
        return null;
    }
    // Remove all non-digit characters
    const digits = phoneNumber.replace(/\D/g, '');
    // Check if the number has exactly 10 digits
    if (digits.length !== 10) {
        console.error("Invalid phone number: Must contain exactly 10 digits.");
        return null;
    }
    // Format the number as (XXX) XXX-XXXX
    const formattedNumber = `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
    return formattedNumber;
}

// Edge Test Cases
console.log(formatPhoneNumber("987 654 3210"));      // "(987) 654-3210"
console.log(formatPhoneNumber("987.654.3210"));      // "(987) 654-3210"
console.log(formatPhoneNumber("9876543210abc"));     // "(987) 654-3210"
console.log(formatPhoneNumber(""));                  // null
console.log(formatPhoneNumber(null));                // null
console.log(formatPhoneNumber(undefined));           // null
console.log(formatPhoneNumber(1234567890));          // null