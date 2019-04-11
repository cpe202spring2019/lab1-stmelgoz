
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   max = 0
   if int_list == []:
       return None
   if int_list == None:
       raise ValueError('no list')
   for i in range(len(int_list)):
       if int_list[i] > max:
           max = int_list[i]
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError""
   
   if int_list == None:
       raise ValueError
   elif (len(int_list) == 1):
       return int_list[0]
   else:
       newl = int_list[-(len(int_list)-1):-1]
       new_intl = reverse_rec(newl)
       return new_intl
   
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError
   else:
       if high > low: 
           mid = 1 + (len(int_list)-1)/2
           if int_list[mid] == target:
               return mid
           elif int_list[mid] > target:
               return bin_search(target, low, mid-1, int_list)
           elif int_list[mid] < target:
                return bin_search(target, mid+1, high, int_list)
           else:
                return None
   
