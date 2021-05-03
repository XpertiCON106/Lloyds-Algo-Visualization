import random
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Create data
    N = 10
    #x = np.random.rand(N)
    #y = np.random.rand(N)
    colors = (0,0,0)
    area = np.pi*3

    with open("input") as file:
        content = file.readlines()

    k = content[0].split()[0]
    n = content[0].split()[1]
    pointLists = content[1:]

    clusters = []
    for i in range(int(k)):
        clusters.append([])

    # picking K RANDOM initial points
    centers = []
    for i in range(int(k)):
        centers.append(pointLists[i])

    resultCenter = []
    while True:
        previousCenters = centers
        for p in pointLists:
            closeClusterIndex = 0
            dist = 0
            checkedFirst = False
            for c in range(len(centers)):
                if checkedFirst == False:
                    dist = ecludian(p.rstrip().split(" "), centers[c].rstrip().split(" "), n)
                    closeClusterIndex = 0
                    checkedFirst = True
                else:
                    if (ecludian(p.rstrip().split(" "), centers[c].rstrip().split(" "), n) <= dist):
                        dist = ecludian(p.rstrip().split(" "), centers[c].rstrip().split(" "), n)
                        closeClusterIndex = c
            clusters[closeClusterIndex].append(p)

        tempCenters = []
        for i in range(len(centers)):
            tempCenters.append("0")

        for i in range(len(clusters)):
            newCenter = center(clusters[i],n)
            tempCenters[i] = newCenter.rstrip()

        if tempCenters == centers:
            resultCenter = centers
            break
        else:
            centers = tempCenters
            clusters = []
            for i in range(int(k)):
                clusters.append([])

    f = open("output","w")
    result = ""

    print("Clusters: " + str(clusters))
    clabel = []
    '''
    # make sure to add more colors if you want more clusters
    colorList = ["red","green","yellow","blue"]
    colors = {}
    for i in range(int(k)):
        colors["Cluster" + str(i)] = (colorList[i])

    print(colors)
    '''
    for i in range(int(k)):
        clabel.append("Cluster " +str(i))

    print(clabel)

        # Generate Data
    num = 20
    x, y = np.random.random((2, num))
    labels = np.random.choice(['a', 'b', 'c'], num)
    df = pd.DataFrame(dict(x=x, y=y, label=labels))

    groups = df.groupby('label')

    # Plot
    fig, ax = plt.subplots()
    ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, label=name)
    ax.legend()

    plt.show()
    '''
    x_array = []
    y_array = []
    for p in content:
        p = p.rstrip()
        x_array.append(float(p.split(" ")[0]))
        y_array.append(float(p.split(" ")[1]))

    x_array = np.array(x_array)
    y_array = np.array(y_array)
    print(x_array)
    print(y_array)

    # Plot
    plt.scatter(x_array, y_array, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    '''
    for i in range(len(resultCenter)):
        if i == len(resultCenter)-1:
            result += str(resultCenter[i])
            break
        result+= str(resultCenter[i]) +"\n"
    f.write(result)
    f.close()

def center(dataPoints, n):
    cen = ""
    for i in range(int(n)):
        sum = 0.0
        div = 0
        for d in dataPoints:
            d.rstrip()
            sum += float(d.split(" ")[i])
            div+=1
        cen += str(round(sum/div,2)) + " "
    return cen

def ecludian(A, B, n):
    result = 0
    for i in range(int(n)):
        result += (float(A[i]) - float(B[i])) * (float(A[i]) - float(B[i]))
    return round(math.sqrt(result),2)

if __name__ == '__main__':
    main()
