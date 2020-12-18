import sys, getopt
import networkx as nx
import lpanni
import generator


def main(argv):
    opts = []
    try:
        opts, args = getopt.getopt(argv, 'i:o:')
    except:
        print('main.py -i <inputFile> -o <outputFile>')
    input_file = './input/network.dat'
    output_file = './output/community.dat'
    for o in opts:
        opt = o[0]
        value = o[1]
        if opt == '-i':
            input_file = value
        if opt == '-o':
            output_file = value
    g: nx.Graph = nx.read_edgelist(str(input_file))
    lpanni.LPANNI(g)
    gen = generator.GraphGenerator(0.1, g)
    communities = gen.get_Overlapping_communities()
    f = open(output_file, 'w')
    for community in communities:
        for u in community:
            f.write(str(u) + ' ')
        f.write('\n')
    f.flush()
    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
