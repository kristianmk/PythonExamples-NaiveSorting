# Very naive and inefficient sorting with profiling.
# Written by K. M. Knausgård 2021
from timeit import default_timer as timer


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


# This way of profiling will give an indication of performance, but no statistics. Run timeit with a large number of
# executions for more accurate and representative results. See timit module documentation:
# https://docs.python.org/3/library/timeit.html
def main():
    some_values = [3, 314, 21, 95, 29, 88, 0, 1000, 1, 26, 8, 19]
    print(some_values)
    start = timer()
    naive_sort(some_values)  # Compare runtime of this...
    #some_values.sort()  # ... to runtime of this!
    end = timer()
    print(some_values)

    print(f"Elapsed time: {(end - start) * 10 ** 6}")


if __name__ == '__main__':
    main()

