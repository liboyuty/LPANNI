# LPANNI
implement for LPANNI: Overlapping Community Detection Using Label Propagation in Large-Scale Complex Networks


### usage
`main.py -i <inputFile> -o <outputFile>`

inputFile:edgelist
>for example

1 2
2 3
3 4
23 45
...

### note
节点的归属系数：设置节点对社区c的归属系数>0.1表示节点属于c社区，可以通过main.py中的generator的初始化来设置这个系数。
