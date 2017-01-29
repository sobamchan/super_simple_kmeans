def super_simple_kmeans(D, k, m):
    c = [[] for i in range(k)]
    for d in D:
        c_max_v = 0
        c_max_i = None
        for i in range(len(m)):
            if c_max_v < abs(d-m[i]):
                c_max_v = abs(d-m[i])
                c_max_i = i
        c[c_max_i].append(d)
    for i in range(len(m)):
        m[i] = sum(c[i]) / len(c[i])

    return c

if __name__ == '__main__':
    D = [0, 1, 3, 5.5, 6, 2]
    k = 2
    m = [-1, 6]
    super_simple_kmeans(D, k, m)
