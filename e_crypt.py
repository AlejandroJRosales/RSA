import random


# Method for finding greatest common denominator of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Method for finding least common multiple of two numbers
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while True:
       if z % x == 0 and z % y == 0:
           answer = z
           break
       z += 1

   return answer


# Inverse Mod
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Method for finding coprime of number
def coprime(x):
    prime = 0
    for i in range(2, x):
        if gcd(a, i) == 1:
            prime = i
    return prime


# Generate Prime numbers and randomly select two different prime numbers
primes = []
for i in range(2, 100):
    k = 0
    for a in range(2, i//2+1):
        if i % a == 0:
            k += 1
    if k <= 0:
        primes.append(i)


# Generating Public Key
p, q = primes.pop(random.randint(0, len(primes) - 1)), primes.pop(random.randint(0, len(primes) - 1))
print(f"Select two prime no's. Suppose P = {p} and Q = {q}")
n = p * q
print(f"Now first part of the Public key: n = P*Q = {n}.")
print("""We also need a small exponent say e:
e Must be:
    An integer.
    Not be a factor of n.
    1 < e < totient

    Our Public Key is made of n and e""")


# Generating Private Key
totient = lcm((p - 1), (q - 1))
print(f"""We need to calculate Carmichael's totient function:
    Such that totient = lcm(P-1, Q-1) or lcm({p}-1, {q}-1) = {totient}""")
print(f"Carmichael's totient function: {totient}")

e = coprime(totient)

d = 0
for d in range(2, totient):
    if e * d == 1 % totient:
        break
print(f"""Now calculate Private Key, d:
de = 1%totient
{d}*{e} = 1%{totient} """)

print(f"Now we are ready!")

msg = input("\nMsg: ")

# Encrypt msg
encrypt = lambda x: x**e % n
e_crypt = "".join([chr(encrypt(ord(c))) for c in msg])
print(f"Encrypted - {e_crypt}")

# Decrypt msg
decrypt = lambda x: x**d % n
d_crypt = "".join([chr(decrypt(ord(c))) for c in e_crypt])
print(f"Decrypted - {d_crypt}")

# Print Private and Public keys
print(f"Public key = (n, e) = ({n}, {e}) Private key = (n, d) = ({n}, {d}) totient = {totient}")
