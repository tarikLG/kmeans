from PIL import Image
import numpy as np

class KMean:
    def __init__(self, k, s):
        self.k = k
        self.s = s


    def clustering(self):
        check = True
        clusterCen = np.array(self.s[np.random.randint(self.s.shape[0], size=self.k)])

        while check: 
            clusters = []

            for i in range(self.k):
                clusters.append([])

            for point in self.s.tolist():
                point = np.array(point)
                temp = np.sum(np.square(clusterCen - point), axis=1)
                
                clusters[temp.tolist().index(min(temp))].append(point.tolist())

            calculated = np.zeros_like(clusterCen)

            for c in clusters:
                center = np.zeros(self.s.shape[1])
                for p in c:
                    center += p
                center = np.divide(center, len(c))
                calculated[clusters.index(c)] = center
            
            if clusterCen.tolist() == calculated.tolist():
                clusterCen = calculated
                check = False
            else:
                clusterCen = calculated

        return (clusterCen, clusters)
        
im = Image.open("testimg.jpg")
im = np.array(im)

im = im.reshape(im.shape[0]*im.shape[1],im.shape[2])

# first element is the cluster centers and the second element is the clusters themselves

kmean = KMean(5, im)
final_clusters = kmean.clustering()

print(final_clusters[0])