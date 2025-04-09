#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
AVL: insertion & deletion
'''

from algopy import avl, bintree



#------------------------------------------------------------------------------
# rotations: works only in "useful" cases

def lr(A): # left rotation
    '''
    A: AVL
    applies a left rotation on A and returns the new root of the AVL
    '''
    aux = A.right
    A.right = aux.left
    aux.left = A
    aux.bal += 1
    A.bal = -aux.bal
    return aux

def rr(A): # right rotation
    '''
    A: AVL
    applies a right rotation on A and returns the new root of the AVL
    '''
    aux = A.left
    A.left = aux.right
    aux.right = A
    aux.bal -= 1
    A.bal = -aux.bal
    return aux

def lrr(A): # left-right rotation
    '''
    A: AVL
    applies a left-right rotation on A and returns the new root of the AVL
    '''
    # left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
    # right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A

def rlr(A): # right-left rotation
    '''
    A: AVL
    applies a right-left rotation on A and returns the new root of the AVL
    '''
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    
    (aux.left.bal, aux.right.bal) = (0, 0)
    if aux.bal == -1:
        aux.left.bal = 1
    elif aux.bal == 1:
        aux.right.bal = -1
    aux.bal = 0

    return aux

#------------------------------------------------------------------------------
        
'''
insertion
'''

def __insertAVL(A, x):
    '''
    A: AVL
    x: element
    inserts x in the AVL A if it is not already in the AVL
    returns (newA, b) where
    - newA is the potentially new root of the AVL
    - b is True if the height of the AVL A has changed, False otherwise
    '''
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    else:
        if x < A.key:
            (A.left, dh) = __insertAVL(A.left, x)
            if not dh:
                return (A, False)
            else:
                A.bal += 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == 1:
                    return (A, True)
                else: # A.bal == 2
                    if A.left.bal == 1:
#                        print(x, "rr", A.key)
                        A = rr(A)
                    else:
#                        print(x, "lrr", A.key)
                        A = lrr(A)
                    return (A, False)
        else:   # x > A.key
            (A.right, dh) = __insertAVL(A.right, x)
            if not dh:
                return (A, False)
            else:
                A.bal -= 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == -1:
                    return (A, True)
                else:
                    if A.right.bal == -1:
#                        print(x, "lr", A.key)
                        A = lr(A)
                    else:
#                        print(x, "rlr", A.key)
                        A = rlr(A)
                    return (A, False)
                    
            
            
def insertAVL(A, x):
    '''
    A: AVL
    x: element
    inserts x in the AVL A if it is not already in the AVL
    returns the potentially new root of the AVL
    '''
    (A, dh) = __insertAVL(A, x)
    return A
        

def buildAVLfromList(L, A = None):
    for x in L:
        A = insertAVL(A, x)
    return A

'''
deletion
'''

# non optimized

def maxBST(B):
    '''
    B: Non-empty AVL
    returns the maximum element of the AVL B
    '''
    while B.right != None:
        B = B.right
    return B.key
    
def __deleteAVL(A, x):
    '''
    A: AVL
    x: element
    deletes the element x in the AVL A
    returns (newA, b) where
    - newA is the potentially new root of the AVL
    - b is True if the height of the AVL A has changed, False otherwise
    '''
    if A == None:
        return (None, False)
        
    elif x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key   # to use the case <=
        else:
            if A.left == None:
                return(A.right, True)
            else:
                return(A.left, True)
                
    if x <= A.key:      
        (A.left, dh) = __deleteAVL(A.left, x)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1              # long version
            if A.bal == 0:
                return (A, True)
            elif A.bal == -1:
                return (A, False)
            else:   # A.bal == -2
                if A.right.bal == -1:
#                    print("lr", A.key)
                    A = lr(A)
                    return (A, True)
                elif A.right.bal == 0:
#                    print("lr", A.key)
                    A = lr(A)
                    return (A, False)
                else:
#                    print("rlr", A.key)
                    A = rlr(A)
                    return (A, True)
           
    else:   # x > A.key
        (A.right, dh) = __deleteAVL(A.right, x)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == -1:
#                    print("lrr", A.key)
                    A = lrr(A)
                else:
#                    print("rr", A.key)
                    A = rr(A)
            return (A, A.bal == 0)  
                   # this shortcut also works in previous case!

def deleteAVL(A, x):
    '''
    A: AVL
    x: element
    deletes the element x in the AVL A
    returns the potentially new root of A
    '''
    (A, _) = __deleteAVL(A, x)
    return A



#------------------------------------------------------------------------------

# trees for tests

B =  bintree.load("files/bst_hbalanced.bintree")
B1 = bintree.load("files/bst_not-hbalanced1.bintree")    # not a BST
B2 = bintree.load("files/bst_not-hbalanced2.bintree")    # not height-balanced
B3 = bintree.load("files/bst_wrong.bintree")    # not height-balanced






