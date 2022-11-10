#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains a set of functions to decode the Pfafstetter coding system including
a modified version that is used by within the HydroBASINS dataset 
(https://www.hydrosheds.org/products/hydrobasins).

Created on Tue Oct 25 16:57:03 2022

@author: vincent
"""

def odd(n, oddOrZero = False):
    """Checks if number is odd.
    
    If the argument 'oddOrZero' is set to True zero is also 
    treated as odd.
    
    Parameters
    ----------
    n : int
        A single number to be checked
    
    oddOrZero : bool, optional
        If set to True zero is odd as well (default is False)
    
    """
    if oddOrZero and n == 0:
        return True
    if n % 2 == 0:
        return False
    else:
        return True

def allodd(x, oddOrZero = False):
    """Checks if all digits in a number are odd.
    
    If the argument 'oddOrZero' is set to True zero is also 
    treated as odd.
    
    Parameters
    ----------
    x : str
        A single number with one or more digits to be checked
    
    oddOrZero : bool, optional
        If set to True zero is odd as well (default is False)
    
    """    
    for i in str(x):
        if not odd(int(i), oddOrZero = oddOrZero):
            return(False)
    return(True)

def upstream(a,b,oddOrZero=False):
    """Checks if b is upstream of a.
    
    The argument 'oddOrZero' can be set to True if the Pfafstetter code is 
    modified and uses Zeros that need to be treated as odd e.g. HydroBASINS 
    (https://www.hydrosheds.org/products/hydrobasins).
    
    Parameters
    ----------
    a : int, scalar
        A number with only digits
        
    b : int, scalar
        A number with only digits
    
    oddOrZero : bool, optional
        If set to True zero is odd as well (default is False)
    """ 
    
    result = updwn(a, b, upstream = True, oddOrZero=oddOrZero)
    
    return(result)

def downstream(a,b,oddOrZero=False):
    """Checks if b is downstream of a.
    
    The argument 'oddOrZero' can be set to True if the Pfafstetter code is 
    modified and uses Zeros that need to be treated as odd e.g. HydroBASINS 
    (https://www.hydrosheds.org/products/hydrobasins).
    
    Parameters
    ----------
    a : int, scalar
        A number with only digits
        
    b : int, scalar
        A number with only digits
    
    oddOrZero : bool, optional
        If set to True zero is odd as well (default is False)
    """ 
    
    result = updwn(a, b, upstream = False, oddOrZero=oddOrZero)
    
    return(result)

def updwn(a, b, upstream = True, oddOrZero = False):
    """Checks if b is upstream or downstream of a.
    
    If 'upstream' is True it checks upstream, if False downstream.
    
    The argument 'oddOrZero' can be set to True if the Pfafstetter code is 
    modified and uses Zeros that need to be treated as odd e.g. HydroBASINS 
    (https://www.hydrosheds.org/products/hydrobasins).
    
    Parameters
    ----------
    a : int, scalar
        A number with only digits
        
    b : int, scalar
        A number with only digits
        
    upstream : bool, optional
        If set to True it checks upstream (default is True)
    
    oddOrZero : bool, optional
        If set to True zero is odd as well (default is False)
    """ 
    ## check input
    try:
        int(a)
        int(b)
    except:
        raise Exception('a and b must only contain digits.')
    
    ## need to be string
    A = str(a)
    B = str(b)
    
    ## number of characters
    nCharA = len(A)
    nCharB = len(B)
    
    ## compare levels if one is larger
    if (nCharB > nCharA):
        print("Warning: Higher level A is compared to lower level B. Turnicate B to same as A.")
        
        B = B[:nCharA]
        nCharB = nCharA
        
    elif (nCharA > nCharB):
        print('Warning: Lower level A is compared to higher level B. Turnicate A to same as B.')
        
        A = A[:nCharB]
        nCharA = nCharB
    
    ## return True if both are the same
    if (A == B): return(True)
    
    ## this shortens the number of tests {}
    if upstream:
        ## Greater
        cond02 = int(A) > int(B)
        
        if not cond02:
            ## exit with False
            return(False)
        
    else:
        ## is less?
        cond02 = int(A) < int(B)
        
        if not cond02:
            return(False)
        
    ## Core from Verdin & Verdin 1999, p. 10
    ## get number of matching digits from start
    for i in range(1,nCharA):
        leadA = A[0:i]
        if not B.startswith(leadA):
            break

    ## get trailing digits
    trailA = A[i-1:]
    trailB = B[i-1:]
        
    ## all odd (or zero)
    if upstream:
        cond01 = allodd(trailB, oddOrZero=oddOrZero)
    else:
        cond01 = allodd(trailA, oddOrZero=oddOrZero)
    
    return(cond01)
    
    