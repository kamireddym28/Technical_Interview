## Question 1:
def anagram(s1, t1):
    s1 = list(s1)
    t1 = list(t1)
    s1.sort()
    t1.sort()
    return s1 == t1

def question1(s, t):
    complete_string = len(s)
    matching_substring = len(t)
    for i in range(complete_string - matching_substring + 1):
        if anagram(s[i: i+matching_substring], t):
            return True
    return False

def q1():
    print question1('udacity', 'ad')
    print question1('udacity', ' ')
    print question1('udacity', 'yt')
    
q1()

print ('******************************************************')

## Question 2:
def question2(s):
  start = 0
  end = 0
  for i in range(len(s)):
    left, right = form_palindrome(s, i, i)
    if right - left > end - start:
      start = left
      end = right
    left, right = form_palindrome(s, i, i + 1)
    if right - left > end - start:
      start = left
      end = right
  return s[start:end + 1]

def form_palindrome(s, left, right):
  if right >= len(s):
    return (0, 0)
  start = left
  end = right
  while start >= 0 and end < len(s) and s[start] == s[end]:
    start -= 1
    end += 1
  return (start + 1, end - 1)

def q2():
    print question2('babad')
    print question2('banana')
    print question2('my favorite ferrariracecar')
    print question2('AXZCBACAECBBCEA')
    print question2('a')

q2()

print ('******************************************************')

## Question 4:

def question4(T, root, n1, n2):
    if (n1 > root and n2 < root) or (n1 < root and n2 > root):
        return root
    elif (n1 < root and n2 < root):
        l = T[root].index(1)
        if n1 == l or n2 == l:
            return root
        else:
            root = l
    elif (n1 > root and n2 > root):
        r = len(T[root]) - T[root][::-1].index(1) - 1
        if n1 == r or n2 == r:
            return root
        else:
            root = r
            
    return question4(T, root, n1, n2)


def q4():
    print question4([[0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [1, 0, 0, 0, 1], 
           [0, 0, 0, 0, 0]], 3, 1, 4)

    print question4([[0, 1, 0, 1],
                    [0, 0, 0, 0],
                    [1, 0, 1, 0],
                    [1, 1, 1, 0]], 0, 2, 4)
    
    print question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 6, 8, 10)

q4()

print ('******************************************************')

## Question 5:

global head
head = None

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def push(new_data):
    global head
    new_node = Node(new_data)
    new_node.next = head
    head = new_node

def question5(head, m):
    node_start = head
    ref_node = head

    count = 0

    if(head is not None):
        while(count < m):
            ref_node = ref_node.next
            count += 1


    while(ref_node is not None):
        node_start = node_start.next
        ref_node = ref_node.next

    return node_start.data

push("nine")
push("eight")
push("seven")            
push("six")
push("five")
push("four")
push("three")
push("two")
push("one")            
push("zero")
    
def q5():
    print(question5(head, 4))
    print(question5(head, 10))
    print(question5(head, 1))

q5()
print ('******************************************************')
