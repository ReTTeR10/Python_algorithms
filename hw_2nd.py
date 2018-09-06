__author__ = 'Мишин Егор Олегович'

'''
нахождение n-ого простого числа c помощью алгоритма решето Эратосфена
'''
import cProfile


def simple_er(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b


'''Время через timeit'''

# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_er(40)"
#               100 loops, best of 5: 23.8 usec per loop

# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_er(400)"
#               100 loops, best of 5: 157 usec per loop

# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_er(4000)"
#               100 loops, best of 5: 1.9 msec per loop

# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_er(40000)"
#               100 loops, best of 5: 20.1 msec per loop


# cProfile.run('simple_er(40000)')


#       4207 function calls in 0.032 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.032    0.032 <string>:1(<module>)
#      1    0.031    0.031    0.031    0.031 hw_2nd.py:8(simple_er)
#      1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#   4203    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('simple_er(4000)')


#            554 function calls in 0.003 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 hw_2nd.py:8(simple_er)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       550    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''
нахождение n-ого простого числа
'''


def simple_2(n):
    lst = [2]

    for i in range(3, int(n), 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


'''
Время через timeit
'''

# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_2(40)"
#           100 loops, best of 5: 16.5 usec per loop
# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_2(400)"
#           100 loops, best of 5: 128 usec per loop
# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_2(4000)"
#           100 loops, best of 5: 1.86 msec per loop
# python -m timeit -n 100 -s "import hw_2nd" "hw_2nd.simple_2(40000)"
#           100 loops, best of 5: 34.1 msec per loop


# cProfile.run('simple_2(40000)')
#           4206 function calls in 0.033 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.033    0.033 <string>:1(<module>)
#         1    0.033    0.033    0.033    0.033 hw_2nd.py:78(simple_2)
#         1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
#      4202    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('simple_2(4000)')

#          553 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 hw_2nd.py:78(simple_2)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#       549    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
