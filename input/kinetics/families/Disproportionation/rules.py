#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 485,
    label = "Y_rad_birad;XH_Rrad",
    group1 = "OR{Y_1centerbirad, Y_rad}",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 487,
    label = "O2_birad;Cmethyl_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.23e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (15.99,"kcal/mol"),
        Tmin = (700,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'sp') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 501,
    label = "O2_birad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.5825e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (14.85,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (900,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'ss') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 20001,
    label = "O2_birad;XH_Rrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
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

