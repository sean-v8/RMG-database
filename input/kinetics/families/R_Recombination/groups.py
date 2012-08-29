#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad", "Y_rad"], products=["Y_Y"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    group = 
"""
1 * R 1
""",
    kinetics = Arrhenius(
        A = (4.65022e+07,"m^3/(mol*s)"),
        n = -0.207264,
        Ea = (138.949,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "H_rad",
    group = 
"""
1 * H 1
""",
    kinetics = Arrhenius(
        A = (0.501503,"m^3/(mol*s)"),
        n = 0.254101,
        Ea = (-394.597,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "Ct_rad",
    group = 
"""
1 * C 1 {2,T}
2   C 0 {1,T}
""",
    kinetics = Arrhenius(
        A = (2.73601,"m^3/(mol*s)"),
        n = 0.099646,
        Ea = (-208.807,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "O_rad",
    group = 
"""
1 * O 1 {2,S}
2   R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.243646,"m^3/(mol*s)"),
        n = 0.236405,
        Ea = (-104.694,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "O_pri_rad",
    group = 
"""
1 * O 1 {2,S}
2   H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.02053,"m^3/(mol*s)"),
        n = 0.16255,
        Ea = (-49.78,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "O_sec_rad",
    group = 
"""
1 * O   1 {2,S}
2   R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0985987,"m^3/(mol*s)"),
        n = 0.266699,
        Ea = (-137.123,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "O_rad/NonDe",
    group = 
"""
1 * O      1 {2,S}
2   {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0700538,"m^3/(mol*s)"),
        n = 0.300656,
        Ea = (-145.888,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O_rad/OneDe",
    group = 
"""
1 * O             1 {2,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 9,
    label = "O2_birad",
    group = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.042218,"m^3/(mol*s)"),
        n = 0.285577,
        Ea = (396.269,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Cd_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   C 0 {1,D}
3   R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.39979,"m^3/(mol*s)"),
        n = 0.141993,
        Ea = (371.943,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Cd_pri_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   C 0 {1,D}
3   H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.39979,"m^3/(mol*s)"),
        n = 0.141993,
        Ea = (371.943,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Cd_sec_rad",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   0 {1,D}
3   R!H 0 {1,S}
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
    index = 13,
    label = "Cd_rad/NonDe",
    group = 
"""
1 * C      1 {2,D} {3,S}
2   C      0 {1,D}
3   {Cs,O} 0 {1,S}
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
    index = 14,
    label = "Cd_rad/OneDe",
    group = 
"""
1 * C             1 {2,D} {3,S}
2   C             0 {1,D}
3   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "Cb_rad",
    group = 
"""
1 * Cb       1 {2,B} {3,B}
2   {Cb,Cbf} 0 {1,B}
3   {Cb,Cbf} 0 {1,B}
""",
    kinetics = Arrhenius(
        A = (0.267114,"m^3/(mol*s)"),
        n = 0.210532,
        Ea = (102.572,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "CO_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   O 0 {1,D}
3   R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.4399,"m^3/(mol*s)"),
        n = 0.108623,
        Ea = (-763.073,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "CO_pri_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   O 0 {1,D}
3   H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.154989,"m^3/(mol*s)"),
        n = 0.250088,
        Ea = (-1458.6,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "CO_sec_rad",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.18115,"m^3/(mol*s)"),
        n = -0.0222974,
        Ea = (-65.3475,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "CO_rad/NonDe",
    group = 
"""
1 * C      1 {2,D} {3,S}
2   O      0 {1,D}
3   {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.18115,"m^3/(mol*s)"),
        n = -0.0222974,
        Ea = (-65.3475,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "CO_rad/OneDe",
    group = 
"""
1 * C             1 {2,D} {3,S}
2   O             0 {1,D}
3   {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 21,
    label = "Cs_rad",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   R 0 {1,S}
3   R 0 {1,S}
4   R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (3.66172,"m^3/(mol*s)"),
        n = -0.200853,
        Ea = (138.18,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "C_methyl",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.11577,"m^3/(mol*s)"),
        n = -0.0951323,
        Ea = (435.033,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "C_pri_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.17933,"m^3/(mol*s)"),
        n = -0.0188394,
        Ea = (-82.05,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "C_rad/H2/Cs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.05568,"m^3/(mol*s)"),
        n = 0.0457877,
        Ea = (-44.2141,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "C_rad/H2/Cd",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cd 0 {1,S}
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
    index = 26,
    label = "C_rad/H2/Ct",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Ct 0 {1,S}
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
    index = 27,
    label = "C_rad/H2/Cb",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cb 0 {1,S}
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
    index = 28,
    label = "C_rad/H2/CO",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   CO 0 {1,S}
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
    index = 29,
    label = "C_rad/H2/O",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   O 0 {1,S}
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
    label = "C_sec_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.87308,"m^3/(mol*s)"),
        n = -0.233986,
        Ea = (-132.733,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.81757,"m^3/(mol*s)"),
        n = -0.215714,
        Ea = (-95.6529,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   H      0 {1,S}
3   O      0 {1,S}
4   {Cs,O} 0 {1,S}
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
    index = 33,
    label = "C_rad/H/CsO",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cs 0 {1,S}
4   O  0 {1,S}
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
    index = 34,
    label = "C_rad/H/O2",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   O 0 {1,S}
4   O 0 {1,S}
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
    index = 35,
    label = "C_rad/H/OneDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cs,O}        0 {1,S}
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
    index = 36,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   Cs            0 {1,S}
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
    index = 37,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   O             0 {1,S}
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
    index = 38,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 39,
    label = "C_ter_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (7.85949,"m^3/(mol*s)"),
        n = -0.466877,
        Ea = (102.153,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "C_rad/NonDeC",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   {Cs,O} 0 {1,S}
3   {Cs,O} 0 {1,S}
4   {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (14.7678,"m^3/(mol*s)"),
        n = -0.583195,
        Ea = (-53.9352,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "C_rad/Cs3",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (14.7678,"m^3/(mol*s)"),
        n = -0.583195,
        Ea = (-53.9352,"J/mol"),
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
        ("Wed Aug 29 13:45:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C_rad/NDMustO",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   O      0 {1,S}
3   {Cs,O} 0 {1,S}
4   {Cs,O} 0 {1,S}
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
    index = 43,
    label = "C_rad/OneDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cs,O}        0 {1,S}
4   {Cs,O}        0 {1,S}
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
    index = 44,
    label = "C_rad/Cs2",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   Cs            0 {1,S}
4   Cs            0 {1,S}
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
    index = 45,
    label = "C_rad/ODMustO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   O             0 {1,S}
4   {Cs,O}        0 {1,S}
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
    index = 46,
    label = "C_rad/TwoDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cs,O}        0 {1,S}
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
    index = 47,
    label = "C_rad/Cs",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   Cs            0 {1,S}
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
    index = 48,
    label = "C_rad/TDMustO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   O             0 {1,S}
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
    index = 49,
    label = "C_rad/ThreeDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cd,Ct,Cb,CO} 0 {1,S}
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
L1: Y_rad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: O2_birad
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                L5: C_rad/H/OneDeO
            L4: C_rad/H/TwoDe
        L3: C_ter_rad
            L4: C_rad/NonDeC
                L5: C_rad/Cs3
                L5: C_rad/NDMustO
            L4: C_rad/OneDe
                L5: C_rad/Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
"""
)

forbidden(
    label = "O4",
    group = 
"""
1    O 1 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4    O 1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

