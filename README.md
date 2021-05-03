# Lloyds-Algo-Visualization
This is a visualization of the Lloyds algorithm. The basic description of the algorithm is described below.



The Lloyd algorithm is one of the most popular clustering heuristics for the k-Means Clustering Problem. It first chooses k arbitrary points Centers from Data as centers and then iteratively performs the following two steps:

Centers to Clusters: After centers have been selected, assign each data point to the cluster corresponding to its nearest center; ties are broken arbitrarily.
Clusters to Centers: After data points have been assigned to clusters, assign each cluster’s center of gravity to be the cluster’s new center.
We say that the Lloyd algorithm has converged if the centers (and therefore their clusters) stop changing between iterations.

Implement the Lloyd algorithm
Given: Integers k and m followed by a set of points Data in m-dimensional space.

Return: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.
