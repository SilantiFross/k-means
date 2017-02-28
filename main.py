import math
import sys

import numpy as np

import drawer
import helper

def euclidean_distance(first_point, second_point):
    return math.sqrt((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2)

def calculation_center_mass(points_in_clusters, clusters):
    for points_in_cluster in points_in_clusters:
        sum_x = 0
        sum_y = 0
        for point in points_in_cluster:
            sum_x += point[0]
            sum_y += point[1]
        center_x = sum_x / len(points_in_cluster)
        center_y = sum_y / len(points_in_cluster)
        clusters[points_in_clusters.index(points_in_cluster)][0] = round(center_x, 2)
        clusters[points_in_clusters.index(points_in_cluster)][1] = round(center_y, 2)

def create_list_of_points(matrix_of_coord):
    list_of_points = []
    for index in range(len(matrix_of_coord[0])):
        point = [matrix_of_coord[0][index], matrix_of_coord[1][index]]
        list_of_points.append(point)
    return list_of_points

def create_empty_list(dimension):
    array = []
    for i in range(len(dimension)):
        array.append([])
    return array

def search_center_for_points(centers, points):
    array = create_empty_list(centers)
    for point in points:
        prev_distance = 1000
        for center in centers:
            curr_distance = euclidean_distance(center, point)
            if curr_distance < prev_distance:
                prev_distance = curr_distance
                index_of_cluster = centers.index(center)
        array[index_of_cluster].append(point)
    return array

def create_empty_list_x_y(number_of_centers):
    array = []
    for i in range(number_of_centers):
        array.append([[], []])
    return array

def create_points_x_y(points_in_clusters, number_of_clusters):
    array = create_empty_list_x_y(number_of_clusters)
    for points in points_in_clusters:
        for point in points:
            array[points_in_clusters.index(points)][0].append(point[0])
            array[points_in_clusters.index(points)][1].append(point[1])
    return array

if __name__ == "__main__":
    COUNT_OF_POINTS, COUNT_OF_CLUSTERS, FROM_FILE = helper.read_data_command_line(sys.argv[1:])
    if FROM_FILE:
        MRX_OF_COORD_POINTS = np.loadtxt('../coords.txt')
        MRX_OF_COORD_CLUSTERS = np.loadtxt('../centers.txt')
    else:
        MRX_OF_COORD_POINTS = np.random.random_sample((2, COUNT_OF_POINTS))
        MRX_OF_COORD_CLUSTERS = np.random.random_sample((2, COUNT_OF_CLUSTERS))

    points = create_list_of_points(MRX_OF_COORD_POINTS)
    clusters = create_list_of_points(MRX_OF_COORD_CLUSTERS)

    points_in_clusters = search_center_for_points(clusters, points)
    if not FROM_FILE:
        point_in_clusters_x_y = create_points_x_y(points_in_clusters, len(clusters))
        TITLE = 'Start of algorithm k-means'
        drawer.draw_graph_clustering(clusters, point_in_clusters_x_y, TITLE)

    is_done = False
    while not is_done:
        previous_clusters = np.copy(clusters)
        calculation_center_mass(points_in_clusters, clusters)
        points_in_clusters = search_center_for_points(clusters, points)
        if np.array_equiv(previous_clusters, clusters):
            is_done = True

    TITLE = 'Result of algorithm k-means'
    point_in_clusters_x_y = create_points_x_y(points_in_clusters, len(clusters))
    drawer.draw_graph_clustering(clusters, point_in_clusters_x_y, TITLE)
