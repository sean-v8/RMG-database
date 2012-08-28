#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 480,
    label = "Rn;Y_rad_out;Ypri_rad_out",
    group1 = "OR{R3, R4, R5, R6}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *2 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (5e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (30,"kcal/mol"),
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

