
import math
import sys

import numpy as npr

import drawer
import helper

def calc_eucl_dist(point_one_x, point_one_y, point_two_x, point_two_y):
    """Returns the distance between two points on a plane"""
    return math.sqrt((point_two_x-point_one_x)**2 + (point_two_y-point_one_y)**2)

def search_points_in_cluster():
    """Looking to which cluster the point belongs and writes to the array"""
    array = []
    for index in range(len(MRX_OF_COORD_POINTS[0])):
        point_one = [MRX_OF_COORD_POINTS[0][index], MRX_OF_COORD_POINTS[1][index]]
        prev_distance = 1000
        for index_p in range(len(MRX_OF_COORD_CLUSTERS[0])):
            point_two = [MRX_OF_COORD_CLUSTERS[0][index_p], MRX_OF_COORD_CLUSTERS[1][index_p]]
            curr_distance = calc_eucl_dist(point_one[0], point_one[1], point_two[0], point_two[1])
            if curr_distance < prev_distance:
                prev_distance = curr_distance
                index_of_cluster = index_p
        array.append(index_of_cluster)
    return array

def remember_points_in_cluster():
    """Records in sheet which point belongs to which cluster"""
    for index in range(len(MRX_OF_COORD_POINTS[0])):
        POINTS_IN_CLUSTERS[ARR_OF_INDEX[index]][0].append(MRX_OF_COORD_POINTS[0][index])
        POINTS_IN_CLUSTERS[ARR_OF_INDEX[index]][1].append(MRX_OF_COORD_POINTS[1][index])

def create_empty_list_of_points():
    """Prepares a list filling"""
    empty_list = []
    for index in range(len(MRX_OF_COORD_CLUSTERS[0])):
        empty_list.append([[], []])
    return empty_list

def calculation_center_mass():
    """Finds the center of mass of points and writes in an array"""
    count = 0
    for point in POINTS_IN_CLUSTERS:
        c_x = round(sum(point[0]) / len(point[0]), 2)
        c_y = round(sum(point[1]) / len(point[1]), 2)
        MRX_OF_COORD_CLUSTERS[0][count] = c_x
        MRX_OF_COORD_CLUSTERS[1][count] = c_y
        count += 1

if __name__ == "__main__":
    COUNT_OF_POINTS, COUNT_OF_CLUSTERS = helper.read_data_command_line(sys.argv[1:])
    MRX_OF_COORD_CLUSTERS = npr.random.random_sample((2, COUNT_OF_CLUSTERS))
    MRX_OF_COORD_POINTS = npr.random.random_sample((2, COUNT_OF_POINTS))

    POINTS_IN_CLUSTERS = create_empty_list_of_points()
    ARR_OF_INDEX = search_points_in_cluster()
    remember_points_in_cluster()
    TITLE = 'Start of algorithm k-means'

    i = 0
    IS_DONE = False
    while not IS_DONE:
        PREV_MRX = npr.copy(MRX_OF_COORD_CLUSTERS)
        calculation_center_mass()
        POINTS_IN_CLUSTERS = create_empty_list_of_points()
        ARR_OF_INDEX = search_points_in_cluster()
        remember_points_in_cluster()
        i += 1
        if npr.array_equiv(PREV_MRX, MRX_OF_COORD_CLUSTERS):
            IS_DONE = True

    print('Iterations: ', i)
    TITLE = 'Result of algorithm k-means'
    print(POINTS_IN_CLUSTERS)
    drawer.draw_graph_clustering(MRX_OF_COORD_CLUSTERS, POINTS_IN_CLUSTERS, TITLE)
