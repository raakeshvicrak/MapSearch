#A* is the best algorithm for finding the optimal path given the heuristic function is correct.
#Heuristic function is the straight line distance between the current node and the goal node.
#for our assignment IDS is the fastest algoritm
#DFS is the most efficient algorithm in terms of memory. 
import mapSearch_BFS;
import mapSearch_DFS;
import mapSearch_Astar;
import mapSearch_IDS;
import sys;

if sys . argv [ 4 ].lower() == "bfs":
    mapSearch_BFS.input_function(sys . argv [ 1 ], sys . argv [ 2 ], sys . argv [ 3 ]);

    mapSearch_BFS.file_reading();

    mapSearch_BFS.search_algorithm();

elif sys . argv [ 4 ].lower() == "dfs":
    mapSearch_DFS.input_function(sys . argv [ 1 ], sys . argv [ 2 ], sys . argv [ 3 ]);

    mapSearch_DFS.file_reading();

    mapSearch_DFS.search_algorithm();

elif sys . argv [ 4 ].lower() == "astar":
    mapSearch_Astar.input_function(sys . argv [ 1 ], sys . argv [ 2 ], sys . argv [ 3 ]);

    mapSearch_Astar.file_reading();

    mapSearch_Astar.search_algorithm();

elif sys . argv [ 4 ].lower() == "ids":
    mapSearch_IDS.input_function(sys . argv [ 1 ], sys . argv [ 2 ], sys . argv [ 3 ]);

    mapSearch_IDS.file_reading();

    mapSearch_IDS.search_algorithm();
    
