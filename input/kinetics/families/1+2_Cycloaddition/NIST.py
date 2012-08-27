#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1957FRE/KIS6373-6379:1",
    reactant1 =
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 =
"""
1 *3 C 2T
""",
    product1 =
"""
1 *1 C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {3,S}
3 *3 C 0 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.98e+06,"m^3/(mol*s)","+|-",6.13e+05),
        n = 0,
        Ea = (22.116,"kJ/mol","+|-",1.106),
        T0 = 1,
        Tmin = (296,"K"),
        Tmax = (728,"K"),
        Pmin = (53300,"Pa"),
        Pmax = (427000,"Pa"),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Kistiakowsky, G.B."],
        title = u'Reactions of methylene. I. Ethylene, propane, cyclopropane and n-butane',
        journal = "J. Am. Chem. Soc.",
        volume = "79",
        pages = """6373-6379""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957FRE/KIS6373-6379:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Relative rate value measured""",
    longDesc =
u"""
Reference reaction: C2H4 + ·CH2 → Products (1993KRA/OEH545-553:1)
Bath gas: CO2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Mon Aug 27 16:56:58 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1957FRE/KIS6373-6379:1"""),
    ],
)

entry(
    index = 2,
    label = "1973GAE/GLA295:2",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 O 2T
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {3,S}
3 *3 O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700000,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
    ),
    reference = Article(
        authors = ["Gaedtke, H.", "Glaenzer, K.", "Hippler, H.", "Luther, K.", "Troe, J."],
        title = u'Addition Reactions of Oxygen Atoms at High Pressures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "14",
        pages = """295""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973GAE/GLA295:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Mon Aug 27 17:03:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1973GAE/GLA295:2"""),
    ],
)

entry(
    index = 3,
    label = "1973GAE/GLA295:7",
    reactant1 =
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    reactant2 =
"""
1 *3 O 2T
""",
    product1 =
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2 *2 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
    ),
    reference = Article(
        authors = ["Gaedtke, H.", "Glaenzer, K.", "Hippler, H.", "Luther, K.", "Troe, J."],
        title = u'Addition Reactions of Oxygen Atoms at High Pressures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "14",
        pages = """295""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973GAE/GLA295:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc =
u"""
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Mon Aug 27 17:17:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1973GAE/GLA295:7"""),
    ],
)

entry(
    index = 4,
    label = "1973HER13C:2",
    reactant1 =
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    reactant2 =
"""
1 *3 O 2T
""",
    product1 =
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2 *2 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (2.104,"kJ/mol"),
        T0 = 1,
        Tmin = (275,"K"),
        Tmax = (360,"K"),
        Pmin = (667,"Pa"),
    ),
    reference = Book(
        authors = ["Herbrechtsmeier, P."],
        title = u'Reactions of O(3P) Atoms with Unsaturated C3-Hydrocarbons',
        publisher = "ed. F. J. Weinberg, pub. Academic Press, London,",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973HER13C:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc =
u"""
Bath gas: CH3CH=CH2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
    history = [
        ("Mon Aug 27 17:20:11 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1973HER13C:2"""),
    ],
)

entry(
    index = 5,
    label = "1968SMI378-389:2",
    reactant1 =
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {3,D}
""",
    reactant2 =
"""
1 *3 O 2T
""",
    product1 =
"""
1 *1 C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S}
4    C 0 {2,S}
5 *3 O 0 {1,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+06,"m^3/(mol*s)","+|-",300000),
        n = 0,
        Ea = (3.342,"kJ/mol","+|-",1.671),
        T0 = 1,
        Tmin = (298,"K"),
        Tmax = (410,"K"),
    ),
    reference = Article(
        authors = ["Smith, I.W.M."],
        title = u'Rate parameters for reactions of O(3P) with CS2, NO2 and olefins',
        journal = "Trans. Faraday Soc.",
        volume = "64",
        pages = """378-389""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968SMI378-389:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc =
u"""
Reference Reaction: CS2 + O· → CS + SO
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Mon Aug 27 17:22:58 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1968SMI378-389:2"""),
    ],
)
