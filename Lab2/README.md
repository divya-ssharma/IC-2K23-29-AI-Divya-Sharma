# Lab 2

Name: Divya Sharma  
Roll No: IC-2K23-29

This lab implements BFS, DFS, hill climbing and A* search. The same graph is used across all three files so that the outputs can be compared directly.

BFS and DFS are implemented together in bfs_dfs.py. BFS returns the shortest path, while DFS returns the first path it reaches. Hill climbing works on a numeric state where the goal is 10, moving one step at a time towards it. A* uses the graph again with heuristic values on each node and expands the node with the lowest f = g + h.

For this graph hill climbing reaches the goal without getting stuck, although on a larger state space it can fail when both neighbours are worse than the current state.
