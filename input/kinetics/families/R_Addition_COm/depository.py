#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/depository"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
1 *2 C 1
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S}
2 *1 C 1 {1,S} {3,D}
3    O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.06,"m^3/(mol*s)","*|/",3),
        n = 1.89,
        Ea = (20.167,"kJ/mol","+|-",8.368),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
Methyl (doublet): external symmetry number (EXTSYM) = 6
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
CH3CO (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Sep  5 15:27:52 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

