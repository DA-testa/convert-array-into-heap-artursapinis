import math

def build_heap(data):
    swaps = []
    n = len(data)
    for i in reversed(range(math.ceil(n / 2))):
        i_max = i
        val = 2 * i + 1
        if val < n and data[val] < data[i_max]:
            i_max = val
        r = 2 * i + 2
        if r < n and data[r] < data[i_max]:
            i_max = r
        if i != i_max:
            swaps.append((i, i_max))
            data[i], data[i_max] = data[i_max], data[i]
            swaps.extend(build_heap(data[i_max:]))
    return swaps

def main():
    # inp = input()[0]
    n = int(input())
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
