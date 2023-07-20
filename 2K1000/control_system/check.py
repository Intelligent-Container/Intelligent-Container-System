def calculate_checksum(data):
    checksum = 0
    length = len(data)
    for i in range(length):
        checksum += ord(data[i])
        checksum = ((checksum << 3) | (checksum >> 29)) & 0xFFFFFFFF  # 进行循环左移操作，并确保结果为32位无符号整数

    return checksum


# if __name__ == '__main__':
#     str = "start:00:01:1B:FF:FF:FF:100:2023:7:9:15:30:30:26.5:79:0:93362.74:112.34&16.84:1234567812345678:end"
#     sum = calculate_checksum(str)
#     print(sum)