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
