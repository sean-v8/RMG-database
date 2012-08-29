#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XZ", "Y_rad_birad"], products=["YXZ."], ownReverse=False)

reverse = "Beta_Scission"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XZ",
    group = "OR{CZ, OCO, OCddO, OSi, OSiddO}",
    kinetics = Arrhenius(
        A = (553853,"m^3/(mol*s)"),
        n = 0.12118,
        Ea = (28796.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad",
    group = "OR{Y_rad, Y_birad}",
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
    label = "CZ",
    group = 
"""
1 *1 {Cd,Cdd,Ct,CO,Sid,Sidd,Sit} 0 {2,{D,T}}
2 *2 {Cd,Cdd,Ct,Od,Sid,Sidd,Sit} 0 {1,{D,T}}
""",
    kinetics = Arrhenius(
        A = (0.992864,"m^3/(mol*s)"),
        n = 0.000299951,
        Ea = (66.1005,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "Cd_Cd",
    group = 
"""
1 *1 Cd 0 {2,D}
2 *2 Cd 0 {1,D}
""",
    kinetics = Arrhenius(
        A = (0.822301,"m^3/(mol*s)"),
        n = 0.0115325,
        Ea = (1226.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "Cd/H2",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.853073,"m^3/(mol*s)"),
        n = 0.0147475,
        Ea = (-305.948,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "Cd/H2_Cd/H2",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.632084,"m^3/(mol*s)"),
        n = 0.0252181,
        Ea = (3028.33,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Cd/H2_Cd/H/Nd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.195614,"m^3/(mol*s)"),
        n = 0.184092,
        Ea = (327.138,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "Cd/H2_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.8046,"m^3/(mol*s)"),
        n = -0.106451,
        Ea = (-9292.45,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Cd/H2_Cd/Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (4.08419,"m^3/(mol*s)"),
        n = -0.055313,
        Ea = (-8277.29,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Cd/H2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (9.62785,"m^3/(mol*s)"),
        n = -0.103605,
        Ea = (-14107.9,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Cd/H2_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (14.4389,"m^3/(mol*s)"),
        n = -0.112143,
        Ea = (-19863.3,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Cd/H/Nd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.186149,"m^3/(mol*s)"),
        n = 0.182875,
        Ea = (4211.86,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "Cd/H/Nd_Cd/H2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.104767,"m^3/(mol*s)"),
        n = 0.297241,
        Ea = (3182.02,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Cd/H/Nd_Cd/H/Nd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
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
    label = "Cd/H/Nd_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 16,
    label = "Cd/H/Nd_Cd/Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
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
    index = 17,
    label = "Cd/H/Nd_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 18,
    label = "Cd/H/Nd_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 19,
    label = "Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.56793,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (5047.35,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "Cd/H/De_Cd/H2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.56793,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (5047.35,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "Cd/H/De_Cd/H/Nd",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
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
    index = 22,
    label = "Cd/H/De_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 23,
    label = "Cd/H/De_Cd/Nd2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
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
    index = 24,
    label = "Cd/H/De_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 25,
    label = "Cd/H/De_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.977598,"m^3/(mol*s)"),
        n = -0.100494,
        Ea = (5948.69,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "Cd/Nd2_Cd/H2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.21009,"m^3/(mol*s)"),
        n = -0.109039,
        Ea = (10606,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 28,
    label = "Cd/Nd2_Cd/H/Nd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
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
    label = "Cd/Nd2_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/Nd2_Cd/Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
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
    index = 31,
    label = "Cd/Nd2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 32,
    label = "Cd/Nd2_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.32413,"m^3/(mol*s)"),
        n = -0.103605,
        Ea = (7544.27,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "Cd/Nd/De_Cd/H2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.32413,"m^3/(mol*s)"),
        n = -0.103605,
        Ea = (7544.27,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "Cd/Nd/De_Cd/H/Nd",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
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
    label = "Cd/Nd/De_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/Nd/De_Cd/Nd2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
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
    label = "Cd/Nd/De_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/Nd/De_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 40,
    label = "Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D}
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
    index = 41,
    label = "Cd/De2_Cd/H2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
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
    index = 42,
    label = "Cd/De2_Cd/H/Nd",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
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
    label = "Cd/De2_Cd/H/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/De2_Cd/Nd2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
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
    label = "Cd/De2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd/De2_Cd/De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Cd_Cdd",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D}
""",
    kinetics = Arrhenius(
        A = (2.13612,"m^3/(mol*s)"),
        n = -0.103365,
        Ea = (-3182.53,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 48,
    label = "Cd_Ca",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    C   0 {2,D}
""",
    kinetics = Arrhenius(
        A = (2.13612,"m^3/(mol*s)"),
        n = -0.103365,
        Ea = (-3182.53,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 49,
    label = "Cd/H2_Ca",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    kinetics = Arrhenius(
        A = (3.14769,"m^3/(mol*s)"),
        n = -0.104293,
        Ea = (-5469.14,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 50,
    label = "Cd/H/Nd_Ca",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    C      0 {2,D}
""",
    kinetics = Arrhenius(
        A = (1.08388,"m^3/(mol*s)"),
        n = -0.101742,
        Ea = (819.03,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 51,
    label = "Cd/H/De_Ca",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    C             0 {2,D}
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
    index = 52,
    label = "Cd/Nd2_Ca",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    C      0 {2,D}
""",
    kinetics = Arrhenius(
        A = (1.08388,"m^3/(mol*s)"),
        n = -0.101742,
        Ea = (819.03,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 53,
    label = "Cd/Nd/De_Ca",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    C             0 {2,D}
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
    index = 54,
    label = "Cd/De2_Ca",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    C             0 {2,D}
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
    index = 55,
    label = "Cd_Ck",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
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
    label = "Cd/H2_Ck",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    Od  0 {2,D}
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
    index = 57,
    label = "Cd/H/Nd_Ck",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
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
    index = 58,
    label = "Cd/H/De_Ck",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
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
    index = 59,
    label = "Cd/Nd2_Ck",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
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
    index = 60,
    label = "Cd/Nd/De_Ck",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
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
    index = 61,
    label = "Cd/De2_Ck",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
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
    index = 62,
    label = "Cdd_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Cd  0 {1,D}
""",
    kinetics = Arrhenius(
        A = (3.94524,"m^3/(mol*s)"),
        n = -0.013313,
        Ea = (-4238.34,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 63,
    label = "Ca_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D}
3    C   0 {1,D}
""",
    kinetics = Arrhenius(
        A = (3.94524,"m^3/(mol*s)"),
        n = -0.013313,
        Ea = (-4238.34,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 64,
    label = "Ca_Cd/H2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    C   0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.183829,"m^3/(mol*s)"),
        n = 0.170687,
        Ea = (-11708.2,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 65,
    label = "Ca_Cd/H/Nd",
    group = 
"""
1 *1 Cdd    0 {2,D} {3,D}
2 *2 Cd     0 {1,D} {4,S} {5,S}
3    C      0 {1,D}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (12.15,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (1588.58,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 66,
    label = "Ca_Cd/H/De",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    C             0 {1,D}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Ca_Cd/Nd2",
    group = 
"""
1 *1 Cdd    0 {2,D} {3,D}
2 *2 Cd     0 {1,D} {4,S} {5,S}
3    C      0 {1,D}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (27.4934,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (-2595.42,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "Ca_Cd/Nd/De",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    C             0 {1,D}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 69,
    label = "Ca_Cd/De2",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    C             0 {1,D}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "Ck_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D}
3    Od  0 {1,D}
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
    label = "Ck_Cd/H2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    Od  0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
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
    index = 72,
    label = "Ck_Cd/H/Nd",
    group = 
"""
1 *1 Cdd    0 {2,D} {3,D}
2 *2 Cd     0 {1,D} {4,S} {5,S}
3    Od     0 {1,D}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
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
    index = 73,
    label = "Ck_Cd/H/De",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    Od            0 {1,D}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 74,
    label = "Ck_Cd/Nd2",
    group = 
"""
1 *1 Cdd    0 {2,D} {3,D}
2 *2 Cd     0 {1,D} {4,S} {5,S}
3    Od     0 {1,D}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
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
    index = 75,
    label = "Ck_Cd/Nd/De",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    Od            0 {1,D}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 76,
    label = "Ck_Cd/De2",
    group = 
"""
1 *1 Cdd           0 {2,D} {3,D}
2 *2 Cd            0 {1,D} {4,S} {5,S}
3    Od            0 {1,D}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 77,
    label = "Cdd_Cdd",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Cdd 0 {1,D}
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
    index = 78,
    label = "Ca_Ca",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    C   0 {1,D}
4    C   0 {2,D}
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
    index = 79,
    label = "Ck_Ck",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    Od  0 {1,D}
4    Od  0 {2,D}
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
    index = 80,
    label = "Ca_Ck",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    C   0 {1,D}
4    Od  0 {2,D}
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
    index = 81,
    label = "Ck_Ca",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    Od  0 {1,D}
4    C   0 {2,D}
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
    index = 82,
    label = "Cdd_Od",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Od  0 {1,D}
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
    index = 83,
    label = "CO2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
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
    index = 84,
    label = "Ck_O",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    C   0 {1,D}
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
    index = 85,
    label = "CO_O",
    group = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    kinetics = Arrhenius(
        A = (0.321996,"m^3/(mol*s)"),
        n = -0.110122,
        Ea = (6160.28,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 86,
    label = "CO/H2_O",
    group = 
"""
1 *1 CO 0 {2,D} {3,S} {4,S}
2 *2 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.729349,"m^3/(mol*s)"),
        n = -0.173437,
        Ea = (-6353.55,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 87,
    label = "CO/H/Nd_O",
    group = 
"""
1 *1 CO     0 {2,D} {3,S} {4,S}
2 *2 Od     0 {1,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
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
    index = 88,
    label = "CO/H/De_O",
    group = 
"""
1 *1 CO            0 {2,D} {3,S} {4,S}
2 *2 Od            0 {1,D}
3    H             0 {1,S}
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
    index = 89,
    label = "CO/Nd2_O",
    group = 
"""
1 *1 CO     0 {2,D} {3,S} {4,S}
2 *2 Od     0 {1,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0817687,"m^3/(mol*s)"),
        n = -0.112143,
        Ea = (13650.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 90,
    label = "CO/Nd/De_O",
    group = 
"""
1 *1 CO            0 {2,D} {3,S} {4,S}
2 *2 Od            0 {1,D}
3    {Cs,O}        0 {1,S}
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
    index = 91,
    label = "CO/De2_O",
    group = 
"""
1 *1 CO            0 {2,D} {3,S} {4,S}
2 *2 Od            0 {1,D}
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
    index = 92,
    label = "Ct_Ct",
    group = 
"""
1 *1 Ct 0 {2,T}
2 *2 Ct 0 {1,T}
""",
    kinetics = Arrhenius(
        A = (1.53135,"m^3/(mol*s)"),
        n = 0.0186128,
        Ea = (-3628.19,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 93,
    label = "Ct/H_Ct/H",
    group = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.249079,"m^3/(mol*s)"),
        n = 0.0911203,
        Ea = (-7224.8,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "Ct/H_Ct/Nd",
    group = 
"""
1 *1 Ct     0 {2,T} {3,S}
2 *2 Ct     0 {1,T} {4,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (160.539,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (2843.78,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 95,
    label = "Ct/H_Ct/De",
    group = 
"""
1 *1 Ct            0 {2,T} {3,S}
2 *2 Ct            0 {1,T} {4,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (18.9866,"m^3/(mol*s)"),
        n = -0.100759,
        Ea = (-9632.59,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "Ct/Nd_Ct/H",
    group = 
"""
1 *1 Ct     0 {2,T} {3,S}
2 *2 Ct     0 {1,T} {4,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
""",
    kinetics = Arrhenius(
        A = (39.5667,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (10040.3,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 97,
    label = "Ct/Nd_Ct/Nd",
    group = 
"""
1 *1 Ct     0 {2,T} {3,S}
2 *2 Ct     0 {1,T} {4,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {2,S}
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
    index = 98,
    label = "Ct/Nd_Ct/De",
    group = 
"""
1 *1 Ct            0 {2,T} {3,S}
2 *2 Ct            0 {1,T} {4,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 99,
    label = "Ct/De_Ct/H",
    group = 
"""
1 *1 Ct            0 {2,T} {3,S}
2 *2 Ct            0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
""",
    kinetics = Arrhenius(
        A = (22.3599,"m^3/(mol*s)"),
        n = -0.105313,
        Ea = (9328.98,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 100,
    label = "Ct/De_Ct/Nd",
    group = 
"""
1 *1 Ct            0 {2,T} {3,S}
2 *2 Ct            0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
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
    index = 101,
    label = "Ct/De_Ct/De",
    group = 
"""
1 *1 Ct            0 {2,T} {3,S}
2 *2 Ct            0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 102,
    label = "OCO",
    group = 
"""
1 *1 Od 0 {2,D}
2 *2 CO 0 {1,D}
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
    index = 103,
    label = "OSi",
    group = 
"""
1 *1 Od 0 {2,D}
2 *2 Si 0 {1,D}
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
    index = 104,
    label = "OCddO",
    group = 
"""
1 *2 Cdd 0 {2,D} {3,D}
2 *1 Od  0 {1,D}
3    Od  0 {1,D}
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
    index = 105,
    label = "OSiddO",
    group = 
"""
1 *2 Sidd 0 {2,D} {3,D}
2 *1 Od   0 {1,D}
3    Od   0 {1,D}
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
    index = 106,
    label = "H_rad",
    group = 
"""
1 *3 H 1
""",
    kinetics = Arrhenius(
        A = (15.2817,"m^3/(mol*s)"),
        n = -0.0522247,
        Ea = (-15086.7,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 107,
    label = "Ct_rad",
    group = 
"""
1 *3 Ct 1 {2,T}
2    Ct 0 {1,T}
""",
    kinetics = Arrhenius(
        A = (11.508,"m^3/(mol*s)"),
        n = -0.148688,
        Ea = (-26099.9,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 108,
    label = "O_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.244453,"m^3/(mol*s)"),
        n = 0.0786731,
        Ea = (-4471.29,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 109,
    label = "O_pri_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.151644,"m^3/(mol*s)"),
        n = 0.380984,
        Ea = (-25566.3,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 110,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.338907,"m^3/(mol*s)"),
        n = -0.128171,
        Ea = (9962.17,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 111,
    label = "O_rad/NonDe",
    group = 
"""
1 *3 O      1 {2,S}
2    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.221841,"m^3/(mol*s)"),
        n = -0.132232,
        Ea = (13433.1,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 112,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O             1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.34327,"m^3/(mol*s)"),
        n = -0.0845728,
        Ea = (89.5394,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 113,
    label = "Cd_rad",
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    R  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.203649,"m^3/(mol*s)"),
        n = 0.19293,
        Ea = (-12630.5,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 114,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0612369,"m^3/(mol*s)"),
        n = 0.283061,
        Ea = (-13146.8,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 115,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 Cd  1 {2,D} {3,S}
2    Cd  0 {1,D}
3    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (15.4031,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (-10771.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 116,
    label = "Cd_rad/NonDe",
    group = 
"""
1 *3 Cd     1 {2,D} {3,S}
2    Cd     0 {1,D}
3    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (15.4031,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (-10771.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 117,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 Cd            1 {2,D} {3,S}
2    Cd            0 {1,D}
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
    index = 118,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = Arrhenius(
        A = (35.742,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (-18302.8,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "CO_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.37308,"m^3/(mol*s)"),
        n = -0.0845728,
        Ea = (-3425.02,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.37308,"m^3/(mol*s)"),
        n = -0.0845728,
        Ea = (-3425.02,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
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
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C      1 {2,D} {3,S}
2    O      0 {1,D}
3    {Cs,O} 0 {1,S}
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
    index = 123,
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
    index = 124,
    label = "Cs_rad",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.36405,"m^3/(mol*s)"),
        n = -0.0255279,
        Ea = (9592.16,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 125,
    label = "C_methyl",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.933162,"m^3/(mol*s)"),
        n = -0.00158255,
        Ea = (7539.82,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 126,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.126149,"m^3/(mol*s)"),
        n = 0.0383025,
        Ea = (11068.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 127,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0325026,"m^3/(mol*s)"),
        n = 0.196253,
        Ea = (1698.24,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 128,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.571773,"m^3/(mol*s)"),
        n = -0.143512,
        Ea = (27937.3,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 129,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.65937,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (20608.4,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 130,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.41266,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (20190,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 131,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
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
    index = 132,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0512727,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (-478.977,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 133,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.40228,"m^3/(mol*s)"),
        n = -0.134398,
        Ea = (21470.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 134,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.161474,"m^3/(mol*s)"),
        n = -0.139161,
        Ea = (1057.87,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 135,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
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
    index = 136,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
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
    index = 137,
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
    index = 138,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.382761,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (23537.2,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 139,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.382761,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (23537.2,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 140,
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
    index = 141,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.2977,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (54080.4,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 142,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.046405,"m^3/(mol*s)"),
        n = -0.138425,
        Ea = (7980.22,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 143,
    label = "C_rad/NonDeC",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    {Cs,O} 0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.030891,"m^3/(mol*s)"),
        n = -0.142113,
        Ea = (-4164.29,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 144,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.030891,"m^3/(mol*s)"),
        n = -0.142113,
        Ea = (-4164.29,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
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
    index = 146,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.110158,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (20399.2,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 147,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.110158,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (20399.2,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 148,
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
    index = 149,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0804195,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (51151.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 150,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.0804195,"m^3/(mol*s)"),
        n = -0.13154,
        Ea = (51151.6,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 151,
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
    index = 152,
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

entry(
    index = 153,
    label = "Cd_pri_rad-Cdd/Cd",
    group = 
"""
1 *3 Cd  1 {2,D} {3,S}
2    Cdd 0 {1,D} {4,D}
3    H   0 {1,S}
4    Cd  0 {2,D}
""",
    kinetics = Arrhenius(
        A = (3.17061e-10,"m^3/(mol*s)"),
        n = 2.87586,
        Ea = (12955,"J/mol"),
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
        ("Wed Aug 29 13:43:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = -1,
    label = "Y_rad",
    group = 
"""
1 *3 R 1
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
    index = -1,
    label = "Y_birad",
    group = 
"""
1 *3 R {2S,2T}
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
L1: XZ
    L2: CZ
        L3: Cd_Cd
            L4: Cd/H2
                L5: Cd/H2_Cd/H2
                L5: Cd/H2_Cd/H/Nd
                L5: Cd/H2_Cd/H/De
                L5: Cd/H2_Cd/Nd2
                L5: Cd/H2_Cd/Nd/De
                L5: Cd/H2_Cd/De2
            L4: Cd/H/Nd
                L5: Cd/H/Nd_Cd/H2
                L5: Cd/H/Nd_Cd/H/Nd
                L5: Cd/H/Nd_Cd/H/De
                L5: Cd/H/Nd_Cd/Nd2
                L5: Cd/H/Nd_Cd/Nd/De
                L5: Cd/H/Nd_Cd/De2
            L4: Cd/H/De
                L5: Cd/H/De_Cd/H2
                L5: Cd/H/De_Cd/H/Nd
                L5: Cd/H/De_Cd/H/De
                L5: Cd/H/De_Cd/Nd2
                L5: Cd/H/De_Cd/Nd/De
                L5: Cd/H/De_Cd/De2
            L4: Cd/Nd2
                L5: Cd/Nd2_Cd/H2
                L5: Cd/Nd2_Cd/H/Nd
                L5: Cd/Nd2_Cd/H/De
                L5: Cd/Nd2_Cd/Nd2
                L5: Cd/Nd2_Cd/Nd/De
                L5: Cd/Nd2_Cd/De2
            L4: Cd/Nd/De
                L5: Cd/Nd/De_Cd/H2
                L5: Cd/Nd/De_Cd/H/Nd
                L5: Cd/Nd/De_Cd/H/De
                L5: Cd/Nd/De_Cd/Nd2
                L5: Cd/Nd/De_Cd/Nd/De
                L5: Cd/Nd/De_Cd/De2
            L4: Cd/De2
                L5: Cd/De2_Cd/H2
                L5: Cd/De2_Cd/H/Nd
                L5: Cd/De2_Cd/H/De
                L5: Cd/De2_Cd/Nd2
                L5: Cd/De2_Cd/Nd/De
                L5: Cd/De2_Cd/De2
        L3: Cd_Cdd
            L4: Cd_Ca
                L5: Cd/H2_Ca
                L5: Cd/H/Nd_Ca
                L5: Cd/H/De_Ca
                L5: Cd/Nd2_Ca
                L5: Cd/Nd/De_Ca
                L5: Cd/De2_Ca
            L4: Cd_Ck
                L5: Cd/H2_Ck
                L5: Cd/H/Nd_Ck
                L5: Cd/H/De_Ck
                L5: Cd/Nd2_Ck
                L5: Cd/Nd/De_Ck
                L5: Cd/De2_Ck
        L3: Cdd_Cd
            L4: Ca_Cd
                L5: Ca_Cd/H2
                L5: Ca_Cd/H/Nd
                L5: Ca_Cd/H/De
                L5: Ca_Cd/Nd2
                L5: Ca_Cd/Nd/De
                L5: Ca_Cd/De2
            L4: Ck_Cd
                L5: Ck_Cd/H2
                L5: Ck_Cd/H/Nd
                L5: Ck_Cd/H/De
                L5: Ck_Cd/Nd2
                L5: Ck_Cd/Nd/De
                L5: Ck_Cd/De2
        L3: Cdd_Cdd
            L4: Ca_Ca
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
        L3: CO_O
            L4: CO/H2_O
            L4: CO/H/Nd_O
            L4: CO/H/De_O
            L4: CO/Nd2_O
            L4: CO/Nd/De_O
            L4: CO/De2_O
        L3: Ct_Ct
            L4: Ct/H_Ct/H
            L4: Ct/H_Ct/Nd
            L4: Ct/H_Ct/De
            L4: Ct/Nd_Ct/H
            L4: Ct/Nd_Ct/Nd
            L4: Ct/Nd_Ct/De
            L4: Ct/De_Ct/H
            L4: Ct/De_Ct/Nd
            L4: Ct/De_Ct/De
    L2: OCO
    L2: OSi
    L2: OCddO
    L2: OSiddO
L1: Y_rad_birad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
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
    L2: Cd_pri_rad-Cdd/Cd
"""
)

forbidden(
    label = "O2_birad",
    group = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

forbidden(
    label = "O2d",
    group = 
"""
1 *1 O 0 {2,D}
2 *2 O 0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

