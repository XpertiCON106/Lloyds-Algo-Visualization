import random
import math

def main():
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
