# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:00:37 2017

@author: zhangmin



You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



"""


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def is_empty(self):
        return self.head is None
  
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
  
    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data
            
    def get_element(self, idx):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('the list is an empty list')
        while cur_idx < idx :
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx +=1
        return cur.data
  
    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:             # 判断是否是空链表
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:   # 遍历链表
            cur = cur.next
            if cur is None:   # 判断是不是最后一个元素
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node
  
    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        if idx == 0:   # 当删除第一个节点时
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:   # 当只有一个节点的链表时
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 当删除的节点是链表最后一个节点时
            self.tail = cur
  
    def size(self):
        current = self.head
        count = 0
        if current is None:
            return 'The list is an empty list'
        while current is not None:
            count += 1
            current = current.next
        return count
  
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
  
#    if __name__ == '__main__':
    
    
#    print(link_list.is_empty())
#    link_list.insert(10, 30)
  
#    link_list.remove(0)
  
#    for node in link_list1.iter():
#        print('node is {0}'.format(node))
#    print(link_list1.size())
#    
#    for node in link_list2.iter():
#        print('node is {0}'.format(node))
#    print(link_list2.size())
#    print(link_list.search(20))
    

def addTwoNumbers( l1, l2):
    cur = 0
    carry = 0
    l1_len = l1.size()
    l2_len = l2.size()
    result = LinkedList()
    while l1_len or l2_len  :
        temp = l1.get_element(cur) if l1_len else 0
        sum = (l1.get_element(cur) if l1_len else 0) + (l2.get_element(cur) if l2_len else 0) + carry
        carry = int(sum / 10)
        print(carry)
#        print(temp)
        result.append(sum % 10)
        
        if l1_len:
            l1_len = l1_len - 1
        if l2_len:
            l2_len = l2_len - 1
#        print(cur)    
        cur = cur + 1
        
        
    
    if carry > 0 :
        result.append(carry)
        
    for node in result.iter():
        print('node is {0}'.format(node))
        
#        cur = cur.next  
#        if l1:
#            l1 = l1
            
    



link_list1 = LinkedList()
    
link_list2 = LinkedList()

for i in [2,4,3]:

    link_list1.append(i)
    
for i in [5,6,4]:
    link_list2.append(i)


addTwoNumbers(link_list1,link_list2)

  


