#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["X_H_or_Xrad_H", "Y_rad_birad"], products=["X_H_or_Xrad_H", "Y_rad_birad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_H_or_Xrad_H",
    group = "OR{X_H, Xrad_H}",
    kinetics = Arrhenius(
        A = (0.25603,"m^3/(mol*s)"),
        n = 2.06549,
        Ea = (43560.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad",
    group = "OR{Y_1centerbirad, Y_rad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "Xrad_H",
    group = 
"""
1 *1 R 1 {2,S}
2 *2 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "X_H",
    group = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.00052,"m^3/(mol*s)"),
        n = 0.00114559,
        Ea = (0.954091,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (51107.2,"m^3/(mol*s)"),
        n = -1.39207,
        Ea = (25287.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "Ct_H",
    group = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (162394,"m^3/(mol*s)"),
        n = -1.14937,
        Ea = (81550.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.28748e-05,"m^3/(mol*s)"),
        n = 1.30699,
        Ea = (-23149.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "O_pri",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0206701,"m^3/(mol*s)"),
        n = 0.452549,
        Ea = (40150.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O_sec",
    group = 
"""
1 *1 O   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.70057e-06,"m^3/(mol*s)"),
        n = 1.42363,
        Ea = (-31790.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.12085,"m^3/(mol*s)"),
        n = 0.135976,
        Ea = (-9639.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "O/H/NonDeO",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (3.75314e-07,"m^3/(mol*s)"),
        n = 1.73513,
        Ea = (-37336.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "H2O2",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (7.89587e-05,"m^3/(mol*s)"),
        n = 1.02754,
        Ea = (-29372.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "ROOH_pri",
    group = 
"""
1    C  0 {2,S} {4,S} {5,S} {6,S}
2    O  0 {1,S} {3,S}
3 *1 O  0 {2,S} {7,S}
4    Cs 0 {1,S}
5    H  0 {1,S}
6    H  0 {1,S}
7 *2 H  0 {3,S}
""",
    kinetics = Arrhenius(
        A = (1.31162e-13,"m^3/(mol*s)"),
        n = 3.70181,
        Ea = (-59473.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "ROOH_sec",
    group = 
"""
1    C  0 {2,S} {4,S} {5,S} {6,S}
2    O  0 {1,S} {3,S}
3 *1 O  0 {2,S} {7,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    H  0 {1,S}
7 *2 H  0 {3,S}
""",
    kinetics = Arrhenius(
        A = (1.31162e-13,"m^3/(mol*s)"),
        n = 3.70181,
        Ea = (-59473.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "ROOH_ter",
    group = 
"""
1    C  0 {2,S} {4,S} {5,S} {6,S}
2    O  0 {1,S} {3,S}
3 *1 O  0 {2,S} {7,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    Cs 0 {1,S}
7 *2 H  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "O/H/OneDe",
    group = 
"""
1 *1 O             0 {2,S} {3,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (51.9995,"m^3/(mol*s)"),
        n = -0.401243,
        Ea = (4435.61,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "Orad_O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 1 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.109e+06,"m^3/(mol*s)"),
        n = -2.36604,
        Ea = (-52921.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "Cd_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (75673.5,"m^3/(mol*s)"),
        n = -1.2158,
        Ea = (41893.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "Cd_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (870328,"m^3/(mol*s)"),
        n = -1.51397,
        Ea = (52985.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "Cd_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    C   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (623.281,"m^3/(mol*s)"),
        n = -0.629905,
        Ea = (20100.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (27.7716,"m^3/(mol*s)"),
        n = -0.328534,
        Ea = (25308,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (7156.73,"m^3/(mol*s)"),
        n = -0.742218,
        Ea = (10677.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 C             0 {2,D} {3,S} {4,S}
2    C             0 {1,D}
3 *2 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (209016,"m^3/(mol*s)"),
        n = -1.21393,
        Ea = (11255.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "Cb_H",
    group = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (185059,"m^3/(mol*s)"),
        n = -1.48235,
        Ea = (32831.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "CO_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (6.36113,"m^3/(mol*s)"),
        n = -0.328886,
        Ea = (-14496.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "CO_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.60569,"m^3/(mol*s)"),
        n = -0.304517,
        Ea = (-11153.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "CO_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    O   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (9.35054,"m^3/(mol*s)"),
        n = -0.357957,
        Ea = (-18484.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "CO/H/NonDe",
    group = 
"""
1 *1 C      0 {2,D} {3,S} {4,S}
2    O      0 {1,D}
3 *2 H      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (9.35054,"m^3/(mol*s)"),
        n = -0.357957,
        Ea = (-18484.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 28,
    label = "InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *1 C 0 {2,S} {12,D} {13,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    O 0 {4,D}
13 *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (1.21039e-08,"m^3/(mol*s)"),
        n = 1.88396,
        Ea = (-35829.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "CO/H/OneDe",
    group = 
"""
1 *1 C             0 {2,D} {3,S} {4,S}
2    O             0 {1,D}
3 *2 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Cs_H",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
5    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.11882,"m^3/(mol*s)"),
        n = 0.00629731,
        Ea = (-1922.83,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_methane",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (125.323,"m^3/(mol*s)"),
        n = -0.482537,
        Ea = (18023.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C_pri",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0547055,"m^3/(mol*s)"),
        n = 0.379817,
        Ea = (-3470.76,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 33,
    label = "C/H3/Cs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0797369,"m^3/(mol*s)"),
        n = 0.395825,
        Ea = (2460.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "InChI=1/C2H6/c1-2/h1-2H3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (8.65957e-08,"m^3/(mol*s)"),
        n = 2.24975,
        Ea = (-12947.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3  *1 C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *2 H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (2.12918e-09,"m^3/(mol*s)"),
        n = 2.47479,
        Ea = (-13516.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 36,
    label = "C/H3/Cd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0127829,"m^3/(mol*s)"),
        n = 0.512822,
        Ea = (-5284.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 37,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3",
    group = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (1.36537e-07,"m^3/(mol*s)"),
        n = 1.89218,
        Ea = (-21473.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3",
    group = 
"""
1  *1 C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {2,S} {4,D}
4     C 0 {3,D} {11,S} {12,S}
5  *2 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (9.98324e-08,"m^3/(mol*s)"),
        n = 1.96353,
        Ea = (-18041.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+",
    group = 
"""
1  *1 C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,D} {11,S}
4     C 0 {2,S} {3,D} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (3.66495e-08,"m^3/(mol*s)"),
        n = 2.28396,
        Ea = (1700.79,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "C/H3/Ct",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (81997.2,"m^3/(mol*s)"),
        n = -1.09511,
        Ea = (-50.4065,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "C/H3/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.2107e+06,"m^3/(mol*s)"),
        n = -1.92792,
        Ea = (13825.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C/H3/CO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    CO 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00854242,"m^3/(mol*s)"),
        n = 0.698886,
        Ea = (-30881.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 43,
    label = "C/H3/O",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.06225e-05,"m^3/(mol*s)"),
        n = 1.66634,
        Ea = (-23702.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 44,
    label = "C_sec",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0728885,"m^3/(mol*s)"),
        n = 0.329884,
        Ea = (-5492.28,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 45,
    label = "C/H2/NonDeC",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.7151,"m^3/(mol*s)"),
        n = -0.176275,
        Ea = (3891.67,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 46,
    label = "InChI=1/C3H8/c1-3-2/h3H2,1-2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (2.34118e-09,"m^3/(mol*s)"),
        n = 2.39756,
        Ea = (-13659.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 47,
    label = "C/H2/NonDeO",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    H      0 {1,S}
4    O      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.51669e-07,"m^3/(mol*s)"),
        n = 1.81436,
        Ea = (-17237.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 48,
    label = "C/H2/CsO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.51669e-07,"m^3/(mol*s)"),
        n = 1.81436,
        Ea = (-17237.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 49,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2  *1 C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6     H 0 {1,S}
7  *2 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (1.51669e-07,"m^3/(mol*s)"),
        n = 1.81436,
        Ea = (-17237.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 50,
    label = "C/H2/O2",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C/H2/OneDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00414781,"m^3/(mol*s)"),
        n = 0.73061,
        Ea = (-13302.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 52,
    label = "C/H2/OneDeC",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00414781,"m^3/(mol*s)"),
        n = 0.73061,
        Ea = (-13302.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 53,
    label = "InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,D} {10,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     O 0 {3,D}
10    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (3.62749e-07,"m^3/(mol*s)"),
        n = 1.52609,
        Ea = (-24162.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 54,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5  *2 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (2.00615e-07,"m^3/(mol*s)"),
        n = 1.9755,
        Ea = (-7690.44,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 55,
    label = "C/H2/OneDeO",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C/H2/TwoDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cd,Ct,CO,Cb} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (114857,"m^3/(mol*s)"),
        n = -1.12045,
        Ea = (-20081.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 57,
    label = "C/H2/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (907299,"m^3/(mol*s)"),
        n = -1.94581,
        Ea = (10593.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 58,
    label = "C_ter",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (288.499,"m^3/(mol*s)"),
        n = -0.698872,
        Ea = (-2865.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 59,
    label = "C/H/NonDeC",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (89.0418,"m^3/(mol*s)"),
        n = -0.570064,
        Ea = (-595.761,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 60,
    label = "C/H/Cs3",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (89.0418,"m^3/(mol*s)"),
        n = -0.570064,
        Ea = (-595.761,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 61,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6  *2 H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (4.63131e-07,"m^3/(mol*s)"),
        n = 1.69063,
        Ea = (-16315.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 62,
    label = "C/H/NDMustO",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "C/H/OneDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2446.9,"m^3/(mol*s)"),
        n = -0.760659,
        Ea = (-22683.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 64,
    label = "C/H/Cs2",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2446.9,"m^3/(mol*s)"),
        n = -0.760659,
        Ea = (-22683.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 65,
    label = "InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,D} {13,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    O 0 {4,D}
13    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (15.394,"m^3/(mol*s)"),
        n = -0.132218,
        Ea = (-25556.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 66,
    label = "C/H/ODMustO",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "C/H/TwoDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.13886e+07,"m^3/(mol*s)"),
        n = -1.86978,
        Ea = (-15522.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "C/H/Cs",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.13886e+07,"m^3/(mol*s)"),
        n = -1.86978,
        Ea = (-15522.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 69,
    label = "C/H/TDMustO",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "C/H/ThreeDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "C/H/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (907299,"m^3/(mol*s)"),
        n = -1.94581,
        Ea = (10593.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 72,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 {Cs,Cd,O} 2T
""",
    kinetics = Arrhenius(
        A = (36.4836,"m^3/(mol*s)"),
        n = -0.329449,
        Ea = (-22556.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 73,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O 2T
""",
    kinetics = Arrhenius(
        A = (82.2952,"m^3/(mol*s)"),
        n = -0.286589,
        Ea = (-24355.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 74,
    label = "CH2_triplet",
    group = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = Arrhenius(
        A = (3.44823,"m^3/(mol*s)"),
        n = -0.453742,
        Ea = (-17337.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 75,
    label = "Y_rad",
    group = 
"""
1 *3 R 1
""",
    kinetics = Arrhenius(
        A = (0.862798,"m^3/(mol*s)"),
        n = 0.0169472,
        Ea = (937.585,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 76,
    label = "H_rad",
    group = 
"""
1 *3 H 1
""",
    kinetics = Arrhenius(
        A = (170.355,"m^3/(mol*s)"),
        n = -0.296774,
        Ea = (-16916.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 77,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 {Ct,Os} 1 {2,{S,T}}
2    {Ct,Os} 1 {1,{S,T}}
""",
    kinetics = Arrhenius(
        A = (2.65116e+06,"m^3/(mol*s)"),
        n = -1.74801,
        Ea = (156092,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 78,
    label = "O2b",
    group = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.53031e+06,"m^3/(mol*s)"),
        n = -1.74006,
        Ea = (164063,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 79,
    label = "C2b",
    group = 
"""
1 *3 C 1 {2,T}
2    C 1 {1,T}
""",
    kinetics = Arrhenius(
        A = (8.51171e+06,"m^3/(mol*s)"),
        n = -1.94672,
        Ea = (-43192.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 80,
    label = "Ct_rad",
    group = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = Arrhenius(
        A = (1.91406e+06,"m^3/(mol*s)"),
        n = -2.00311,
        Ea = (-44047.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 81,
    label = "O_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.039899,"m^3/(mol*s)"),
        n = 0.367791,
        Ea = (-19264.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 82,
    label = "O_pri_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.6514,"m^3/(mol*s)"),
        n = 0.027742,
        Ea = (-40728.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 83,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00362724,"m^3/(mol*s)"),
        n = 0.586805,
        Ea = (-5439.43,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 84,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0393682,"m^3/(mol*s)"),
        n = 0.229866,
        Ea = (-26761.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 85,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {6,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 {1,S}
6  *3 O 1 {3,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (1.19309e-05,"m^3/(mol*s)"),
        n = 1.50513,
        Ea = (-31486.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 86,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00712266,"m^3/(mol*s)"),
        n = 0.531185,
        Ea = (2058.49,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 87,
    label = "OOCH3",
    group = 
"""
1    O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3    C 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (3.37056e-05,"m^3/(mol*s)"),
        n = 1.37162,
        Ea = (-131.863,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 88,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O             1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.13694e-07,"m^3/(mol*s)"),
        n = 1.75216,
        Ea = (18007.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 89,
    label = "InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3",
    group = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,S}
3    C 0 {1,D} {5,S}
4    C 0 {2,S}
5 *3 O 1 {3,S}
""",
    kinetics = Arrhenius(
        A = (0.000391596,"m^3/(mol*s)"),
        n = 0.768768,
        Ea = (22278.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 90,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o",
    group = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8 *3 O 1 {3,S}
9    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (1.4205e-11,"m^3/(mol*s)"),
        n = 3.22724,
        Ea = (11601.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 91,
    label = "Cd_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.702741,"m^3/(mol*s)"),
        n = 0.0223636,
        Ea = (-21076.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 92,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.3347,"m^3/(mol*s)"),
        n = 0.137481,
        Ea = (-24357.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 93,
    label = "InChI=1/C2H3/c1-2/h1H,2H2",
    group = 
"""
1    C 0 {2,D} {3,S} {4,S}
2 *3 C 1 {1,D} {5,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.0927e-05,"m^3/(mol*s)"),
        n = 1.28464,
        Ea = (-37739.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {4,D} {10,S}
4  *3 C 1 {3,D} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (0.0112045,"m^3/(mol*s)"),
        n = 0.538768,
        Ea = (-54582,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 95,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    C   0 {1,D}
3    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.72738,"m^3/(mol*s)"),
        n = -0.117216,
        Ea = (-17098,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0333415,"m^3/(mol*s)"),
        n = 0.366945,
        Ea = (-27127.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 97,
    label = "InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 {3,D} {7,S} {8,S}
3 *3 C 1 {1,S} {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (9.87335e-07,"m^3/(mol*s)"),
        n = 1.68925,
        Ea = (-28036.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 98,
    label = "InChI=1/C4H7/c1-3-4-2/h3H,1-2H3",
    group = 
"""
1     C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,D} {11,S}
4  *3 C 1 {2,S} {3,D}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (0.00490195,"m^3/(mol*s)"),
        n = 0.608768,
        Ea = (-40147.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 99,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 C             1 {2,D} {3,S}
2    C             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.38853e+06,"m^3/(mol*s)"),
        n = -1.78488,
        Ea = (17447.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 101,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = Arrhenius(
        A = (4159.9,"m^3/(mol*s)"),
        n = -1.36775,
        Ea = (-20461.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 102,
    label = "CO_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.140297,"m^3/(mol*s)"),
        n = 0.329522,
        Ea = (20611.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 103,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.572492,"m^3/(mol*s)"),
        n = 0.226831,
        Ea = (32956.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 104,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0529958,"m^3/(mol*s)"),
        n = 0.400616,
        Ea = (12064.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 105,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C      1 {2,D} {3,S}
2    O      0 {1,D}
3    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0529958,"m^3/(mol*s)"),
        n = 0.400616,
        Ea = (12064.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 106,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C             1 {2,D} {3,S}
2    O             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "Cs_rad",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.131719,"m^3/(mol*s)"),
        n = 0.196009,
        Ea = (111.454,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 108,
    label = "C_methyl",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (12440,"m^3/(mol*s)"),
        n = -0.995807,
        Ea = (4789.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 109,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00125739,"m^3/(mol*s)"),
        n = 0.745734,
        Ea = (-2006.06,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 110,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.08478e-05,"m^3/(mol*s)"),
        n = 1.11022,
        Ea = (-12432.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 111,
    label = "InChI=1/C2H5/c1-2/h1H2,2H3",
    group = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 {1,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.03324e-09,"m^3/(mol*s)"),
        n = 2.45169,
        Ea = (-18121.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 112,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {3,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.0322689,"m^3/(mol*s)"),
        n = 0.178768,
        Ea = (-20147.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 113,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {5,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.00342296,"m^3/(mol*s)"),
        n = 0.548768,
        Ea = (-16926,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 114,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.0644257,"m^3/(mol*s)"),
        n = -0.041232,
        Ea = (-21361,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 115,
    label = "InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {1,S} {12,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.00235294,"m^3/(mol*s)"),
        n = 0.548768,
        Ea = (-16758.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 116,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {1,S} {12,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (3.84747e-09,"m^3/(mol*s)"),
        n = 2.24157,
        Ea = (-17894,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 117,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (51.3894,"m^3/(mol*s)"),
        n = -0.382825,
        Ea = (32842.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 118,
    label = "InChI=1/C3H5/c1-3-2/h3H,1-2H2",
    group = 
"""
1 *3 C 1 {2,S} {4,S} {5,S}
2    C 0 {1,S} {3,D} {6,S}
3    C 0 {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.000196638,"m^3/(mol*s)"),
        n = 1.23877,
        Ea = (17968.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,D} {4,S}
3     C 0 {2,D} {8,S} {9,S}
4  *3 C 1 {2,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (5.14489e-08,"m^3/(mol*s)"),
        n = 2.04257,
        Ea = (13980.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.77347e+06,"m^3/(mol*s)"),
        n = -1.78488,
        Ea = (36507.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.63252e-11,"m^3/(mol*s)"),
        n = 2.87306,
        Ea = (-27222.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 123,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.000137399,"m^3/(mol*s)"),
        n = 0.852296,
        Ea = (7268.59,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 124,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.000319684,"m^3/(mol*s)"),
        n = 0.825146,
        Ea = (-4686.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 125,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.000130895,"m^3/(mol*s)"),
        n = 0.901133,
        Ea = (-13644.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 126,
    label = "InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group = 
"""
1     C 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 {1,S} {2,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (2.10662e-10,"m^3/(mol*s)"),
        n = 2.48169,
        Ea = (-18581.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 127,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3",
    group = 
"""
1     C 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 {1,S} {5,S} {8,S} {9,S}
3     C 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {3,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.00756301,"m^3/(mol*s)"),
        n = 0.438768,
        Ea = (-17302.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 128,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3",
    group = 
"""
1     C 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 {4,S} {5,S} {11,S} {12,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4  *3 C 1 {1,S} {2,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.0035238,"m^3/(mol*s)"),
        n = 0.538768,
        Ea = (-16549.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 129,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {3,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.00980391,"m^3/(mol*s)"),
        n = -0.071232,
        Ea = (-25001.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 130,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.04918e-07,"m^3/(mol*s)"),
        n = 1.79171,
        Ea = (-21286.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 131,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.04918e-07,"m^3/(mol*s)"),
        n = 1.79171,
        Ea = (-21286.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 132,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 C 1 {2,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.0166386,"m^3/(mol*s)"),
        n = 0.408768,
        Ea = (-17428,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 133,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (7.19139e-10,"m^3/(mol*s)"),
        n = 2.48318,
        Ea = (-23216.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 134,
    label = "C_rad/H/O2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0441452,"m^3/(mol*s)"),
        n = 0.244318,
        Ea = (17675.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 136,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0441452,"m^3/(mol*s)"),
        n = 0.244318,
        Ea = (17675.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 137,
    label = "C_rad/H/CO/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.24648e-08,"m^3/(mol*s)"),
        n = 2.0706,
        Ea = (-8843.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 138,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 {1,S} {3,S} {7,S}
3    C 0 {2,S} {8,D} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    O 0 {3,D}
9    H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (1.26089e-07,"m^3/(mol*s)"),
        n = 1.72669,
        Ea = (-967.057,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 139,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0159112,"m^3/(mol*s)"),
        n = 0.282163,
        Ea = (3520.44,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 142,
    label = "C_rad/NonDeC",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    {Cs,O} 0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.61904e-05,"m^3/(mol*s)"),
        n = 0.977617,
        Ea = (-13537.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 143,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.000413377,"m^3/(mol*s)"),
        n = 0.707748,
        Ea = (-8872.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 144,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 {1,S} {2,S} {3,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (4.45953e-10,"m^3/(mol*s)"),
        n = 2.34815,
        Ea = (-24817.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 145,
    label = "C_rad/NDMustO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    O      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.65431e-08,"m^3/(mol*s)"),
        n = 1.91091,
        Ea = (-29668.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 146,
    label = "C_rad/OOH/Cs/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S} {5,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    O  0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.64938e-14,"m^3/(mol*s)"),
        n = 3.75306,
        Ea = (-40318.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 147,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 {1,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = Arrhenius(
        A = (0.193837,"m^3/(mol*s)"),
        n = 0.068768,
        Ea = (-19018,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 148,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (308825,"m^3/(mol*s)"),
        n = -1.78488,
        Ea = (54219.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 149,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (308825,"m^3/(mol*s)"),
        n = -1.78488,
        Ea = (54219.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:43:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 150,
    label = "C_rad/ODMustO",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    O             0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "C_rad/TDMustO",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

tree(
"""
L1: X_H_or_Xrad_H
    L2: Xrad_H
    L2: X_H
        L3: H2
        L3: Ct_H
        L3: O_H
            L4: O_pri
            L4: O_sec
                L5: O/H/NonDeC
                L5: O/H/NonDeO
                    L6: H2O2
                    L6: ROOH_pri
                    L6: ROOH_sec
                    L6: ROOH_ter
                L5: O/H/OneDe
        L3: Orad_O_H
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cb_H
        L3: CO_H
            L4: CO_pri
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3
                L5: CO/H/OneDe
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C/H3/Cs
                    L6: InChI=1/C2H6/c1-2/h1-2H3
                    L6: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma
                L5: C/H3/Cd
                    L6: InChI=1/C3H6/c1-3-2/h3H,1H2,2H3
                    L6: InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3
                    L6: InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+
                L5: C/H3/Ct
                L5: C/H3/Cb
                L5: C/H3/CO
                L5: C/H3/O
            L4: C_sec
                L5: C/H2/NonDeC
                    L6: InChI=1/C3H8/c1-3-2/h3H2,1-2H3
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha
                    L6: C/H2/O2
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                        L7: InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta
                        L7: InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3
                    L6: C/H2/OneDeO
                L5: C/H2/TwoDe
                L5: C/H2/Cb
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta
                    L6: C/H/NDMustO
                L5: C/H/OneDe
                    L6: C/H/Cs2
                        L7: InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3
                    L6: C/H/ODMustO
                L5: C/H/TwoDe
                    L6: C/H/Cs
                    L6: C/H/TDMustO
                L5: C/H/ThreeDe
                L5: C/H/Cb
L1: Y_rad_birad
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: C2b
        L3: Ct_rad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3
                L5: O_rad/NonDeO
                    L6: OOCH3
                L5: O_rad/OneDe
                    L6: InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3
                    L6: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: InChI=1/C2H3/c1-2/h1H,2H2
                L5: InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: InChI=1/C3H5/c1-3-2/h1H2,2H3
                    L6: InChI=1/C4H7/c1-3-4-2/h3H,1-2H3
                L5: Cd_rad/NonDeO
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                    L6: InChI=1/C2H5/c1-2/h1H2,2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3
                    L6: InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3
                L5: C_rad/H2/Cd
                    L6: InChI=1/C3H5/c1-3-2/h3H,1-2H2
                    L6: InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                    L6: InChI=1/C3H7/c1-3-2/h3H,1-2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                        L7: InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3
                    L6: C_rad/H/O2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: C_rad/H/CO/Cs
                            L8: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c
                    L6: C_rad/H/OneDeO
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3
                    L6: C_rad/NDMustO
                        L7: C_rad/OOH/Cs/Cs
                        L7: InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
"""
)

