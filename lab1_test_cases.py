import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Finds max from a list of numbers."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        alist = []
        self.assertEqual(max_list_iter(alist), None) #used to check for an empty list
        blist = [1,2,3]
        self.assertEqual(max_list_iter(blist), 3) #used to check for max at end
        clist = [4,2,1]
        self.assertEqual(max_list_iter(clist), 4) #used to check for max at start of list
        dlist = [1,3,9,7,0]
        self.assertEqual(max_list_iter(dlist), 9) #used to check for max at middle
        elist = [1,10,3,4,7]
        self.assertEqual(max_list_iter(elist), 10) #used to check for max at in between
        flist = [4,6,3,11,2]
        self.assertEqual(max_list_iter(flist), 11) #used to check for max at in between
        glist = [1,2,3,3]
        self.assertEqual(max_list_iter(glist), 3) #used to check with repeating nums
        hlist = [2,2,2,5]
        self.assertEqual(max_list_iter(hlist), 5) #used to check with repeating nums
        ilist = [1,1,1,1]
        self.assertEqual(max_list_iter(ilist), 1) #used to check with repeating nums


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #checks if it reverses the order
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3]) #checks if it reverses the order
        self.assertEqual(reverse_rec([0,0,0]),[0,0,0]) #reverses the order even if same values
        self.assertEqual(reverse_rec([0]),[0]) #checks if there's a single element
        self.assertEqual(reverse_rec(None),None) #checks if there's a list

    #def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) #checks for mid
        a_val = [2,3,4,17,18,23] 
        low1 = 2
        high1 = len(a_val) -1 
        self.assertEqual(bin_search(17, 2, len(a_val)-1, a_val), 17 ) #checks for mid
        b_val = [33,14,23,22,12,6,8,9,10]
        low2 = 6
        high2 = len(b_val) -1
        self.assertEqual(bin_search(12, 6, len(b_val)-1, b_val), 12 ) #checks for mid
        c_val = [2,3,4,65,4,33,21,1]
        low3 = 1
        high3 = len(c_val) -1
        self.assertEqual(bin_search(4, 1, len(c_val)-1, c_val), 4 ) #checks for mid
        d_val = None
        low4 = 1
        high4 = len(d_val) -1
        with self.assertRaises(ValueError):
            bin_search(None, 1, len(d_val)-1, d_val), None) #checks for exception


if __name__ == "__main__":
        unittest.main()

    
