import time

# print(time)

# print(time.time())   # отсчёт времени(sec.milisec) с первого января 1970 года
# start_time = time.time()
# print(time.ctime(2345234523))
# time.sleep(2.5)  # время в секундах для остановки программы
# end_time = time.time()
# print(time.time())

# print('end_time - start_time ', end_time - start_time)


def total_duration():
    start_time = time.time()

    # my_range = range(10000)
    # print(my_range[1000])
    my_range = list(range(100000000))
    print(my_range[1000])

    end_time = time.time()
    print('Total duration of the operation: ', end_time - start_time)

total_duration()