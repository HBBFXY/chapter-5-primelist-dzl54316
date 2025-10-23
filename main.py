def PrimeList(N):
    if N <= 2:
        return ""  # 小于等于2时无质数（2本身不小于2）
    # 初始化筛子：index对应数字，True表示是质数
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 0、1不是质数
    # 埃拉托斯特尼筛法
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            # 标记当前质数的所有倍数为非质数
            sieve[i*i : N : i] = [False] * len(sieve[i*i : N : i])
    # 提取质数并拼接为字符串
    primes = [str(num) for num, is_prime in enumerate(sieve) if is_prime]
    return " ".join(primes)
