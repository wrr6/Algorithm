# python实现
class Stack:
    def __init__(self):
        self.items = ['X', 'Y']

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def length(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

"""
分析：
Stack的实现也是使用一个列表List,特点是后进先出
使用append方法添加元素到栈中，时间复杂度为O(1)
出栈使用pop()，将栈顶元素pop出去，时间复杂度为O(1)

Queue的实现是使用一个空列表List,特点是先进先出
使用append方法添加元素到队列中，时间复杂度为O(1)
出队则用pop(0)，时间复杂度为O(N)，需要将列表中的第一个元素pop之后，将后面的元素往前移动

Priority Queue
1.插入操作:O(1)
2.取出操作:O(logN) - 按照元素的优先级取出
3.底层具体实现的数据结构较为多样化和复杂:heap堆、bst二叉树、treap
"""

# java实现  (看不懂)
"""
  1: /* Stack.java - Class that provides a Last In First Out (LIFO)
   2:    datatype, known more commonly as a Stack
   3:    Copyright (C) 1998, 1999, 2001, 2004, 2005
   4:    Free Software Foundation, Inc.
   5: 
   6: This file is part of GNU Classpath.
   7: 
   8: GNU Classpath is free software; you can redistribute it and/or modify
   9: it under the terms of the GNU General Public License as published by
  10: the Free Software Foundation; either version 2, or (at your option)
  11: any later version.
  12: 
  13: GNU Classpath is distributed in the hope that it will be useful, but
  14: WITHOUT ANY WARRANTY; without even the implied warranty of
  15: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  16: General Public License for more details.
  17: 
  18: You should have received a copy of the GNU General Public License
  19: along with GNU Classpath; see the file COPYING.  If not, write to the
  20: Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
  21: 02110-1301 USA.
  22: 
  23: Linking this library statically or dynamically with other modules is
  24: making a combined work based on this library.  Thus, the terms and
  25: conditions of the GNU General Public License cover the whole
  26: combination.
  27: 
  28: As a special exception, the copyright holders of this library give you
  29: permission to link this library with independent modules to produce an
  30: executable, regardless of the license terms of these independent
  31: modules, and to copy and distribute the resulting executable under
  32: terms of your choice, provided that you also meet, for each linked
  33: independent module, the terms and conditions of the license of that
  34: module.  An independent module is a module which is not derived from
  35: or based on this library.  If you modify this library, you may extend
  36: this exception to your version of the library, but you are not
  37: obligated to do so.  If you do not wish to do so, delete this
  38: exception statement from your version. */
  39: 
  40: 
  41: package java.util;
  42: 
  43: /* Written using "Java Class Libraries", 2nd edition, ISBN 0-201-31002-3
  44:  * "The Java Language Specification", ISBN 0-201-63451-1
  45:  * plus online API docs for JDK 1.2 beta from http://www.javasoft.com.
  46:  * Status:  Believed complete and correct
  47: 
  48: /**
  49:  * Stack provides a Last In First Out (LIFO) data type, commonly known
  50:  * as a Stack.  Stack itself extends Vector and provides the additional
  51:  * methods for stack manipulation (push, pop, peek). You can also seek for
  52:  * the 1-based position of an element on the stack.
  53:  *
  54:  * @author Warren Levy (warrenl@cygnus.com)
  55:  * @author Eric Blake (ebb9@email.byu.edu)
  56:  * @see List
  57:  * @see AbstractList
  58:  * @see LinkedList
  59:  * @since 1.0
  60:  * @status updated to 1.4
  61:  */
  62: public class Stack<T> extends Vector<T>
  63: {
  64:   // We could use Vector methods internally for the following methods,
  65:   // but have used Vector fields directly for efficiency (i.e. this
  66:   // often reduces out duplicate bounds checking).
  67: 
  68:   /**
  69:    * Compatible with JDK 1.0+.
  70:    */
  71:   private static final long serialVersionUID = 1224463164541339165L;
  72: 
  73:   /**
  74:    * This constructor creates a new Stack, initially empty
  75:    */
  76:   public Stack()
  77:   {
  78:   }
  79: 
  80:   /**
  81:    * Pushes an Object onto the top of the stack.  This method is effectively
  82:    * the same as addElement(item).
  83:    *
  84:    * @param item the Object to push onto the stack
  85:    * @return the Object pushed onto the stack
  86:    * @see Vector#addElement(Object)
  87:    */
  88:   public T push(T item)
  89:   {
  90:     // When growing the Stack, use the Vector routines in case more
  91:     // memory is needed.
  92:     // Note: spec indicates that this method *always* returns obj passed in!
  93: 
  94:     addElement(item);
  95:     return item;
  96:   }
  97: 
  98:   /**
  99:    * Pops an item from the stack and returns it.  The item popped is
 100:    * removed from the Stack.
 101:    *
 102:    * @return the Object popped from the stack
 103:    * @throws EmptyStackException if the stack is empty
 104:    */
 105:   public synchronized T pop()
 106:   {
 107:     if (elementCount == 0)
 108:       throw new EmptyStackException();
 109: 
 110:     modCount++;
 111:     T obj = elementData[--elementCount];
 112: 
 113:     // Set topmost element to null to assist the gc in cleanup.
 114:     elementData[elementCount] = null;
 115:     return obj;
 116:   }
 117: 
 118:   /**
 119:    * Returns the top Object on the stack without removing it.
 120:    *
 121:    * @return the top Object on the stack
 122:    * @throws EmptyStackException if the stack is empty
 123:    */
 124:   public synchronized T peek()
 125:   {
 126:     if (elementCount == 0)
 127:       throw new EmptyStackException();
 128: 
 129:     return elementData[elementCount - 1];
 130:   }
 131: 
 132:   /**
 133:    * Tests if the stack is empty.
 134:    *
 135:    * @return true if the stack contains no items, false otherwise
 136:    */
 137:   public synchronized boolean empty()
 138:   {
 139:     return elementCount == 0;
 140:   }
 141: 
 142:   /**
 143:    * Returns the position of an Object on the stack, with the top
 144:    * most Object being at position 1, and each Object deeper in the
 145:    * stack at depth + 1.
 146:    *
 147:    * @param o The object to search for
 148:    * @return The 1 based depth of the Object, or -1 if the Object
 149:    *         is not on the stack
 150:    */
 151:   public synchronized int search(Object o)
 152:   {
 153:     int i = elementCount;
 154:     while (--i >= 0)
 155:       if (equals(o, elementData[i]))
 156:         return elementCount - i;
 157:     return -1;
 158:   }
 159: }
"""
