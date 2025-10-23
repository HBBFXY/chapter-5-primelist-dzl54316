def PrimeList(N):
    # 处理所有小于2的情况，直接返回空字符串
    if N <= 2:
        return ""
    
    # 初始化筛子：确保0和1被标记为非质数
    sieve = [True] * N
    sieve[0], sieve[1] = False, False
    
    # 埃拉托斯特尼筛法：循环到int(N**0.5)的整数部分
    max_factor = int(N ** 0.5)
    for i in range(2, max_factor + 1):
        if sieve[i]:
            # 更高效的标记方式：使用切片但不创建临时列表
            # 从i*i开始标记（i*2到i*(i-1)已经被更小的质数标记过了）
            start = i * i
            sieve[start : N : i] = [False] * ((N - 1 - start) // i + 1)
    
    # 提取质数（仅保留≥2的数）
    primes = []
    for num in range(2, N):
        if sieve[num]:
            primes.append(str(num))
    
    # 拼接为字符串：若为空则返回空字符串，否则无末尾空格
    return " ".join(primes) if primes else ""
