# Very naive and inefficient sorting.
# Written by K. M. Knausgård 2021


def naive_sort(some_values):
    for i, v in enumerate(some_values):
        ki = i
        kv = v
        for j in range(i+1, len(some_values)):
            if some_values[j] < kv:
                kv = some_values[j]
                ki = j
        some_values[i] = kv
        some_values[ki] = v
    return


def main():
    some_values = [3, 314, 21, 95, 29, 88, 0, 1000, 1, 26, 8, 19]
    print(some_values)
    naive_sort(some_values)
    print(some_values)


if __name__ == '__main__':
    main()

