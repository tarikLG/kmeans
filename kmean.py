import random
import imageio
import numpy

def euclid_dist(a, b):
    distance = ((a[0] - b[0])**2) + ((a[1] - b[1])**2) + ((a[2] - b[2])**2)

    return distance

def calc_clusterCent(x, k):
    calculated = []
    center = [0, 0, 0]
    for c in x:
        for p in c:
            center[0] += p[0]
            center[1] += p[1]
            center[2] += p[2]
        for n in center:
            center[center.index(n)] = n/len(c)
        calculated.append(center)
        
    return calculated


def kmeans(k, s):
    check = True
    clusterCen = []
    clusters = [[],[],[],[],[]]
    for j in range(1, k+1):
        clusterCen.append(random.choice(s))
    while check:
        for x in s:
            temp = []
            for c in clusterCen:
                dis = euclid_dist(x, c)
                temp.append(dis)
            clusters[temp.index(min(temp))].append(x)
        if calc_clusterCent(clusters, k) == clusterCen:
            clusterCen = calc_clusterCent(clusters, k)
            check = False
        else:
            clusterCen = calc_clusterCent(clusters, k)

    return clusterCen

im = imageio.v2.imread('testimg.jpg')

im = im.reshape(im.shape[0]*im.shape[1],im.shape[2])

print(im.shape)

print(kmeans(5, im.tolist()))
