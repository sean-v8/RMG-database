#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/depository"
shortDesc = u""
longDesc = u"""

"""
recommended = False


entry(
    index = 1,
    reactant1 = 
"""
1 *1 O 1 {2,S}
2 *4 O 0 {1,S} {3,S}
3 *5 C 0 {2,S} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *5 C 0 {1,S} {5,S}
3 *3 C 1 {1,S}
4 *1 O 0 {1,S} {5,S}
5 *4 O 0 {2,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.724e+10,"s^-1","*|/",3),
        n = 0.478,
        Ea = (122.04,"kJ/mol","+|-",8.368),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
u"""
Previous RMG estimate for this reaction was an "Average of average" estimate. This reaction was of interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO. The high-P limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)

TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable hindered rotor was accurate)

Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one. The k(T) was calculated from 600-2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:

k(T) = 2.724e+10 * (T/1K)^0.478 * exp(-29.169 kcal/mol / RT) cm3/mol/s.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Sep  5 13:38:20 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

