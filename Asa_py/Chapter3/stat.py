import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]

sorted(values)

statistics.mean(values)

statistics.median(values)

statistics.mode(values)


print(f'This is the mean {statistics.mean(values)}, the median {statistics.median(values)}, and the mode of the numbers {statistics.mode(values)}')