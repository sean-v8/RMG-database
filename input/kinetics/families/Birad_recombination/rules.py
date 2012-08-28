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

entry(
    index = 486,
    label = "R6_SSSSS;C_rad_out_2H;Cpri_rad_out_2H",
    group1 = 
"""
1 *1 {Cs,Cd,CO,Os} 1 {2,S}
2 *3 {Cs,Cd,CO,Os} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os} 0 {2,S} {4,S}
4    {Cs,Cd,CO,Os} 0 {3,S} {5,S}
5 *4 {Cs,Cd,CO,Os} 0 {4,S} {6,S}
6 *2 {Cs,Cd,CO,Os} 1 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    H 0 {1,S}
""",
    group3 = 
"""
1 *2 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.21e+10,"s^-1"),
        n = 0.137,
        alpha = 0,
        E0 = (2.12,"kcal/mol"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2CH2. -> cyclohexane (k5-1+k5-2 in Scheme 7/Table 10) (includes formation of both boat and chair conformations)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant; the rate constant added here was found my performing least squares fit for log(ktot) from 600-2000 K (where ktot is the sum of k5-1 and k5-2)

Note: Recent experimental/RRKM study by Kiefer, Gupte, Harding, and Klippenstein (http://www.combustion.org.uk/ECM_2009/P810069.pdf) (stated uncertainty is +/- 30%) appears to agree with Sirjean et al. results, but they only report forward rate constant
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

