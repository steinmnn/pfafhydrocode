#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A couple of tests.

Created on Thu Oct 27 11:13:32 2022

@author: vincent
"""

import unittest
from pfafhydrocode import odd, allodd, updwn, upstream, downstream

class TestPfafhydrocode(unittest.TestCase):
    
    ## odd() function
    def test_odd_with_odd_number_one(var):
        var.assertTrue(odd(1), "1: should be True.")
        
    def test_odd_with_odd_number_five(var):
        var.assertTrue(odd(5), "5: should be True.")
        
    def test_odd_with_even_number_eight(var):
        var.assertFalse(odd(8), "8: should be False.")
        
    def test_odd_with_zero(var):
        var.assertFalse(odd(0), "0: should be False.")
        
    def test_odd_with_zero_and_oddOrZero_True(var):
        var.assertTrue(odd(0, oddOrZero=True), "0: with oddOrZero=True should be True.")
        
    ## allodd() function
    def test_allodd_with_odd_numbers(var):
        var.assertTrue(allodd('13579'),'Should be True as 13579 are all odd.')
        
    def test_allodd_with_odd_numbers_int_input(var):
        var.assertTrue(allodd(13579),'Should be True as 13579 are all odd.')
        
    def test_allodd_with_oddOrZero_True_odd_numbers(var):
        var.assertTrue(allodd('013579', oddOrZero=True),'Should be True as 013579 are all odd.')
    
    ## updwn() function
    def test_updwn_with_same_number(var):
        var.assertTrue(updwn(1994,1994),'Comparing same_number_should give True.')
        
    def test_updwn_with_a_greater_as_b(var):
        var.assertFalse(updwn(1995,1884),"Should be False. Greater A can't be downstream of B.")
        
    def test_updwn_with_a_less_than_b_and_upstream_false(var):
        var.assertFalse(updwn(1884,1995,upstream=False),"Should be False. Greater B can't be downstream of A if tested on downstream.")
        
    def test_updwn_upstream_with_single_number_from_wiki(var):
        var.assertTrue(updwn(8835,8833),'Should be True. As 8835 is upstream of 8833.')
        
    def test_updwn_downstream_with_single_number_from_wiki(var):
        var.assertFalse(updwn(8835,8821),'Should be False. As 8835 is not upstream of 8821.')
        
    def test_updwn_with_whole_wiki_example(var):
        dwn = [8833, 8811, 8832, 8821, 9135]
        var.assertEqual([updwn(8835,x) for x in dwn], [True, True, False, False, False], 'Should be equal. See wikipedia example.')
        
    def test_updwn_with_single_hydrobasins_PFAF12(var):
        var.assertTrue(updwn(232670911100,232670700000,oddOrZero=True), 'Should be True as 232670911100 is upstream from 232670700000.')
        
    def test_updwn_with_single_hydrobasins_PFAF12_downstream(var):
        var.assertFalse(updwn(232670911100,232670700000,upstream=False,oddOrZero=True), 'Should be False as 232670911100 is upstream from 232670700000.')
    
    def test_updwn_with_single_hydrobasins_PFAF12_far_apart(var):
        var.assertTrue(updwn(232670942000,232670700000,oddOrZero=True), 'Should be True as 232670911100 is upstream from 232670700000.')
        
    ## upstream() function
    def test_upstream_with_characters(var):
        with var.assertRaises(Exception):
            upstream('2326709420ab','232670700000',oddOrZero=True)
            
    def test_upstream_with_hybas_example_pfaf12(var):
        var.assertTrue(upstream(232630300200,232630300300,oddOrZero=True),'Should be True as learned from QGIS project (Pfafstetter level 12).')
        
    def test_upstream_with_hybas_example_pfaf08(var):
        var.assertTrue(upstream(23263030,23263030,oddOrZero=True),'Should be True as learned from QGIS project (Pfafstetter level 8.')
        
    def test_upstream_with_different_levels(var):
        a = str(232630300200)
        b = str(232630300300)
        results = []
        for i in range(len(b)):
            results.append(upstream(a,b[:i+1],oddOrZero=True))
            
        var.assertEqual(results, [True for i in range(len(b))],'Should all be True, as we learned from the QGIS project.')
    
    ## downstream() function
    def test_downstream_with_characters(var):
        with var.assertRaises(Exception):
            downstream('2326709420ab','2326707000bb',oddOrZero=True)
        
if __name__ == "__main__":
    unittest.main()