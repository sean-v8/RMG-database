#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 6000,
    label = "db_2H;mb_OC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 Od 0 {2,D}
2 *4 CO 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (2.33e+06,"cm^3/(mol*s)","*|/",5),
        n = 1.65,
        alpha = 0,
        E0 = (54.15,"kcal/mol"),
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

