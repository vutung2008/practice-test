def is_prime(a):
   if a < 2:
      return False
   for i in range(2, int(a**0.5) +1):
      if a % i == 0:
          return False
   return True

def prime_sum_up_to_n(n):
    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum
N = 10
result = prime_sum_up_to_n(N)
print ("tổng của tất cả các số nguyên tố từ 2 đến", N, "là:", result)
        