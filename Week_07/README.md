# 第七周学习笔记

## 1.回顾

树  Tree

```
               root                        
             /      \                    
         root.left   root.right
```



二叉搜索树

定义：子树的关系，任何一个节点它的左子树的所有节点都要小于这个根节点，它的右子树的所有根节点都要大于根节点，中序遍历（左根右）是升序序列。

查找的时间复杂度较少为logn

当二叉搜索树退化成链表，最差的时间复杂度为O(n)

此时需要平衡二叉树(AVL)，要求balance factor（平衡因子）：是他的左子树的高度减去右子树的高度。

balance factor的取值范围为-1, 0, 1

可进行的旋转操作有

- 左旋
- 右旋
- 左右旋
- 右左旋

红黑树的要求则不那么严格，只要能保证任何一个结点的左右子树的高度差小于两倍，或者说只需要balance factor 不超过2倍即可，这样减少平衡的操作的次数。

- 每个节点要么是红色，要么是黑色
- 根节点是黑色
- 每个叶节点（NIL节点，空节点）是黑色的
- 不能有相邻接的两个红色节点
- 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点



对于写入操作多的，建议采用红黑树

对于经常读取的，可以采用AVL



## 2.Trie树（字典树）

基本结构：是一种树形结构，典型应用于统计和排序大量的字符串，常用于搜索引擎系统用于文本词频统计。优点是最大限度地减少无谓的字符串的比较，查询效率比哈希表高。



基本性质：

- 节点本身不存完整单词
- 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串
- 每个节点的所有子节点路径代表的字符串都不相同



```python
#208.实现Trie（前缀树）
#实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
```

```python
#解题方式一：
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#" 

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```



```python
#解题方式二：更加简洁的版本
class Trie:

    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```



## 3.并查集

基本操作：

- makeSet(s):建立一个新的并查集，其中包含s个单元素集合。
- unionSet(x,y):把元素x和元素y所在的集合合并，要求x和y所在的集合并不相交，如果相交则不合并。
- find(x):找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将他们各自的代表比较一下即可。

```python
def init(p):
    #for i = 0..n; p[i] = i;
    p = [i for i in range(n)]
    
def union(self, p, i, j):
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] != root:
        root = p[root]
    while p[i] != i:
        x = i
        i = p[i]
        p[x] = root
    return root
```



## 4.高级搜索

初级搜索：

- 朴素搜索

- 优化方式：不重复(fibonacci)、剪枝（生成括号问题）

- 搜索方向：

  - DFS:depth first search 深度优先搜索
  - BFD:breadth first search 广度优先搜索

  双向搜索、启发式搜索（优先队列）



BFS代码

```python
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```



```python
#例题1：22.括号生成
#数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```



解题方式一：回溯

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
```

解题方式二：剪枝

```java
class Solution {
    public List<String> result;
    
    public List<String> generateParenthesis(int n) {
        result = new ArrayList<String>();
        _generate(0, 0, n, "");
        return result;
    }

    private void _generate(int left, int right, int n, String s){
        // terminator
        if (left == n && right ==n){
            // filter out the invalid parentheses.
            result.add(s);
            return;
        }

        // process

        //drill down
        if (left < n)
            _generate(left + 1, right, n, s + "(");

        if (right < n && right <left)
            _generate(left, right + 1, n, s + ")");
        
        //restore
    }
}
```



```python
#51.N皇后
#回溯法
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
         # 回溯法
        res = []
        s = '.' * n
        def backtrack(path=[], i=0, col_selected=[], z_diag=set(), f_diag=set()):
            if i == n:
                res.append(path)
                return 
            for j in range(n):
                if j not in col_selected and i-j not in z_diag and i+j not in f_diag:
                    backtrack(path+[s[:j]+'Q'+s[j+1:]], i+1, col_selected+[j], z_diag|{i-j}, f_diag|{i+j})
            
        backtrack()
        return res

```





```python
#37.解数独
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1,10)) for _ in range(9)] #行剩余可用数字
        col = [set(range(1,10)) for _ in range(9)] #列剩余可用数字
        block = [set(range(1,10)) for _ in range(9)] #块剩余可用数字

        empty = []  #收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  #更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))
        
        def backtrack(iter = 0):
            if iter == len(empty):  #处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  #回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack() 
```





启发式搜索：

- 启发式函数:h(n)， 他用来评价那些节点最希望的是一个我们要找到的节点，h(n)会返回一个非负实数，也可以认为是从节点n的目标节点路径的估价成本。

启发式函数是一种告知搜索方向的一个算法，他提供一种明智的方法来猜测那个邻居节点会导向一个目标。



