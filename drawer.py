
import matplotlib.pyplot as plt

def draw_graph_clustering(array_of_clusters, points_in_clusters, title):
    """Takes a double array of points and displays them on the graph array[0]->xs array[1]->ys"""
    array_of_color = ['#FF0000', '#00FF00', '#00FFFF', '#7FAFD4', '#8A2BE2',
                      '#A52A2A', '#DC143C', '#A9A9A9', '#006400', '#8B008B',
                      '#FF8C00', '#228B22', '#DCDCDC', '#ADFF2F', '#7CFC00',
                      '#FFFACD', '#F08080', '#B0C4DE', '#FFA07A', '#20B2AA']

    plt.title(title)
    index_clr = 0
    for point in points_in_clusters:
        plt.plot(point[0], point[1], 'o', color=array_of_color[index_clr], markersize=3)
        index_clr += 1
    plt.plot(array_of_clusters[0], array_of_clusters[1], 's', color='blue', markersize=10)
    plt.xticks(())
    plt.yticks(())
    plt.show()
