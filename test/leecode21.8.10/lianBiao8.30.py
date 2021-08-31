"""
二 链表
链表是一种通过指针串联在一起的线性结构，每一个节点是又两部分组成，一个是数据域一个是指针域（存放指向下一个节点的指针），最后一个节点的指针域指向null（空指针的意思）
数据类型：
1.以上为单链表：单链表中的节点只能指向节点的下一个节点。
2，双链表：每一个节点有两个指针域，一个指向下一个节点，一个指向上一个节点。
3.循环链表，顾名思义，就是链表首尾相连。循环链表可以用来解决约瑟夫环问题。
链表的存储方式：
1.通过指针域的指针链接在内存中各个节点，所以链表中的节点在内存中不是连续分布的 ，而是散乱分布在内存中的某地址上，分配机制取决于操作系统的内存管理
删除节点：只要把指向该节点的指针指向别处即可，该该节点不被任何指向后，释放该节点内存（Java和Python有自己自动内存回收机制,C和C++需要手动释放）
新增节点：指向新的节点，新节点的指向指向原指向节点，串联起来即可
链表增添和删除时间复杂度是O(1)操作，查找的是O(n)
"""
"""
1.#203.移除链表元素
https://leetcode-cn.com/problems/remove-linked-list-elements/
题意：删除链表中等于给定值 val 的所有节点。
示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
"""
# Definition for singly-linked list.
head = [1,2,6,3,4,5,6]
val = 6

class ListNode():
    def __init__(self, val,next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head) #设置一个虚拟头结点在进行删除操作。
        cur = dummy_head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next

"""
2.设计链表及基础方法
"""
# 单链表
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head = Node(0)  # 虚拟头部节点
        self._count = 0  # 添加的节点数

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 计数累加
        self._count += 1

        add_node = Node(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            # 计数-1
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None


# 双链表
# 相对于单链表, Node新增了prev属性
class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head, self._tail = Node(0), Node(0)  # 虚拟节点
        self._head.next, self._tail.prev = self._tail, self._head
        self._count = 0  # 添加的节点数

    def _get_node(self, index: int) -> Node:
        # 当index小于_count//2时, 使用_head查找更快, 反之_tail更快
        if index >= self._count // 2:
            # 使用prev往前找
            node = self._tail
            for _ in range(self._count - index):
                node = node.prev
        else:
            # 使用next往后找
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node, val)

    def _update(self, prev: Node, next: Node, val: int) -> None:
        """
            更新节点
            :param prev: 相对于更新的前一个节点
            :param next: 相对于更新的后一个节点
            :param val:  要添加的节点值
        """
        # 计数累加
        self._count += 1
        node = Node(val)
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            node = self._get_node(index)
            # 计数-1
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev
"""
3.反转指针
#双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre
"""
class ListNode1():
    def __init__(self,head=0):
        self.head=head
        self.next=None
class FF():
    def fun(self,listNode):
        pre=None
        cur=listNode
        while cur.next != None:
            tem=cur.next
            cur.next=pre
            pre=cur
            cur=tem
        return pre
# Definition for singly-linked list.
"""
4.两两交换链表中的节点：
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # 设置一个虚拟头结点
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            tmp = cur.next  # 记录临时节点
            tmp1 = cur.next.next.next  # 记录临时节点

            cur.next = cur.next.next  # 步骤一
            cur.next.next = tmp  # 步骤二
            cur.next.next.next = tmp1  # 步骤三

            cur = cur.next.next  # cur移动两位，准备下一轮交换
        return dummy.next
"""
5.链表删除倒数第n个节点
双指针的经典应用，如果要删除倒数第n个节点，
思路：让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        while(n!=0): #fast先往前走n步
            fast = fast.next
            n -= 1
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next #删除
        return head_dummy.next
"""
6.链表相交
题目链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。
换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA, lengthB = 0, 0
        curA, curB = headA, headB
        while (curA != None):  # 求链表A的长度
            curA = curA.next
            lengthA += 1

        while (curB != None):  # 求链表B的长度
            curB = curB.next
            lengthB += 1

        curA, curB = headA, headB

        if lengthB > lengthA:  # 让curA为最长链表的头，lenA为其长度
            lengthA, lengthB = lengthB, lengthA
            curA, curB = curB, curA

        gap = lengthA - lengthB  # 求长度差
        while (gap != 0):
            curA = curA.next  # 让curA和curB在同一起点上
            gap -= 1

        while (curA != None):
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None

"""
7.环形链表II
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
7.1找到环入口
思路：先通过快慢指针通过是否相遇判断哪是否有环；再x + y = n (y + z)转换为x = (n - 1) (y + z) + z 注意这里n一定是大于等于1的，因为 fast指针至少要多走一圈才能相遇slow指针。
x为头到入口，y为入口到相遇点，z相遇点到入口
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None