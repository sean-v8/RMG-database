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

entry(
    index = 2,
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 1 {1,S} {4,D}
4    O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (77,"m^3/(mol*s)","*|/",3),
        n = 1.37,
        Ea = (23.807,"kJ/mol","+|-",8.368),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
Ethyl (doublet): external symmetry number (EXTSYM) = 1, one hindered rotor (methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
CH3CH2CO (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Sep  5 15:31:37 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 1 {2,S} {5,D}
5    O 0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (65100,"m^3/(mol*s)","*|/",3),
        n = 0.45,
        Ea = (27.949,"kJ/mol","+|-",8.368),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
n-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 4)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 2; propyl group, symmetry = 1)
CH3CH2CH2CO (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Sep  5 15:37:23 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 1 {1,S} {2,S}
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *1 C 1 {1,S} {5,D}
5    O 0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (86.1,"m^3/(mol*s)","*|/",3),
        n = 1.36,
        Ea = (20.083,"kJ/mol","+|-",8.368),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
iso-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 6; methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
CH3CH(CO)CH3 (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Sep  5 15:37:23 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

