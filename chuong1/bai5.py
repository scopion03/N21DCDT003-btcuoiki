def classify_number(n):
    s = sum([i for i in range(1, n) if n % i == 0])
    
    if s < n:
        return 'deficient'
    elif s == n:
        return 'perfect'
    else:
        return 'abundant'

def classify_numbers_in_range(x, y):
   
    classification = {}
    
    for number in range(x, y + 1):
        classification[number] = classify_number(number)
    
    return classification

x = 1
y = 20
classifications = classify_numbers_in_range(x, y)
for number, classification in classifications.items():
    print(f"Number {number} is {classification}.")
