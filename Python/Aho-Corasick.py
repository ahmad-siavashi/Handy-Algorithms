# http://marios.io/2012/02/26/string-searching-using-aho-corasick/
from collections import deque

class Node(object):
    def __init__(self,ch=None,transitions=[],results=[],fail=None):
        self.ch = ch
        self.transitions = transitions
        self.results = results
        self.fail = fail

def BuildTrie(keywords):
    root = Node(None,[],[],None)
    root.fail = root
    queue = deque([root])
    for keyword in keywords:
        current_node = root
        for char in keyword:
            new_node = None
            for transition in current_node.transitions:
                if transition.ch == char:
                    new_node = transition
                    break
     
            if new_node is None:
                new_node = Node(char)
                current_node.transitions.append(new_node)
                if current_node is root:
                    new_node.fail = root
     
            current_node = new_node
        current_node.results.append(keyword)
    
    while queue:
        current_node = queue.popleft()
        for node in current_node.transitions:
            queue.append(node)
            fail_state_node = current_node.fail
            while not any(x for x in fail_state_node.transitions if node.ch == x.ch) and fail_state_node is not root:
                fail_state_node = fail_state_node.fail
     
            node.fail = next((x for x in fail_state_node.transitions if node.ch == x.ch and x is not node), root)
     
    return root

def Search(tree_root,text):
    current_node = tree_root
    for c in text:
        transition = None
        while transition is None and transition is not tree_root:
            transition = next((x for x in current_node.transitions if x.ch == c), current_node.fail)
     
        current_node = transition
     
        if len(transition.results) > 0:
            for result in transition.results:
                yield result
            current_node = transition.fail


r = BuildTrie(['He'])
