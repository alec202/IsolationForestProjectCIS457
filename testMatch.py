from matching import matching

result = matching("122.130.01.20")
result2 = matching("13.133.1.20")
result3 = matching("123.456.01.20")

#Test1
if result is not False:
    print(f"IP address was found at index {result}")
else:
    print("IP address not found")

#Test 2
if result2 is not False:
    print(f"IP address was found at index {result}")
else:
    print("IP address not found")  

#Test 3 
if result3 is not False:
    print(f"IP address was found at index {result}")
else:
    print("IP address not found")  
