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
    def test_updwn_with_characters(var):
        with var.assertRaises(Exception):
            upstream('2326709420ab','232670700000')

    def test_updwn_with_same_number(var):
        var.assertTrue(updwn(1994,1994),'Comparing same_number_should give True.')

    def test_updwn_with_different_code_length_b_longer(var):
        var.assertTrue(updwn(1994, 1994123), '1994123 (B) is trimmed to 1994. Same number should give True.')

    def test_updwn_with_different_code_length_a_longer(var):
        var.assertTrue(updwn(1994456, 1994), '1994456 (A) is trimmed to 1994. Same number should give True.')

    def test_updwn_with_same_number_exclude_equal(var):
        var.assertFalse(updwn(1994, 1994, includeEqual=False), 'Comparing same_number_should give False when includeEqual is set False.')
        
    def test_updwn_with_a_greater_as_b(var):
        var.assertFalse(updwn(1995,1884),"Should be False. 1884 (B) is not upstream of 1995 (A). Higher always denote upstream segments.")
        
    def test_updwn_with_a_less_than_b_and_upstream_false(var):
        var.assertFalse(updwn(1884,1995,upstream=False),"Should be False. 1995 (B) is not downstream of 1884 (A). Higher always denote upstream segments.")
        
    def test_updwn_upstream_with_wikipedia_example_single_number(var):
        var.assertTrue(updwn(8833,8835),'Should be True. 8835 (B) is upstream of 8833 (A). See wikipedia example.')
        
    def test_updwn_downstream_with_wikipedia_example_single_number(var):
        var.assertFalse(updwn(8821,8835),'Should be False. 8835 (B) is not upstream of 8821 (A). See wikipedia example.')
        
    def test_updwn_with_wikipedia_example_all_numbers(var):
        as_ = [8833, 8811, 8832, 8821, 9135]
        var.assertEqual([updwn(a,8835) for a in as_], [True, True, False, False, False], 'Should be equal. See wikipedia example.')
        
    ## upstream() function

    def test_upstream_with_hybas_example_pfaf12(var):
        var.assertTrue(upstream(232630300200,232630300300,oddOrZero=True),'Should be True as learned from QGIS project.')

    def test_upstream_with_different_levels(var):
        a = str(232630300200)
        b = str(232630300300)
        results = []
        for i in range(len(b)):
            results.append(upstream(a,b[:i+1],oddOrZero=True))

        var.assertEqual(results, [True for i in range(len(b))],'Should all be True as we learned from the QGIS project.')

    def test_upstream_with_lev5_example_array_nmizukami(var):
        a = 23267
        bs = [23261, 23262, 23263, 23264, 23265, 23267, 23266, 23268, 23269]
        rightresult = [False, False, False, False, False, False, False, True, True]

        var.assertEqual(rightresult, [upstream(a,b,includeEqual=False) for b in bs],'Should be equal. Like result from nmizukami/pfaf_decode')

    def test_upstream_with_lev5_example_nmizukami_single(var):
        var.assertTrue(upstream(23267,23268,includeEqual=False),'23268 (B) is upstream of 23267 (A)')

    ## downstream() function
    def test_downstream_with_characters(var):
        with var.assertRaises(Exception):
            downstream('2326709420ab','2326707000bb',oddOrZero=True)

    def test_downstream_with_lev12_example_from_qgis_1(var):
        var.assertTrue(downstream('216029033500','216029010320'), 'Should be True. As learned from QGIS example.')

    def test_downstream_with_lev12_example_from_qgis_2(var):
        var.assertTrue(downstream('216029033500','216029033400'), 'Should be True. As learned from QGIS example.')
        
if __name__ == "__main__":
    unittest.main()