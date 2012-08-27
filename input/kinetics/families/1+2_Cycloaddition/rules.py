#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 576,
    label = "elec_def;multiplebond",
    group1 = "OR{carbene, me_carbene, dime_carbene, ph_carbene, o_atom}",
    group2 = 
"""
1 *1 {Cd,CO} 0 {2,D}
2 *2 {Cd,O}  0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (1e+12,"cm^3/(mol*s)"),
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

