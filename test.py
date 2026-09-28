# GuardRail Security Test

# Test 1: Secret detection
API_KEY = "sk-live-9876543210987654321"

# Test 2: Dangerous eval detection
user_input = input("Enter value: ")
result = eval(user_input)

print(result)