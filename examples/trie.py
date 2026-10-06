
class Node:
    def __init__(self):
        self.children = {}
        self.letter = None
        self.isEnd = False
        self.wholeWord = ""
tria = Node()


def insert(tria, key):
    child = tria
    i = 0
    while key[i] in child.children.keys():
        child = child.children[key[i]]
        i += 1 

    for j in range(i,len(key)):
        node = Node()
        node.letter = key[j]
        child.children[key[j]] = node
        child = child.children[key[j]]
    child.isEnd = True
    child.wholeWord = key
    return tria

def prefix(trie,prefix):
    child = tria
    i = 0
    while len(child.children.keys()) > 0 and i < len(prefix):
        child = child.children[prefix[i]]
        i += 1 
    dump(child)

def dump(tree):
    node = tree
    queue = []
    queue.extend(node.children.values())
    while queue:
        node = queue.pop()
        if node.isEnd:
            print(node.wholeWord)
        queue.extend(node.children.values())
        
        
        
tria = insert(tria, "test")
tria = insert(tria, "teryaki")
tria = insert(tria, "kucho")
prefix(tria,"k")