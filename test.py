def isHappy( n: int) -> bool:
    record_set = set()
    sum = n
    while 1 not in record_set:

        for i in str(sum):
            sum_temp = 0
            sum_temp += int(i) ** 2
        if sum_temp in record_set:
            return False
        sum = sum_temp
        record_set.add(sum)
    return True


n=2
print(isHappy(n))