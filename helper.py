
import sys
import getopt

def read_data_command_line(argv):
    """Reads and returns the data needed to implement the K-means algorithm"""
    count_of_points = 1000
    count_of_clusters = 2
    try:
        opts, args = getopt.getopt(argv, "hp:c:f")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    from_file = False
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -p <count_of_points> -c <count_of_clasters> OR main.py -f')
            sys.exit()
        elif opt == '-p':
            count_of_points = arg
        elif opt == '-c':
            count_of_clusters = arg
        elif opt == '-f':
            from_file = True
    return int(count_of_points), int(count_of_clusters), from_file

def conversation_to_matrix(points):
    matrix = [[], []]
    for point in points:
        matrix[0].append(point[0])
        matrix[1].append(point[1])
    return matrix
