# java 示例代码
"""
Deque<String> deque = new LinkedList<String>();
deque.push("a");
deque.push("b");
deque.push("c");
System.out.println(deque);

String str = deque.peek();
System.out.println(str);
System.out.println(deque);

while (deque.size()>0){
    System.out.println(deque.pop());
}
System.out.println(deque);
"""

# add first改写后的代码
"""
Deque<String> deque = new LinkedList<String>();
deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

String str = deque.getFirst();
System.out.println(str);
System.out.println(deque);

while (deque.size()>0){
    System.out.println(deque.removeFirst());
}
System.out.println(deque);
"""

# add last改写后的代码
"""
Deque<String> deque = new LinkedList<String>();
deque.addLast("a");
deque.addLast("b");
deque.addLast("c");
System.out.println(deque);

String str = deque.getLast();
System.out.println(str);
System.out.println(deque);

while (deque.size()>0){
    System.out.println(deque.removeLast());
}
System.out.println(deque);
"""


