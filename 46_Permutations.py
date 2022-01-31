'''
46. Permutations (https://leetcode.com/problems/permutations/)

- Basically treat it as a graph and find all paths that visit everything
- A lot of it is simplified
    - all nodes are connected, so they can always go to any of the other numbers
    - just need to keep track of visited
- Have to remember that working arrays must be copied
- I use a dict for visited since numbers can be negative as well
'''

def find_paths(res, nums, visited, path, cur):
    # add to path so far, mark visited
    path.append(cur)
    visited[cur] = True;

    # if path is full, we add to res list and stop
    if len(path) == len(nums):        
        res.append(path)
        return
    
    # otherwise, go thru and visit each of the remaining (non-visited) numbers
    for i in nums:
        if not visited[i]:
            find_paths(res, nums, visited.copy(), path[:], i)
            # ^ note that we need to provide copy of visited and path
     
            
class Solution(object):
    def permute(self, nums):
        res = []
        visited = {k : False for k in range(-10,11)} # gen dict with all False
        
        # find paths starting from each number
        for i in nums:
            find_paths(res, nums, visited.copy(), [], i)
        
        return res
