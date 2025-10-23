def PrimeList(N):
    if N <= 2:
        return ""  # 小于2的数无质数
    # 初始化筛子：index表示数字，值为True表示是质数
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 0和1不是质数
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : N : i] = [False] * len(sieve[i*i : N : i])
    # 提取所有质数并转为空格分隔的字符串
    primes = [str(num) for num, is_prime in enumerate(sieve) if is_prime]
    return " ".join(primes)
