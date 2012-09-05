#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
recommended = True

entry(
    index = 807,
    label = "Rn;multiplebond_intra;radadd_intra",
    group1 = "OR{R4, R5, R6, R7}",
    group2 = 
"""
1 *2 {Cd,Ct,CO} 0 {2,{D,T}}
2 *3 {Cd,Ct,Od} 0 {1,{D,T}}
""",
    group3 = 
"""
1 *1 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
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
    index = 808,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 Cd  0 {5,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (6.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 809,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHDe",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Cd  0 {2,S} {4,D}
4 *3 Cd  0 {3,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs            1 {2,S} {3,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (25.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 810,
    label = "R6_SMS_D;doublebond_intra;radadd_intra_cs",
    group1 = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 Cd         0 {5,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D}
2 *3 Cd 0 {1,D}
""",
    group3 = 
"""
1 *1 Cs 1
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (46.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 811,
    label = "R6_SSM_D;doublebond_intra;radadd_intra_cs",
    group1 = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 Cd         0 {5,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D}
2 *3 Cd 0 {1,D}
""",
    group3 = 
"""
1 *1 Cs 1
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (46.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 812,
    label = "R5_SD_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 Cd  0 {4,D}
""",
    group2 = 
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    H      0 {1,S}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    group3 = 
"""
1 *1 Cs     1 {2,S} {3,S}
2    H      0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (46.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

