def PrimeList(N):
    # 处理N≤2的情况：无小于N的质数
    if N <= 2:
        return ""
    
    # 初始化筛子：index对应数字，True表示是质数
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 明确排除0和1
    
    # 埃拉托斯特尼筛法：遍历到√N即可
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            # 标记i的倍数（从i²开始，避免重复标记）
            sieve[i*i : N : i] = [False] * len(sieve[i*i : N : i])
    
    # 提取所有质数（确保不包含1）
    primes = [str(num) for num, is_prime in enumerate(sieve) if is_prime and num >= 2]
    # 拼接为空格分隔的字符串（末尾无空格）
    return " ".join(primes)
