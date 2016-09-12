def reverse_base(base,material = 'RNA'):
  """reverse the single base"""
  if material == 'DNA':
       if base in 'Tt':
             return 'A'
       elif base in 'Aa':
             return 'T'
       elif base in 'Cc':
             return 'G'
       elif base in 'Gg':
             return 'C'
  if material == 'RNA':
      if base in 'Uu':
           return 'A'
      elif base in 'Aa':
           return 'U'
      elif base in 'Cc':
           return 'G'
      elif base in 'Gg':
           return 'C'

def reverse_seq(str):
    """reverse the DNA sequence"""
    l = len(str)
    seq = ''
    for i in range(l):
        seq += reverse_base(str[l-i-1])
    return seq

def reverse_seq2(str):
    """reverse the DNA sequence"""
    l = len(str)
    seq = ''
    i = 0;
    while i < l:
        seq += reverse_base(str[l-i-1])
        i += 1
    return seq

def LCS(str1, str2):
    """to find Longest common substring"""

    if len(str1) > len(str2) :
        str3 = str1
        str1 = str2
        str2 = str3
    l1 = len(str1)
    l2 = len(str2)

    num = 0;
    longstring = '';

    for i in range(l1):
      for j in range(l1-i):
        if str2.find(str1[i:j+1]) > -1 and j > num:
            num = j
            longstring = str1[i:j+1]
    return longstring

def parentheses_check(str):
    """check the parentheses"""

    l = len(str)
    num1 = 0
    num2 = 0
    for i in range(l):
      if str[i] == '(':
          num1 += 1
      if str[i] == ')':
          num2 += 1
    if num1 == num2:
         return True
    return False


def rna_ss_validator(str1,str2,wobble = True):
    """examin whether the sequence is valid"""
    if not parentheses_check(str2):
        return False
    num = 0
    couple = [(0,0)] * 100
    coupleleft = [True] * 100
    l = len(str2)
    for i in range(l):
      if str2[i] == '(':
         coupleleft[i] = False
      elif str2[i] == ')':
          j = i-1
          while coupleleft[j] == True:
                 j -= 1
          if i-j < 4:
              return False
          if wobble:
              if str1[j] != reverse_base(str1[i]):
                  if not((str1[i]=='G' and str1[j]=='U') or (str1[j]=='G' and str1[i]=='U')):
                      return False
          elif str1[j] != reverse_base(str1[i]):
              return False
          coupleleft[j] = True
          couple[num] = (j,i)
          num += 1
    return True,couple[0:num]
