#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = u""
longDesc = u"""
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
recommended = True

entry(
    index = 416,
    label = "COm;Y_rad",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 R 1
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 423,
    label = "COm;O_rad/NonDe",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 O      1 {2,S}
2    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.41e+07,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Wang et al. [105].""",
    longDesc = 
u"""
[105] Wang, B.; Hou, H.; Gu, Y. Phys. Chem. A 1999, 103, 8021.
RRK(M) extrapolation. CH3O + CO --> CH3OCO, 250K and 2500K

Data stored in RMG appears to be linear fit of the following data, presented on pg.8028

in the right-hand column under the section heading "3.Implications for Atmospheric
and Combustion Chemistry.": (250K, 5torr, 1.39x10^-19 cm3/molecule/s) and 
(2500K, 760torr, 3.10x10^-17 cm3/molecule/s).
Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results

in "y = -1.502x - 37.412" with an R^2 value of 1.  The A and Ea values calculated
by MRH are thus: A=3.40x10^7 cm3/mol/s, Ea=2.98 kcal/mol, in agreement w/database.
MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 424,
    label = "COm;C_methyl",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.06e+06,"cm^3/(mol*s)","*|/",3),
        n = 1.89,
        alpha = 0,
        E0 = (4.82,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3 + CO = CH3CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

Methyl (doublet): external symmetry number (EXTSYM) = 6
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
CH3CO (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 425,
    label = "COm;CH2CH3",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (7.7e+07,"cm^3/(mol*s)","*|/",3),
        n = 1.37,
        alpha = 0,
        E0 = (5.69,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2 + CO = CH3CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

Ethyl (doublet): external symmetry number (EXTSYM) = 1, one hindered rotor (methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
CH3CH2CO (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 426,
    label = "COm;CH2CH2CH3",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     H 0 {4,S}
7     C 0 {4,S} {8,S} {9,S} {10,S}
8     H 0 {7,S}
9     H 0 {7,S}
10    H 0 {7,S}
""",
    kinetics = ArrheniusEP(
        A = (6.51e+10,"cm^3/(mol*s)","*|/",3),
        n = 0.45,
        alpha = 0,
        E0 = (6.68,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2CH2 + CO = CH3CH2CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

n-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 4)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 2; propyl group, symmetry = 1)
CH3CH2CH2CO (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "COm;CH[CH3]2",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     C 0 {1,S} {5,S} {6,S} {7,S}
4     C 0 {1,S} {8,S} {9,S} {10,S}
5     H 0 {3,S}
6     H 0 {3,S}
7     H 0 {3,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (8.61e+07,"cm^3/(mol*s)","*|/",3),
        n = 1.36,
        alpha = 0,
        E0 = (4.8,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CHCH3 + CO = CH3CH(CO)CH3
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

iso-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 6; methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
CH3CH(CO)CH3 (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

