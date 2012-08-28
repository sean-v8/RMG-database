#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 589,
    label = "diene_out;diene_in;ene",
    group1 = "OR{diene_unsub_unsub_out, diene_unsub_monosub_out, diene_unsub_disub_out, diene_monosub_monosub_out, diene_monosub_disub_out, diene_disub_disub_out}",
    group2 = 
"""
1 *4 Cd 0 {2,S}
2 *5 Cd 0 {1,S}
""",
    group3 = 
"""
1 *1 Cd 0 {2,D}
2 *2 Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (5e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

