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

def upstream(a, b, oddOrZero=False, includeEqual=True):
    """Checks if b is upstream of a
    
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

    includeEqual : bool, optional
        If set to True equal codes return True (default is True).
    """ 
    
    result = updwn(a, b, upstream=True, oddOrZero=oddOrZero, includeEqual=includeEqual)
    
    return result

def downstream(a,b,oddOrZero=False,includeEqual=True):
    """Checks if b is downstream of a
    
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

    includeEqual : bool, optional
        If set to True equal codes return True (default is True).
    """ 
    
    result = updwn(a, b, upstream=False, oddOrZero=oddOrZero, includeEqual=includeEqual)
    
    return result

def updwn(a, b, upstream = True, oddOrZero = False, includeEqual = True):
    """Checks if b is upstream of a
    
    If 'upstream' is True it checks if b is downstream of a
    
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

    includeEqual : bool, optional
        If set to True equal codes return True (default is True).
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
        print("Warning: Higher level B is compared to lower level A. Trim B to same as A.")
        
        B = B[:nCharA]
        nCharB = nCharA
        
    elif (nCharA > nCharB):
        print('Warning: Lower level B is compared to higher level A. Trim A to same as B.')
        
        A = A[:nCharB]
        nCharA = nCharB
    
    ## return True if both are the same and includeEqual option is True
    if (A == B):
        if includeEqual:
            return(True)
        else:
            return(False)

    # This shortens the test for check downstream case
    if not upstream:
        # higher digits always denote upstream segments
        if b > a:
            return False
        
    ## Core from Verdin & Verdin 1999, p. 10
    ## get number of matching digits from start
    for n in range(1,nCharA+1):
        leadA = A[0:n]
        if not B.startswith(leadA):
            break

    # get trailing digits
    trailA = A[n-1:]
    trailB = B[n-1:]

    if upstream:
        # B is upstream of A, if B has higher digits than A
        # At each level, higher digits denote upstream segments
        # Greater
        cond01 = int(trailB) > int(trailA)

        # cond02 needed?
        cond02 = allodd(trailA, oddOrZero=oddOrZero)

        return cond01 and cond02 #only necessary for wikipedia example

    else: # downstream
        # Therefore, given a point with code A on the water system, a point with code B is downstream if:
        # less than the remaining digits of A?
        cond01 = int(trailB) < int(trailA)

        # all odd.
        cond02 = allodd(trailB, oddOrZero=oddOrZero)

        return cond01 and cond02
    
    