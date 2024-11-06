def exponent(x, eps):
    s_i = 1
    term = 1
    i = 1
    
    while True:
        term *= x / i
        s_next = s_i + term
        if abs(s_next - s_i) <= eps:
            return s_next        
        s_i = s_next
        i += 1

x = float(input())
eps = float(input())
result = exponent(x, eps)
print(result)
