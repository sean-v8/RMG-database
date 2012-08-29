#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_12birad"], products=["Y_alkene"], ownReverse=False)

reverse = "Alkene_to_1,2-birad"

recipe(actions=[
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_12birad",
    group = "OR{Y_12_00, Y_12_10, Y_12_20, Y_12_30, Y_12_40, Y_12_01, Y_12_02, Y_12_03, Y_12_04, Y_12_11, Y_12_12, Y_12_21, Y_12_22, Y_12_13, Y_12_31}",
    kinetics = Arrhenius(
        A = (2.3706e+07,"s^-1"),
        n = 2.06501e-14,
        Ea = (-9.90874e-11,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_12_00",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S} {4,S}
2 *2 Cs 1 {1,S} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = Arrhenius(
        A = (4.21835,"s^-1"),
        n = -5.70655e-14,
        Ea = (-6.88338e-12,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "Y_12_10",
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    H       0 {1,S}
5    H       0 {2,S}
6    H       0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.66178,"s^-1"),
        n = -3.25961e-13,
        Ea = (1.58273e-09,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "Y_12_20",
    group = "OR{Y_12_20a, Y_12_20b}",
    kinetics = Arrhenius(
        A = (1.6789,"s^-1"),
        n = 5.15143e-14,
        Ea = (-3.5582e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "Y_12_30",
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    {Cs,Os} 0 {2,S}
6    H       0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.05881,"s^-1"),
        n = -1.11473e-14,
        Ea = (4.71845e-11,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "Y_12_40",
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    {Cs,Os} 0 {2,S}
6    {Cs,Os} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.666499,"s^-1"),
        n = 1.01828e-14,
        Ea = (-7.82985e-11,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Y_12_01",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.11339,"s^-1"),
        n = 9.87752e-15,
        Ea = (-1.32776e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "Y_12_02",
    group = "OR{Y_12_02a, Y_12_02b}",
    kinetics = Arrhenius(
        A = (1.05881,"s^-1"),
        n = -2.27041e-14,
        Ea = (1.43469e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Y_12_03",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    H             0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.531512,"s^-1"),
        n = -1.07539e-13,
        Ea = (6.03004e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Y_12_04",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.266178,"s^-1"),
        n = -1.15186e-14,
        Ea = (-1.70974e-11,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Y_12_11",
    group = "OR{Y_12_11a, Y_12_11b}",
    kinetics = Arrhenius(
        A = (1.333,"s^-1"),
        n = -5.14172e-15,
        Ea = (1.38778e-11,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Y_12_12",
    group = "OR{Y_12_12a, Y_12_12b}",
    kinetics = Arrhenius(
        A = (0.666499,"s^-1"),
        n = 1.09743e-14,
        Ea = (-1.69069e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "Y_12_21",
    group = "OR{Y_12_21a, Y_12_21b}",
    kinetics = Arrhenius(
        A = (0.84367,"s^-1"),
        n = -4.56857e-14,
        Ea = (1.97786e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Y_12_22",
    group = "OR{Y_12_22a, Y_12_22b}",
    kinetics = Arrhenius(
        A = (0.421835,"s^-1"),
        n = 1.86517e-14,
        Ea = (-1.09399e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "Y_12_13",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cs,Os}       0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.334937,"s^-1"),
        n = -3.9746e-14,
        Ea = (1.97842e-10,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "Y_12_31",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cs,Os}       0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.531512,"s^-1"),
        n = -2.22045e-15,
        Ea = (4.89886e-12,"J/mol"),
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
        ("Wed Aug 29 13:45:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = -1,
    label = "Y_12_20a",
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    H       0 {2,S}
6    H       0 {2,S}
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
    label = "Y_12_20b",
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    H       0 {1,S}
5    {Cs,Os} 0 {2,S}
6    H       0 {2,S}
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
    label = "Y_12_02a",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
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
    index = -1,
    label = "Y_12_02b",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = -1,
    label = "Y_12_11a",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
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
    index = -1,
    label = "Y_12_11b",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cs,Os}       0 {2,S}
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
    index = -1,
    label = "Y_12_12a",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
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
    index = -1,
    label = "Y_12_12b",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = -1,
    label = "Y_12_21a",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = -1,
    label = "Y_12_21b",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
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
    index = -1,
    label = "Y_12_22a",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
6    {Cs,Os}       0 {2,S}
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
    label = "Y_12_22b",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cs,Os}       0 {2,S}
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
L1: Y_12birad
    L2: Y_12_00
    L2: Y_12_10
    L2: Y_12_20
    L2: Y_12_30
    L2: Y_12_40
    L2: Y_12_01
    L2: Y_12_02
    L2: Y_12_03
    L2: Y_12_04
    L2: Y_12_11
    L2: Y_12_12
    L2: Y_12_21
    L2: Y_12_22
    L2: Y_12_13
    L2: Y_12_31
"""
)

