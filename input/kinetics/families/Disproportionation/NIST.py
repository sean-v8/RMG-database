#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1986TSA/HAM1087:46",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    reactant2 = 
"""
1 *4 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 1
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.02e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (285.186,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:46",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002190/rk00000001.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:09:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:46"""),
    ],
)

entry(
    index = 2,
    label = "2004LI/ZHA9474-9480:1",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.55e-15,"m^3/(mol*s)"),
        n = -0.58,
        Ea = (7.111,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Li, Q.S.", "Zhang, Y.", "Zhang, S.W."],
        title = u'Direct ab initio dynamics study on the rate constants and kinetics isotope effects of CH3O + H -&gt; CH2O + H2 reaction',
        journal = "J. Chem. Phys.",
        volume = "121",
        pages = """9474-9480""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/ZHA9474-9480:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010601
Pressure dependence: Rate constant is pressure independent

The authors calculated the potential energy surface at several levels of theory, up to UQCISD(T)/aug-cc-pVTZ//UQCISD/cc-pVDZ, and then used canonical variational transition-state theory to calculate the rate constants. At the highest level of theory employed the rate constants are within a factor of about 2.5 of the experimental values, while deviations are much larger (ca 10x at low and high T) at lower levels of theory. The kinetic isotope effect is also calculated.
""",
    history = [
        ("Thu Jul 12 23:16:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2004LI/ZHA9474-9480:1"""),
    ],
)

entry(
    index = 3,
    label = "1981TSU/HAS61:1",
    reactant1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (79.985,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1200,"K"),
        Tmax = (1800,"K"),
        Pmin = (20300,"Pa"),
        Pmax = (507000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsuboi, T.", "Hashimoto, K."],
        title = u'Shock Tube Study on Homogeneous Thermal Oxidation of Methanol',
        journal = "Combust. Flame",
        volume = "42",
        pages = """61""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/HAS61:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001361/rk00000001.xml
Bath gas: Ar
""",
    history = [
        ("Thu Jul 12 23:08:38 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/HAS61:1"""),
    ],
)

entry(
    index = 4,
    label = "1988NES/PAY4030:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.03e+09,"m^3/(mol*s)","+|-",1.5e+09),
        n = 0,
        Ea = (14.301,"kJ/mol","+|-",5.862),
        T0 = (1,"K"),
        Tmin = (215,"K"),
        Tmax = (250,"K"),
        Pmin = (133,"Pa"),
        Pmax = (133,"Pa"),
    ),
    reference = Article(
        authors = ["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."],
        title = u'Temperature dependence for the absolute rate constant for the reaction CH2OH + O2 \u2192\x92 HO2 + H2CO from 215 to 300 K',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4030""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
    history = [
        ("Thu Jul 12 23:08:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:1"""),
    ],
)

entry(
    index = 5,
    label = "1988NES/PAY4030:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (1.655,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (250,"K"),
        Tmax = (300,"K"),
        Pmin = (133,"Pa"),
        Pmax = (133,"Pa"),
    ),
    reference = Article(
        authors = ["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."],
        title = u'Temperature dependence for the absolute rate constant for the reaction CH2OH + O2 \u2192\x92 HO2 + H2CO from 215 to 300 K',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4030""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
    history = [
        ("Thu Jul 12 23:08:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:2"""),
    ],
)

entry(
    index = 6,
    label = "1988GRO/RIE4028:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e-12,"m^3/(mol*s)"),
        n = 5.94,
        Ea = (-18.957,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (700,"K"),
        Pmin = (131,"Pa"),
        Pmax = (259,"Pa"),
    ),
    reference = Article(
        authors = ["Grotheer, H.", "Riekert, G.", "Walter, D.", "Just, Th."],
        title = u'Non-arrhenius behavior of the reaction of hydroxymethyl radicals with molecular oxygen',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4028""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GRO/RIE4028:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
    history = [
        ("Thu Jul 12 23:08:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988GRO/RIE4028:1"""),
    ],
)

entry(
    index = 7,
    label = "1981VAN/VAN473:4",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (20.952,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1000,"K"),
        Tmax = (2000,"K"),
        Pmin = (5333,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Vandooren, J.", "Van Tiggelen, P.J."],
        title = u'Experimental Investigation of Methanol Oxidation in Flames: Mechanism and Rate Constants of Elementary Steps',
        journal = "Symp. Int. Combust. Proc.",
        volume = "18",
        pages = """473""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981VAN/VAN473:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
    history = [
        ("Thu Jul 12 23:08:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1981VAN/VAN473:4"""),
    ],
)

entry(
    index = 8,
    label = "1987OLS/OLS4160:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (25.11,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1000,"K"),
        Tmax = (2000,"K"),
        Pmin = (5333,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Olsson, J.M.", "Olsson, I.B.M.", "Andersson, L.L."],
        title = u'Lean premixed laminar methanol flames: A computational study',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """4160""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987OLS/OLS4160:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Uncertainty: 5.0
Bath gas: Ar
""",
    history = [
        ("Thu Jul 12 23:08:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987OLS/OLS4160:1"""),
    ],
)

entry(
    index = 9,
    label = "1991TSA221-273:91",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+06,"m^3/(mol*s)","*|/",3),
        n = -0.32,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:91",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010110
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010110/rk00000001.xml
Uncertainty: 3.0

===

M. Harper, 8/31/09:

No data available at the time. Recommended rate coefficient expression based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-to-addition ratio of 0.03. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and CH3+CH3-->adduct. (p. 257, Entry 47,16a)

NOTE: The Ea reported in the discussion is Ea/R=-132 Kelvin. However, in the table near the beginning of the review article (summarizing all reported data) and in the NIST online database (kinetics.nist.gov), the reported Ea/R=-66 Kelvin. MRH took the geometric mean of the allyl combination rxn (1.70E-11 * exp(132/T)) and methyl combination rxn (1.68E-9 * T^-0.64) to obtain 1.69E-11 * T^-0.32 * exp(66/T). Multiplying by 0.03 results in the recommended rate coefficient expression.
""",
    history = [
        ("Thu Jul 12 23:12:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:91"""),
    ],
)

entry(
    index = 10,
    label = "1951IVI/STE25:2",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.65e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (3.342,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (248,"K"),
        Tmax = (473,"K"),
        Pmin = (133,"Pa"),
        Pmax = (10700,"Pa"),
    ),
    reference = Article(
        authors = ["Ivin, K.J.", "Steacie, E.W.R."],
        title = u'The disproportionation and combination of ethyl radicals: The photolysis of mercury diethyl',
        journal = "Proc. R. Soc. London A",
        volume = "208",
        pages = """25""",
        year = "1951",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1951IVI/STE25:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010240
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010240/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
    history = [
        ("Thu Jul 12 23:13:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1951IVI/STE25:2"""),
    ],
)

entry(
    index = 11,
    label = "2003ORL/TYN4657-4689:3",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47100,"m^3/(mol*s)","+|-",22900),
        n = 0,
        Ea = (9.562,"kJ/mol","+|-",1.58),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (610,"K"),
    ),
    reference = Article(
        authors = ["Orlando, J.J.", "Tyndall, G.S.", "Wallington, T.J."],
        title = u'The atmospheric chemistry of alkoxy radicals',
        journal = "Chem. Rev.",
        volume = "103",
        pages = """4657-4689""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ORL/TYN4657-4689:3",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003ORL/TYN4657-4689:3"""),
    ],
)

entry(
    index = 12,
    label = "2001ATK/BAU1-56:129",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400,"m^3/(mol*s)"),
        n = 0,
        Ea = (8.98,"kJ/mol","+|-",2.494),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (610,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:129",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Pressure dependence: None reported
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:129"""),
    ],
)

entry(
    index = 13,
    label = "1997DEM/SAN1-266:269",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23500,"m^3/(mol*s)"),
        n = 0,
        Ea = (7.483,"kJ/mol","+|-",2.469),
        T0 = (1,"K"),
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:269",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:269"""),
    ],
)

entry(
    index = 14,
    label = "1997ATK/BAU521-1011:213",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400,"m^3/(mol*s)"),
        n = 0,
        Ea = (8.98,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (610,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:213",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:213"""),
    ],
)

entry(
    index = 15,
    label = "1997ATK99-111:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400,"m^3/(mol*s)"),
        n = 0,
        Ea = (8.98,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (600,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:1",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:1"""),
    ],
)

entry(
    index = 16,
    label = "1994DEM/SAN:251",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23500,"m^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (7.483,"kJ/mol","+|-",2.469),
        T0 = (1,"K"),
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.J.", "Molina, M.J."],
        title = u'Chemical Kinetic and Photochemical Data for Use in Stratospheric Modeling: Evaluation No. 11 of the NASA Panel for Data Evaluation',
        journal = "JPL Publication 94-26",
        pages = """1-2""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:251",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.5
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:251"""),
    ],
)

entry(
    index = 17,
    label = "1994BAU/COB847-1033:65",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21700,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (7.317,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:65",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:65"""),
    ],
)

entry(
    index = 18,
    label = "1992BAU/COB411-429:118",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (8.896,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:118",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:118"""),
    ],
)

entry(
    index = 19,
    label = "1992ATK/BAU1125-1568:181",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400,"m^3/(mol*s)"),
        n = 0,
        Ea = (8.98,"kJ/mol","+|-",2.511),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (610,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:181",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:181"""),
    ],
)

entry(
    index = 20,
    label = "1989ATK/BAU881-1097:108",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400,"m^3/(mol*s)","*|/",1.58),
        n = 0,
        Ea = (8.98,"kJ/mol","+|-",2.511),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (610,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:108",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.58
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:108"""),
    ],
)

entry(
    index = 21,
    label = "1988HEI177:5",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51300,"m^3/(mol*s)","*|/",1.35),
        n = 0,
        Ea = (10.726,"kJ/mol","+|-",1.073),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (628,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:5",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.35
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:5"""),
    ],
)

entry(
    index = 22,
    label = "1986TSA/HAM1087:151",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66200,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (10.892,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:151",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:151"""),
    ],
)

entry(
    index = 23,
    label = "1984WAR197C:130",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (30.015,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:130",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:130"""),
    ],
)

entry(
    index = 24,
    label = "1989BAL/POR483-488:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (235000,"m^3/(mol*s)"),
        n = 0,
        Ea = (15.049,"kJ/mol","+|-",4.515),
        T0 = (1,"K"),
        Tmin = (384,"K"),
        Tmax = (425,"K"),
        Pmin = (267,"Pa"),
        Pmax = (267,"Pa"),
    ),
    reference = Article(
        authors = ["Ballod, A.P.", "Poroikova, A.I.", "Titarchuk, T.A.", "Khabarov, V.N.488"],
        title = u'Determination of the rate constant of the reaction of methoxyl radicals with molecular oxygen',
        journal = "Kinet. Catal.",
        volume = "30",
        pages = """483-488""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BAL/POR483-488:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989BAL/POR483-488:2"""),
    ],
)

entry(
    index = 25,
    label = "1988ZAS/MUK244:6",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000,"m^3/(mol*s)"),
        n = 0,
        Ea = (10.892,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (700,"K"),
        Tmax = (900,"K"),
        Pmin = (13300,"Pa"),
        Pmax = (45600,"Pa"),
    ),
    reference = Article(
        authors = ["Zaslonko, I.S.", "Mukoseev, Yu.K.", "Tyurin, A.N."],
        title = u'Reactions of CH3O radicals in shock waves',
        journal = "Kinet. Catal.",
        volume = "29",
        pages = """244""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988ZAS/MUK244:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Chemiluminescence
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988ZAS/MUK244:6"""),
    ],
)

entry(
    index = 26,
    label = "1987ZEL403-407:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33100,"m^3/(mol*s)","+|-",12000),
        n = 0,
        Ea = (8.314,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (425,"K"),
        Pmin = (9999,"Pa"),
        Pmax = (9999,"Pa"),
    ),
    reference = Article(
        authors = ["Zellner, R."],
        title = u'Recent advances in free radical kinetics of oxygenated hydrocarbon radicals',
        journal = "J. Chim. Phys.",
        volume = "84",
        pages = """403-407""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987ZEL403-407:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987ZEL403-407:2"""),
    ],
)

entry(
    index = 27,
    label = "1987WAN/OLD4653:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-25,"m^3/(mol*s)","+|-",1.13e-25),
        n = (9.5,"","+|-",0.67),
        Ea = (-23.031,"kJ/mol","+|-",2.76),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (973,"K"),
        Pmin = (9999,"Pa"),
        Pmax = (9999,"Pa"),
    ),
    reference = Article(
        authors = ["Wantuck, P.J.", "Oldenborg, R.C.", "Baughcum, S.L.", "Winn, K.R."],
        title = u'Removal rate constant measurements for CH3O by O2 over the 298-973 K range',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """4653""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987WAN/OLD4653:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987WAN/OLD4653:1"""),
    ],
)

entry(
    index = 28,
    label = "1985LOR/RHA341:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33100,"m^3/(mol*s)","+|-",12000),
        n = 0,
        Ea = (8.314,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (450,"K"),
        Pmin = (9999,"Pa"),
        Pmax = (9999,"Pa"),
    ),
    reference = Article(
        authors = ["Lorenz, K.", "Rhasa, D.", "Zellner, R.", "Fritz, B."],
        title = u'Laser photolysis - LIF kinetic studies of the reactions of CH3O and CH2CHO with O2 between 300 and 500 K',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "89",
        pages = """341""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985LOR/RHA341:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985LOR/RHA341:1"""),
    ],
)

entry(
    index = 29,
    label = "1982GUT/SAN66:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (10.892,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (413,"K"),
        Tmax = (628,"K"),
        Pmin = (5333,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Gutman, D.", "Sanders, N.", "Butler, J.E."],
        title = u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """66""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:2"""),
    ],
)

entry(
    index = 30,
    label = "1980COX/DER149:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75900,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (11.225,"kJ/mol","+|-",2.81),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (450,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Cox, R.A.", "Derwent, R.G.", "Kearsey, S.V.", "Batt, L.", "Partick, K.G."],
        title = u'Photolysis of Methyl Nitrite: Kinetics of the Reaction of the Methoxy Radical with O2',
        journal = "J. Photochem.",
        volume = "13",
        pages = """149""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980COX/DER149:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1980COX/DER149:1"""),
    ],
)

entry(
    index = 31,
    label = "1979BAT/ROB1045:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (20.121,"kJ/mol","+|-",4.623),
        T0 = (1,"K"),
        Tmin = (383,"K"),
        Tmax = (433,"K"),
        Pmin = (66900,"Pa"),
        Pmax = (67600,"Pa"),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Reaction of Methoxy Radicals with Oxygen. I. Using Dimethyl Peroxide as a Thermal Source of Methoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1045""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/ROB1045:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/ROB1045:1"""),
    ],
)

entry(
    index = 32,
    label = "1979BAT/RAT1183:3",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (18.791,"kJ/mol","+|-",4.523),
        T0 = (1,"K"),
        Tmin = (383,"K"),
        Tmax = (433,"K"),
        Pmin = (93300,"Pa"),
        Pmax = (93300,"Pa"),
    ),
    reference = Article(
        authors = ["Batt, L.", "Rattray, G.N."],
        title = u'The Reaction of Methoxy Radicals with Nitric Oxide and Nitrogen Dioxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1183""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/RAT1183:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/RAT1183:3"""),
    ],
)

entry(
    index = 33,
    label = "1977BAR/BEN31:3",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (316000,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (16.712,"kJ/mol","+|-",11.723),
        T0 = (1,"K"),
        Tmin = (396,"K"),
        Tmax = (442,"K"),
        Pmin = (93600,"Pa"),
        Pmax = (93600,"Pa"),
    ),
    reference = Article(
        authors = ["Barker, J.R.", "Benson, S.W.", "Golden, D.M."],
        title = u'The Decomposition of Dimethyl Peroxide and the Rate Constant for CH3O + O2 \u2192\x92 CH2O +HO2',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """31""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAR/BEN31:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010588/rk00000010.xml
Uncertainty: 3.1600001
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1977BAR/BEN31:3"""),
    ],
)

entry(
    index = 34,
    label = "1980MOS/POL315:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *4 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+15,"m^3/(mol*s)"),
        n = 0,
        Ea = (136.357,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (593,"K"),
        Tmax = (626,"K"),
        Pmin = (81200,"Pa"),
        Pmax = (81200,"Pa"),
    ),
    reference = Article(
        authors = ["Moshkina, R.I.", "Polyak, S.S.", "Sokolova, N.A.", "Masterovoi, I.F.", "Nalbandyan, A.B."],
        title = u'Study of the ethane oxidation reaction by the kinetic tracer method',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """315""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980MOS/POL315:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: O2
""",
    history = [
        ("Thu Jul 12 23:14:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1980MOS/POL315:2"""),
    ],
)

entry(
    index = 35,
    label = "1986TSA/HAM1087:43",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (4.82e+08,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (299.321,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:43",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Uncertainty: 5.0
""",
    history = [
        ("Thu Jul 12 23:18:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:43"""),
    ],
)

entry(
    index = 36,
    label = "1983AYR/BAC83-104:1",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.86e+08,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (268.557,"kJ/mol","+|-",8.057),
        T0 = (1,"K"),
        Tmin = (748,"K"),
        Tmax = (819,"K"),
        Pmin = (13300,"Pa"),
        Pmax = (40000,"Pa"),
    ),
    reference = Article(
        authors = ["Ayranci, G.", "Back, M.H."],
        title = u'Kinetics of the reaction: 2C2H4 \u2192\x92 C2H5 + C2H3. Heat of formation of the vinyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """83-104""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983AYR/BAC83-104:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Uncertainty: 5.0
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:18:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1983AYR/BAC83-104:1"""),
    ],
)

entry(
    index = 37,
    label = "1981AYR/BAC897:1",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+10,"m^3/(mol*s)"),
        n = 0,
        Ea = (280.198,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (700,"K"),
        Tmax = (773,"K"),
        Pmin = (9999,"Pa"),
        Pmax = (53300,"Pa"),
    ),
    reference = Article(
        authors = ["Ayranci, G.", "Back, M.H."],
        title = u'Kinetics of the Bimolecular Initiation Process in the Thermal Reactions of Ethylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """897""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981AYR/BAC897:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:18:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1981AYR/BAC897:1"""),
    ],
)

entry(
    index = 38,
    label = "1970BAC409-418:1",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+08,"m^3/(mol*s)"),
        n = 0,
        Ea = (267.726,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (800,"K"),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011408/rk00000003.xml
""",
    history = [
        ("Thu Jul 12 23:18:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:1"""),
    ],
)

entry(
    index = 39,
    label = "1992BAU/COB411-429:209",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (102000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-9.146,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (1200,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:209",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:209"""),
    ],
)

entry(
    index = 40,
    label = "1989ATK/BAU881-1097:221",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (843000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (16.213,"kJ/mol","+|-",5.03),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:221",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:221"""),
    ],
)

entry(
    index = 41,
    label = "1986TSA/HAM1087:249",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (843000,"m^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (16.213,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:249",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 1.5
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:249"""),
    ],
)

entry(
    index = 42,
    label = "1984WAR197C:187",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+06,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (20.869,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (700,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:187",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 3.1600001
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:187"""),
    ],
)

entry(
    index = 43,
    label = "1993DOB/BEN8798-8809:5",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.55,"m^3/(mol*s)","+|-",2.3),
        n = 0,
        Ea = (-21.202,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (243,"K"),
        Tmax = (368,"K"),
    ),
    reference = Article(
        authors = ["Dobis, O.", "Benson, S.W."],
        title = u'Reaction of the ethyl radical with oxygen at millitorr pressures at 243-368 K and a study of the Cl + HO2, ethyl + HO2, and HO2 + HO2 reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "115",
        pages = """8798-8809""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993DOB/BEN8798-8809:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1993DOB/BEN8798-8809:5"""),
    ],
)

entry(
    index = 44,
    label = "1990BOZ/DEA3313-3317:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.56e+13,"m^3/(mol*s)"),
        n = -2.77,
        Ea = (8.273,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (250,"K"),
        Tmax = (1200,"K"),
        Pmin = (93.33,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Bozzelli, J.W.", "Dean, A.M."],
        title = u'Chemical activation analysis of the reaction of C2H5 with O2',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """3313-3317""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BOZ/DEA3313-3317:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: N2
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990BOZ/DEA3313-3317:2"""),
    ],
)

entry(
    index = 45,
    label = "1987MCA/WAL1509:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (11200,"m^3/(mol*s)","*|/",1.51),
        n = 0,
        Ea = (-6.302,"kJ/mol","+|-",3.525),
        T0 = (1,"K"),
        Tmin = (593,"K"),
        Tmax = (753,"K"),
        Pmin = (7999,"Pa"),
        Pmax = (7999,"Pa"),
    ),
    reference = Article(
        authors = ["McAdam, K.G.", "Walker, R.W."],
        title = u'Arrhenius Parameters for the reaction C2H5 + O2 \u2192\x92 C2H4 + HO2',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """1509""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987MCA/WAL1509:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 1.51
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987MCA/WAL1509:2"""),
    ],
)

entry(
    index = 46,
    label = "1971BAK/BAL291:23",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (217000,"m^3/(mol*s)","*|/",1.38),
        n = 0,
        Ea = (5.77,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (713,"K"),
        Tmax = (896,"K"),
    ),
    reference = Article(
        authors = ["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."],
        title = u'The Use of the H2 + O2 Reaction in Determining the Velocity Constants of Elementary Reactions in Hydrocarbon Oxidation',
        journal = "Symp. Int. Combust. Proc.",
        volume = "13",
        pages = """291""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971BAK/BAL291:23",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000007.xml
Uncertainty: 1.38
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971BAK/BAL291:23"""),
    ],
)

entry(
    index = 47,
    label = "2003DES/KLI4415-4427:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.11e+10,"m^3/(mol*s)"),
        n = -1.87,
        Ea = (5.878,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:2"""),
        ("Wed Jul 18 13:27:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Removed invalid pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp0221946"""),
    ],
)

entry(
    index = 48,
    label = "1980BAL/PIC2374:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (851000,"m^3/(mol*s)"),
        n = 0,
        Ea = (16.213,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (673,"K"),
        Tmax = (813,"K"),
        Pmin = (7999,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Pickering, I.A.", "Walker, R.W."],
        title = u'Reactions of Ethyl Radicals with Oxygen over the Temperature Range 400-540oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """2374""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BAL/PIC2374:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: N2
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1980BAL/PIC2374:1"""),
    ],
)

entry(
    index = 49,
    label = "1971COO/WIL757:4",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (20.952,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1400,"K"),
        Tmax = (1800,"K"),
        Pmin = (26700,"Pa"),
        Pmax = (40000,"Pa"),
    ),
    reference = Article(
        authors = ["Cooke, D.F.", "Williams, A."],
        title = u'Shock-tube studies of the ignition and combustion of ethane and slightly rich methane mixtures with oxygen',
        journal = "Symp. Int. Combust. Proc.",
        volume = "13",
        pages = """757""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COO/WIL757:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: Ar
""",
    history = [
        ("Thu Jul 12 23:19:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971COO/WIL757:4"""),
    ],
)

entry(
    index = 50,
    label = "1986TSA/HAM1087:209",
    reactant1 = 
"""
1 *1 O 1
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *2 C 0 {1,D} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *2 C 0 {1,D} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:209",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00017303
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017303/rk00000001.xml
Uncertainty: 3.0
""",
    history = [
        ("Wed Jul 25 13:45:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:209"""),
    ],
)

entry(
    index = 51,
    label = "1990TSA1-68:73",
    reactant1 = 
"""
1 *2 C 0 {4,S} {5,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.26e+07,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-2.494,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:73",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009800
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009800/rk00000004.xml
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:10:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:73"""),
    ],
)

entry(
    index = 52,
    label = "1991TSA221-273:111",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (964000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:111",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010098
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010098/rk00000003.xml
Uncertainty: 2.0

===

M. Harper, 8/31/09: The recommended rate expression is derived from the experimentally-determined disproportionation-to-addition ratio of 0.047 (James and Troughton) and the addition rate rule (C2H5+C3H5-->adduct) calculated using the geometric mean rule of the rxns C2H5+C2H5-->adduct and C3H5+C3H5-->adduct. (p. 259, Entry 47,17a)
""",
    history = [
        ("Thu Jul 12 23:11:31 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:111"""),
    ],
)

entry(
    index = 53,
    label = "1985KOR/TRU1068:1",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.35e+08,"m^3/(mol*s)","+|-",3.7e+07),
        n = 0,
        Ea = (164.627,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1070,"K"),
        Tmax = (1130,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Korzun, N.V.", "Trushkova, L.V."],
        title = u'Kinetic parameters of the reaction C2H6 + C3H4 \u2192\x92 C2H5 + C3H5',
        journal = "Kinet. Catal.",
        volume = "26",
        pages = """1068""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985KOR/TRU1068:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010098
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:11:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985KOR/TRU1068:1"""),
    ],
)

entry(
    index = 54,
    label = "1991TSA221-273:112",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.59e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:112",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010099/rk00000004.xml
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:11:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:112"""),
    ],
)

entry(
    index = 55,
    label = "1991TSA221-273:6",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.78e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (216.176,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:6",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010099/rk00000004.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:11:42 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:6"""),
    ],
)

entry(
    index = 56,
    label = "1970BAC409-418:2",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+08,"m^3/(mol*s)"),
        n = 0,
        Ea = (206.199,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (800,"K"),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
""",
    history = [
        ("Thu Jul 12 23:11:42 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:2"""),
    ],
)

entry(
    index = 57,
    label = "2005LEE/BOZ1015-1022:3",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0206,"m^3/(mol*s)"),
        n = 2.19,
        Ea = (73.597,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (2000,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Lee, J.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis of the allyl radical with O2 reaction system',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1015-1022""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005LEE/BOZ1015-1022:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010133

Reaction potential energy surface was studied using quantum chemistry, product pathways were analyzed, and rate constants were calculated using QRRK / master equation method. Rate constants were calculated for a wide range of temperatures; Arrhenius expressions for the pressure of 1 atm are given in a table in the Supplementary Data (online).
""",
    history = [
        ("Thu Jul 12 23:12:37 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2005LEE/BOZ1015-1022:3"""),
    ],
)

entry(
    index = 58,
    label = "1991TSA221-273:7",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.22e+09,"m^3/(mol*s)","*|/",3),
        n = -0.65,
        Ea = (308.467,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:7",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010195
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:12:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:7"""),
    ],
)

entry(
    index = 59,
    label = "1970BAC409-418:3",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (264.4,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (800,"K"),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010195
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010195/rk00000004.xml
""",
    history = [
        ("Thu Jul 12 23:12:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:3"""),
    ],
)

entry(
    index = 60,
    label = "1984WAR197C:120",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+06,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (12.472,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:120",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010209/rk00000003.xml
Uncertainty: 3.1600001
""",
    history = [
        ("Thu Jul 12 23:13:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:120"""),
    ],
)

entry(
    index = 61,
    label = "1988GUL/WAL401:2",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (27500,"m^3/(mol*s)","*|/",1.78),
        n = 0,
        Ea = (-8.98,"kJ/mol","+|-",5.039),
        T0 = (1,"K"),
        Tmin = (653,"K"),
        Tmax = (773,"K"),
        Pmin = (4800,"Pa"),
        Pmax = (5733,"Pa"),
    ),
    reference = Article(
        authors = ["Gulati, S.K.", "Walker, R.W."],
        title = u'Arrhenius parameters for the reaction i-C3H7 + O2 \u2192\x92 C3H6 + HO2',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "84",
        pages = """401""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GUL/WAL401:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
Uncertainty: 1.78
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:13:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988GUL/WAL401:2"""),
    ],
)

entry(
    index = 62,
    label = "2003DES/KLI4415-4427:5",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (6.7e+14,"m^3/(mol*s)"),
        n = -3.02,
        Ea = (10.476,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Thu Jul 12 23:13:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:5"""),
        ("Wed Jul 18 13:27:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Removed invalid pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp0221946"""),
    ],
)

entry(
    index = 63,
    label = "1991TSA221-273:8",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (315.95,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:8",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010524
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010524/rk00000002.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:13:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:8"""),
    ],
)

entry(
    index = 64,
    label = "1984WAR197C:127",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+06,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (21.036,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:127",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010543
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010543/rk00000007.xml
Uncertainty: 3.1600001
""",
    history = [
        ("Thu Jul 12 23:13:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:127"""),
    ],
)

entry(
    index = 65,
    label = "2003DES/KLI4415-4427:8",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.7e+10,"m^3/(mol*s)"),
        n = -1.63,
        Ea = (14.301,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010543
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Thu Jul 12 23:13:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:8"""),
        ("Wed Jul 18 13:27:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Removed invalid pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp0221946"""),
    ],
)

entry(
    index = 66,
    label = "2001ATK/BAU1-56:130",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol","+|-",2.494),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (425,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:130",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Pressure dependence: None reported
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:130"""),
    ],
)

entry(
    index = 67,
    label = "1997DEM/SAN1-266:275",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (37900,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol","+|-",1.646),
        T0 = (1,"K"),
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:275",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:275"""),
    ],
)

entry(
    index = 68,
    label = "1997ATK/BAU521-1011:219",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (425,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:219",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:219"""),
    ],
)

entry(
    index = 69,
    label = "1997ATK99-111:2",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (600,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:2"""),
    ],
)

entry(
    index = 70,
    label = "1994DEM/SAN:257",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (37900,"m^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (4.573,"kJ/mol","+|-",1.646),
        T0 = (1,"K"),
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.J.", "Molina, M.J."],
        title = u'Chemical Kinetic and Photochemical Data for Use in Stratospheric Modeling: Evaluation No. 11 of the NASA Panel for Data Evaluation',
        journal = "JPL Publication 94-26",
        pages = """1-2""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:257",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 1.5
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:257"""),
    ],
)

entry(
    index = 71,
    label = "1992BAU/COB411-429:123",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (60300,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (6.901,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:123",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 3.1600001
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:123"""),
    ],
)

entry(
    index = 72,
    label = "1992ATK/BAU1125-1568:187",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol","+|-",2.519),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (425,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:187",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:187"""),
    ],
)

entry(
    index = 73,
    label = "1988HEI177:11",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (97700,"m^3/(mol*s)","*|/",1.55),
        n = 0,
        Ea = (6.652,"kJ/mol","+|-",1.064),
        T0 = (1,"K"),
        Tmin = (225,"K"),
        Tmax = (425,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:11",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 1.55
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:11"""),
    ],
)

entry(
    index = 74,
    label = "1990HAR/KAR639-645:1",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (42800,"m^3/(mol*s)","+|-",4300),
        n = 0,
        Ea = (4.59,"kJ/mol","+|-",0.55),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (411,"K"),
        Pmin = (3453,"Pa"),
        Pmax = (3453,"Pa"),
    ),
    reference = Article(
        authors = ["Hartmann, D.", "Karthauser, J.", "Sawerysyn, J.P.", "Zellner, R."],
        title = u'Kinetics and HO2 product yield of the reaction C2H5O + O2 between 295 and 411 K',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "94",
        pages = """639-645""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990HAR/KAR639-645:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990HAR/KAR639-645:1"""),
    ],
)

entry(
    index = 75,
    label = "1985ZAB/HEI455:2",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (181000,"m^3/(mol*s)","+|-",60000),
        n = 0,
        Ea = (7.683,"kJ/mol","+|-",0.768),
        T0 = (1,"K"),
        Tmin = (225,"K"),
        Tmax = (393,"K"),
        Pmin = (533,"Pa"),
        Pmax = (48100,"Pa"),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'Reactions of alkoxy radicals with O2. I. C2H5O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """455""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI455:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI455:2"""),
    ],
)

entry(
    index = 76,
    label = "1982GUT/SAN66:3",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (17200,"m^3/(mol*s)"),
        n = 0,
        Ea = (3.143,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (353,"K"),
        Pmin = (5333,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Gutman, D.", "Sanders, N.", "Butler, J.E."],
        title = u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """66""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010641/rk00000002.xml
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:17:03 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:3"""),
    ],
)

entry(
    index = 77,
    label = "1982NAT/BHA834:4",
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (23.281,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1300,"K"),
        Tmax = (1700,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (203000,"Pa"),
    ),
    reference = Article(
        authors = ["Natarajan, K.", "Bhaskaran, K.A."],
        title = u'An Experimental and Analytical Investigation of High Temperature Ignition of Ethanol',
        journal = "Proc. Int. Symp. Shock Tubes Waves",
        volume = "13",
        pages = """834""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982NAT/BHA834:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011080
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011080/rk00000001.xml
Bath gas: Ar
""",
    history = [
        ("Thu Jul 12 23:18:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982NAT/BHA834:4"""),
    ],
)

entry(
    index = 78,
    label = "1991TSA221-273:108",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (56.705,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:108",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010133
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010133/rk00000002.xml
Rate constant is an upper limit.

===

M. Harper, 8/31/09: The author states that there is uncertainty whether this rxn is appreciable at high temperatures. There were conflicting results published regarding the significance above 461K (Morgan et al. and Slagle and Gutman). The author thus decides to place an upper limit on the rate coefficient of 2E-12 * exp(-6820/T) cm3/molecule/s. The author further notes that this upper limit assumes no contribution from a complex rearrangement of the adduct. Finally, the author notes that this rxn should not be significant in combustion situations. (p. 251, Entry 47,3b)
""",
    history = [
        ("Tue Jul 24 17:09:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:108"""),
    ],
)

entry(
    index = 79,
    label = "1979EVA/WAL1458:2",
    reactant1 = 
"""
1 *2 C 0 {4,S} {5,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    degeneracy = 18,
    kinetics = Arrhenius(
        A = (800000,"m^3/(mol*s)"),
        n = 0,
        Ea = (9.063,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (713,"K"),
        Tmax = (813,"K"),
        Pmin = (66700,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Evans, G.A.", "Walker, R.W."],
        title = u'Reaction of t-Butyl Radicals with Hydrogen and with Oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "75",
        pages = """1458""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979EVA/WAL1458:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009826
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009826/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (9.977) found and ignored
""",
    history = [
        ("Thu Jul 12 23:10:31 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1979EVA/WAL1458:2"""),
    ],
)

entry(
    index = 80,
    label = "1991TSA221-273:78",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300,"m^3/(mol*s)","*|/",2.5),
        n = 0,
        Ea = (-1.098,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:78",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010092
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010092/rk00000002.xml
Uncertainty: 2.5

===

M. Harper, 8/31/09: The recommended rate expression is derived from the experimentally-determined disproportionation-to-addition ratio of 0.008 (James and Kambanis) and the addition rate rule (C3H5+C3H5-->adduct) calculated based on the results of Tulloch et al. (p. 271-272, Entry 47,47b)
""",
    history = [
        ("Thu Jul 12 23:10:36 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:78"""),
    ],
)

entry(
    index = 81,
    label = "1996BAR/MAR829-847:8",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33900,"m^3/(mol*s)"),
        n = 0,
        Ea = (39.327,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
        Pmin = (4000,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010092
Bath gas: CH3CH=CH2
""",
    history = [
        ("Thu Jul 12 23:10:36 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:8"""),
    ],
)

entry(
    index = 82,
    label = "1991TSA221-273:80",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 1 {1,S} {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+06,"m^3/(mol*s)","*|/",3),
        n = -0.35,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:80",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010094
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010094/rk00000001.xml
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Recommended rate coefficient expression based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values for "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-to-addition ratio of 0.04. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and iC3H7+iC3H7-->adduct. (p. 268, Entry 47,42b)
""",
    history = [
        ("Thu Jul 12 23:10:46 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:80"""),
    ],
)

entry(
    index = 83,
    label = "1991TSA221-273:81",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.29e+07,"m^3/(mol*s)","*|/",3),
        n = -0.35,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:81",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010095/rk00000002.xml
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Recommended rate coefficient expression based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values for "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-to-addition ratio of 0.2. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and iC3H7+iC3H7-->adduct. (p. 268, Entry 47,42a)
""",
    history = [
        ("Thu Jul 12 23:10:50 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:81"""),
    ],
)

entry(
    index = 84,
    label = "1996BAR/MAR829-847:9",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (501000,"m^3/(mol*s)"),
        n = 0,
        Ea = (19.622,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
        Pmin = (4000,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
""",
    history = [
        ("Thu Jul 12 23:10:50 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:9"""),
    ],
)

entry(
    index = 85,
    label = "1991TSA221-273:21",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.88e+07,"m^3/(mol*s)","*|/",2.5),
        n = 0,
        Ea = (218.671,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:21",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010095/rk00000002.xml
Uncertainty: 2.5
""",
    history = [
        ("Thu Jul 12 23:10:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:21"""),
    ],
)

entry(
    index = 86,
    label = "1973SIM/BAC2934:1",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (182.087,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (743,"K"),
        Tmax = (803,"K"),
        Pmin = (667,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Simon, M.", "Back, M.H."],
        title = u'The Kinetics of the Reaction 2C3H6 \u2192\x92 C3H5 + C3H7',
        journal = "Can. J. Chem.",
        volume = "51",
        pages = """2934""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973SIM/BAC2934:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:10:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1973SIM/BAC2934:1"""),
    ],
)

entry(
    index = 87,
    label = "1996BAR/MAR829-847:5",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.57e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (236.962,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
        Pmin = (4000,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
""",
    history = [
        ("Thu Jul 12 23:10:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:5"""),
    ],
)

entry(
    index = 88,
    label = "1970BAC409-418:4",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.32e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (202.873,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (800,"K"),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
""",
    history = [
        ("Thu Jul 12 23:10:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:4"""),
    ],
)

entry(
    index = 89,
    label = "1991TSA221-273:87",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:87",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010105
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010105/rk00000001.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:11:54 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:87"""),
    ],
)

entry(
    index = 90,
    label = "1991TSA221-273:88",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.45e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:88",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010106/rk00000001.xml
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Recommended rate coefficient expression based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values for "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-to-addition ratio of 0.07. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and nC3H7+nC3H7-->adduct. (p. 268, Entry 47,41a)
""",
    history = [
        ("Thu Jul 12 23:11:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:88"""),
    ],
)

entry(
    index = 91,
    label = "1996BAR/MAR829-847:10",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (275000,"m^3/(mol*s)"),
        n = 0,
        Ea = (19.622,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
        Pmin = (4000,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
Bath gas: CH3CH=CH2
""",
    history = [
        ("Thu Jul 12 23:11:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:10"""),
    ],
)

entry(
    index = 92,
    label = "1991TSA221-273:22",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.53e+08,"m^3/(mol*s)","*|/",2.5),
        n = 0,
        Ea = (231.142,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:22",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010106/rk00000001.xml
Uncertainty: 2.5
""",
    history = [
        ("Thu Jul 12 23:12:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:22"""),
    ],
)

entry(
    index = 93,
    label = "1996BAR/MAR829-847:6",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.89e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (249.434,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
        Pmin = (4000,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
Bath gas: CH3CH=CH2
""",
    history = [
        ("Thu Jul 12 23:12:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:6"""),
    ],
)

entry(
    index = 94,
    label = "2001ATK/BAU1-56:132",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8430,"m^3/(mol*s)"),
        n = 0,
        Ea = (1.746,"kJ/mol","+|-",1.663),
        T0 = (1,"K"),
        Tmin = (210,"K"),
        Tmax = (390,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:132",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Pressure dependence: None reported
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:132"""),
    ],
)

entry(
    index = 95,
    label = "1997ATK/BAU521-1011:289",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040,"m^3/(mol*s)"),
        n = 0,
        Ea = (1.663,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (390,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:289",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:289"""),
    ],
)

entry(
    index = 96,
    label = "1997ATK99-111:3",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040,"m^3/(mol*s)"),
        n = 0,
        Ea = (1.663,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (600,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:3",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:3"""),
    ],
)

entry(
    index = 97,
    label = "1992ATK/BAU1125-1568:275",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040,"m^3/(mol*s)"),
        n = 0,
        Ea = (1.663,"kJ/mol","+|-",1.663),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (390,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:275",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:275"""),
    ],
)

entry(
    index = 98,
    label = "1989ATK/BAU881-1097:193",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (1.663,"kJ/mol","+|-",1.663),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (390,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:193",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Uncertainty: 2.0
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:193"""),
    ],
)

entry(
    index = 99,
    label = "1988HEI177:17",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (49000,"m^3/(mol*s)","*|/",1.55),
        n = 0,
        Ea = (6.652,"kJ/mol","+|-",1.064),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (383,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:17",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Uncertainty: 1.55
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:17"""),
    ],
)

entry(
    index = 100,
    label = "1985BAL/NEL323:5",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 O 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9100,"m^3/(mol*s)","+|-",4200),
        n = 0,
        Ea = (1.63,"kJ/mol","+|-",1.172),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (383,"K"),
        Pmin = (133,"Pa"),
        Pmax = (6666,"Pa"),
    ),
    reference = Article(
        authors = ["Balla, R.J.", "Nelson, H.H.", "McDonald, J.R."],
        title = u'Kinetics of the reactions of isopropoxy radicals with NO, NO2, and O2',
        journal = "Chem. Phys.",
        volume = "99",
        pages = """323""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985BAL/NEL323:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012573/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Thu Jul 12 23:18:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985BAL/NEL323:5"""),
    ],
)

entry(
    index = 101,
    label = "1978BAK/BAL2229:6",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.7e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (26.606,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (313,"K"),
        Tmax = (753,"K"),
        Pmin = (66700,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."],
        title = u'Addition of i-Butane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480o C',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """2229""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAK/BAL2229:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012779
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012779/rk00000003.xml
Bath gas: N2
""",
    history = [
        ("Thu Jul 12 23:19:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1978BAK/BAL2229:6"""),
    ],
)

entry(
    index = 102,
    label = "2001ATK/BAU1-56:131",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,S} {5,S}
4 *3 O 1 {3,S}
5 *4 H 0 {3,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8430,"m^3/(mol*s)"),
        n = 0,
        Ea = (0.915,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (220,"K"),
        Tmax = (310,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:131",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
Pressure dependence: None reported
Note: Invalid activation energy uncertainty (4.157) found and ignored
""",
    history = [
        ("Thu Jul 12 23:20:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:131"""),
    ],
)

entry(
    index = 103,
    label = "1988HEI177:19",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,S} {5,S}
4 *3 O 1 {3,S}
5 *4 H 0 {3,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000,"m^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (8.281,"kJ/mol","+|-",0.745),
        T0 = (1,"K"),
        Tmin = (250,"K"),
        Tmax = (361,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:19",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
Uncertainty: 1.3
""",
    history = [
        ("Thu Jul 12 23:20:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:19"""),
    ],
)

entry(
    index = 104,
    label = "1985ZAB/HEI477:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,S} {5,S}
4 *3 O 1 {3,S}
5 *4 H 0 {3,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,D}
4 *3 O 0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (175000,"m^3/(mol*s)","+|-",100000),
        n = 0,
        Ea = (7.308,"kJ/mol","+|-",0.948),
        T0 = (1,"K"),
        Tmin = (247,"K"),
        Tmax = (361,"K"),
        Pmin = (20000,"Pa"),
        Pmax = (20000,"Pa"),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'The reactions of alkoxy radicals with O2. II. n-C3H7O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """477""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI477:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013958/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:20:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI477:2"""),
    ],
)

entry(
    index = 105,
    label = "1978ARR/KIR3016:1",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 1 {1,S} {2,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.01e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (-0.208,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (301,"K"),
        Tmax = (424,"K"),
    ),
    reference = Article(
        authors = ["Arrowsmith, P.", "Kirsch, L.J."],
        title = u'Mutual Reaction of Isopropyl Radicals',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """3016""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978ARR/KIR3016:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010168/rk00000013.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Tue Jul 24 17:13:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1978ARR/KIR3016:1"""),
    ],
)

entry(
    index = 106,
    label = "1991TSA221-273:74",
    reactant1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *1 C 1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+07,"m^3/(mol*s)","*|/",3),
        n = -0.75,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:74",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009781
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009781/rk00000001.xml
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Recommended rate coefficient expression based on "allyl and alkyl radicals behaving in similar fashion" (possibly referencing Gibian M.J. and Corley R.C.); this leads to disproportionation-to-addition ratio of 0.04. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and tC4H9+tC4H9-->adduct. (p. 269, Entry 47,44b)
""",
    history = [
        ("Thu Jul 12 23:10:04 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:74"""),
    ],
)

entry(
    index = 107,
    label = "1991TSA221-273:75",
    reactant1 = 
"""
1 *2 C 0 {4,S} {5,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (4.33e+08,"m^3/(mol*s)","*|/",3),
        n = -0.75,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:75",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009782
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009782/rk00000001.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:10:09 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:75"""),
    ],
)

entry(
    index = 108,
    label = "1991TSA221-273:103",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *1 C 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (783000,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:103",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010124
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010124/rk00000001.xml
Uncertainty: 3.0
""",
    history = [
        ("Thu Jul 12 23:12:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:103"""),
    ],
)

entry(
    index = 109,
    label = "1991TSA221-273:104",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (783000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-0.549,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:104",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010125
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010125/rk00000001.xml
Uncertainty: 2.0

===

M. Harper, 8/31/09: No data available at the time. Recommended rate coefficient expression based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-to-addition ratio of 0.04. The addition rate expression was derived using the geometric mean rule for the rxns C3H5+C3H5-->adduct and iC4H9+iC4H9-->adduct. (p. 270, Entry 47,45a)
""",
    history = [
        ("Thu Jul 12 23:12:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:104"""),
    ],
)

entry(
    index = 110,
    label = "2001ATK/BAU1-56:133",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,S} {6,S}
5 *3 O 1 {4,S}
6 *4 H 0 {4,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,D}
5 *3 O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100,"m^3/(mol*s)"),
        n = 0,
        Ea = (4.573,"kJ/mol","+|-",4.157),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (400,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:133",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
Pressure dependence: None reported
""",
    history = [
        ("Thu Jul 12 23:20:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:133"""),
    ],
)

entry(
    index = 111,
    label = "1988HEI177:20",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,S} {6,S}
5 *3 O 1 {4,S}
6 *4 H 0 {4,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,D}
5 *3 O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000,"m^3/(mol*s)","*|/",1.32),
        n = 0,
        Ea = (8.281,"kJ/mol","+|-",0.745),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (361,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:20",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
Uncertainty: 1.3200001
""",
    history = [
        ("Thu Jul 12 23:20:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:20"""),
    ],
)

entry(
    index = 112,
    label = "1987MOR/HEI2641:1",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,S} {6,S}
5 *3 O 1 {4,S}
6 *4 H 0 {4,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,D}
5 *3 O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (450000,"m^3/(mol*s)"),
        n = 0,
        Ea = (9.811,"kJ/mol","+|-",1.472),
        T0 = (1,"K"),
        Tmin = (265,"K"),
        Tmax = (393,"K"),
        Pmin = (53300,"Pa"),
        Pmax = (53300,"Pa"),
    ),
    reference = Article(
        authors = ["Morabito, P.", "Heicklen, J."],
        title = u'The reactions of alkoxyl radicals with O2. IV. n-C4H9O radicals',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "60",
        pages = """2641""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987MOR/HEI2641:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013972/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:20:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987MOR/HEI2641:1"""),
    ],
)

entry(
    index = 113,
    label = "1988HEI177:21",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 C 0 {1,S} {5,S} {6,S}
5 *3 O 1 {4,S}
6 *4 H 0 {4,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 C 0 {1,S} {5,D}
5 *3 O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000,"m^3/(mol*s)","*|/",1.32),
        n = 0,
        Ea = (8.281,"kJ/mol","+|-",0.745),
        T0 = (1,"K"),
        Tmin = (265,"K"),
        Tmax = (361,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:21",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013994
Uncertainty: 1.3200001
""",
    history = [
        ("Thu Jul 12 23:21:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:21"""),
    ],
)

entry(
    index = 114,
    label = "1985ZAB/HEI503:2",
    reactant1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 C 0 {1,S} {5,S} {6,S}
5 *3 O 1 {4,S}
6 *4 H 0 {4,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 C 0 {1,S} {5,D}
5 *3 O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (193000,"m^3/(mol*s)","+|-",120000),
        n = 0,
        Ea = (6.951,"kJ/mol","+|-",1.322),
        T0 = (1,"K"),
        Tmin = (265,"K"),
        Tmax = (361,"K"),
        Pmin = (20000,"Pa"),
        Pmax = (20000,"Pa"),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'Reactions of alkoxy radicals with O2. III. i-C4H9O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """503""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI503:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013994
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013994/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:21:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI503:2"""),
    ],
)

entry(
    index = 115,
    label = "1994DOU/PER1597-1627:2",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {3,S}
3    C 0 {1,S} {2,S} {4,D}
4    C 0 {3,D}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {4,D}
3 *1 C 1 {2,S}
4    C 0 {2,D}
""",
    product2 = 
"""
1 *2 C 0 {4,S} {5,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
5 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (209.525,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (753,"K"),
        Tmax = (813,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (13300,"Pa"),
    ),
    reference = Article(
        authors = ["Douhou, S.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """1597-1627""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005815
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005815/rk00000001.xml
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:09:54 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:2"""),
    ],
)

entry(
    index = 116,
    label = "1994DOU/PER1597-1627:3",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {3,S}
3    C 0 {1,S} {2,S} {4,D}
4    C 0 {3,D}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {4,D}
3 *1 C 1 {2,S}
4    C 0 {2,D}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.9e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (231.142,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (763,"K"),
        Tmax = (813,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (13300,"Pa"),
    ),
    reference = Article(
        authors = ["Douhou, S.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """1597-1627""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005816
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005816/rk00000001.xml
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Thu Jul 12 23:09:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:3"""),
    ],
)

entry(
    index = 117,
    label = "1960KER/TRO1602:5",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 1 {2,S}
5 *4 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 0 {2,S} {5,S}
5 *4 H 0 {4,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 C 0 {1,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+08,"m^3/(mol*s)"),
        n = 0,
        Ea = (5.438,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (334,"K"),
        Tmax = (502,"K"),
        Pmin = (1600,"Pa"),
        Pmax = (2800,"Pa"),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde',
        journal = "J. Chem. Soc.",
        pages = """1602""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1602:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011216
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011216/rk00000001.xml
Bath gas: n-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 17:23:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1602:5"""),
    ],
)

entry(
    index = 118,
    label = "1988TSA887:79",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:79",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author recommends a rate coefficient expression equal to double the rate expression of H+C2H5=H2+C2H4. (p. 932, Entry 42,4a)
""",
    history = [
        ("Tue Aug 28 16:31:58 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:79"""),
    ],
)

entry(
    index = 119,
    label = "1986TSA/HAM1087:255",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:255",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: Author recommends rate coefficient from study performed by Camilleri, et al. (1974) (p. 1174, Entry 17,4c)
""",
    history = [
        ("Tue Aug 28 16:38:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:255"""),
    ],
)

entry(
    index = 120,
    label = "1988TSA887:61",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (94100,"m^3/(mol*s)","*|/",1.5),
        n = 0.68,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:61",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Uncertainty: 1.5

===

M. Harper, 8/30/09: Author notes that measurements performed by Arthur and Anastasi on the rate coefficient of total CH3+i-C3H7 decomposition matches very well with the coefficient derived from the recommended rate of CH3+CH3 decomposition, the recommended rate of i-C3H7+i-C3H7 decomposition, and the geometric rule. The author recommends a high-pressure rate expression of 4.7E-11*(300/T)^0.68 cm3/molecule/s for the addition rxn (based on the geometric mean rule???) and recommends the branching ratio of 0.16 reported by Gibian and Corley (1973). (p. 937, Entry 42,16b)
""",
    history = [
        ("Tue Aug 28 17:04:22 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:61"""),
    ],
)

entry(
    index = 121,
    label = "1988TSA887:61",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+07,"m^3/(mol*s)","*|/",1.1),
        n = -0.35,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:81",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Reference Reaction: iso-C3H7 + ·C2H5 → iso-C5H12 (1988TSA887:84)
Uncertainty: 1.1

===

M. Harper, 8/30/09: No data available at the time. The rate coefficient expression for the combination rxn is computed using the geometric mean rule and is reported as 2.6E11*(300/T)^0.35 cm3/molecule/s. The recommended branching ratio for disproportionation to addition is that reported by Gibian and Corley (1973). (p. 937-938, Entry 42,17c)
""",
    history = [
        ("Tue Aug 28 17:22:43 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:81"""),
    ],
)

entry(
    index = 122,
    label = "1988TSA887:65",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 1 {2,S}
2    O 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:65",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/30/09: No data available at the time. Author recommends a rate coefficient of 4.8E-12 based on the rate expression of i-C3H7+C2H5=C2H6+C3H6. (p. 945, Entryy 42,39c)
""",
    history = [
        ("Tue Aug 28 17:38:42 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:65"""),
    ],
)

entry(
    index = 123,
    label = "1988TSA887:51",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 1 {1,S} {2,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+08,"m^3/(mol*s)","*|/",2),
        n = -0.7,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:51",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No high-Temperature data available. Author has fit rate coefficient expression for addition rxn to 4 sets of experimental data. Recommended branching ratio agrees well with most of the experimental data. (p. 946-947, Entry 42,42b)
""",
    history = [
        ("Tue Aug 28 17:43:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:51"""),
    ],
)

entry(
    index = 124,
    label = "1990TSA1-68:63",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *1 C 1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.86e+09,"m^3/(mol*s)","*|/",1.7),
        n = -1.1,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:63",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 1.7

===

M. Harper, 8/30/09: The author computes the combination rate expression using the geometric mean rule (of the rxns t-C4H9+t-C4H9-->adduct and i-C3H7+i-C3H7-->adduct). The disproportionation rate coefficient expression was then computed using the reported branching ratio. (p. 46, Entry 44,42a)
""",
    history = [
        ("Tue Aug 28 17:48:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:63"""),
    ],
)

entry(
    index = 125,
    label = "1988TSA887:70",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.52e+08,"m^3/(mol*s)","*|/",2),
        n = -0.7,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:70",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author recommends the rate coefficient expression of C2H5+i-C3H7 for the rate expression for C2H3+i-C3H7. Author also recommends the branching ratio of disproportionation to addition of the C2H5+i-C3H7 system for the C2H3+i-C3H7 system. (p. 939-940, Entry 42,19a)
""",
    history = [
        ("Tue Aug 28 17:54:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:70"""),
    ],
)

entry(
    index = 126,
    label = "1988TSA887:54",
    reactant1 = 
"""
1    C 0 {2,T}
2 *1 C 1 {1,T}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,T}
2 *1 C 0 {1,T} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:54",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author recommends a rate coefficient of 6E-12 cm3/molecule/s, a "typical" disproportionation rate. (p. 941-942, Entry 42,21a)
""",
    history = [
        ("Tue Aug 28 18:00:08 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:54"""),
    ],
)

entry(
    index = 127,
    label = "1988TSA887:76",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:76",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author notes that both a H-atom abstractionrxn and an addition + hot adduct decomposition rxn will result in the same products. (p. 934, Entry 42,6)
""",
    history = [
        ("Tue Aug 28 18:04:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:76"""),
    ],
)

entry(
    index = 128,
    label = "1992BAU/COB411-429:119",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+07,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:119",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.1600001

===

M. Harper, 8/31/09: Authors state that no new data have been reported for this reaction. MRH assumes the recommended value comes from a previous review article published by authors. In any case, recommended data fits the reported data well. (p. 523)
""",
    history = [
        ("Tue Aug 28 18:44:50 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:119"""),
    ],
)

entry(
    index = 129,
    label = "1988TSA887:116",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:116",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author recommends the rate coefficient of the H+C2H5=C2H4+H2 rxn for the H+n-C3H7=C3H6+H2 rxn. (p. 915-916, Entry 41,4a)
""",
    history = [
        ("Tue Aug 28 18:56:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:116"""),
    ],
)

entry(
    index = 130,
    label = "1988TSA887:99",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+07,"m^3/(mol*s)","*|/",1.7),
        n = -0.32,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:99",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 1.7

===

M. Harper, 8/30/09: No direct measurements for either the addition or disproportionation rxns. Author recommends a rate coefficient expression for the addition rxn, based on the geometric mean rule of the rxns CH3+CH3=>adduct and n-C3H7+n-C3H7=>adduct. Furthermore, author recommends a branching ratio for disproportionation to addition of 0.06 (which appears to MRH to be consistent with the experimentally measured branching ratios). (p. 920, Entry 41,16b)
""",
    history = [
        ("Tue Aug 28 19:00:18 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:99"""),
    ],
)

entry(
    index = 131,
    label = "1988TSA887:117",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+06,"m^3/(mol*s)","*|/",1.4),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:117",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 1.4

===

M. Harper, 8/30/09: No direct measurements for either the addition or disproportionation rxns. Author recommends a rate coefficient expression for the addition rxn, based on the geometric mean rule of the rxns C2H5+C2H5=>adduct and n-C3H7+n-C3H7=>adduct. Furthermore, author recommends a branching ratio for disproportionation to addition of 0.073 (which is an average of the 2 experimentally determined branching ratios). (p. 937-938, Entry 42,17b)
""",
    history = [
        ("Tue Aug 28 19:05:18 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:117"""),
    ],
)

entry(
    index = 132,
    label = "1988TSA887:102",
    reactant1 = 
"""
1 *1 C 1 {2,S}
2    O 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (482000,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:102",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the rate coefficient for the addition rxn to be similar to the rate for n-C3H7+n-C3H7=>adduct. Author also estimates the branching ratio of disproportionation to addition as 0.051. (p. 926, Entry 41,39c)
""",
    history = [
        ("Tue Aug 28 19:18:52 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:102"""),
    ],
)

entry(
    index = 133,
    label = "1988TSA887:56",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,S}
4 *4 H 0 {3,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+07,"m^3/(mol*s)","*|/",2),
        n = -0.35,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:56",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the rate coefficient expression of the addition rxn using the rate for i-C3H7+i-C3H7=>adduct, the rate for n-C3H7+n-C3H7=>adduct, and the geometric mean rule. The author recommends the branching ratio of disproportionation to addition reported by Gibian and Corley (1973). (p. 945-946, Entry 42,41b)
""",
    history = [
        ("Tue Aug 28 19:23:19 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:56"""),
    ],
)

entry(
    index = 134,
    label = "1990TSA1-68:69",
    reactant1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *1 C 1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08,"m^3/(mol*s)","*|/",2),
        n = -0.75,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:69",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the rate expression for the combination rxn using the geometric mean rule (of the rxns t-C4H9+t-C4H9-->adduct and n-C3H7+n-C3H7-->adduct). The author then estimates the disproportionation rate expression using the branching ratio; the branching ratio is from "analogous processes". (p. 45, Entry 44,41a)
""",
    history = [
        ("Tue Aug 28 19:30:22 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:69"""),
    ],
)

entry(
    index = 135,
    label = "1988TSA887:106",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:106",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the rate coefficient based on the rxn C2H5+n-C3H7=C3H6=C2H6. (p. 922, Entry 41,19a)
""",
    history = [
        ("Tue Aug 28 19:35:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:106"""),
    ],
)

entry(
    index = 136,
    label = "1988TSA887:90",
    reactant1 = 
"""
1    C 0 {2,T}
2 *1 C 1 {1,T}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,T}
2 *1 C 0 {1,T} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:90",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author notes that the rxn is more exothermic than the rxn CH3+n-C3H7=C3H6+CH4 and suggests a rate coefficient 3x larger, namely 1.0E-11 cm3/molecule/s. (p. 923, Entry 41,21a)
""",
    history = [
        ("Tue Aug 28 19:41:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:90"""),
    ],
)

entry(
    index = 137,
    label = "1988TSA887:112",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:112",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates rate coefficient based on the rate coefficient for OH+C2H5=C2H4+H2O, namely 4.0E-11 cm3/molecule/s. (p. 917, Entry 41,6a)
""",
    history = [
        ("Tue Aug 28 19:43:52 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:112"""),
    ],
)

entry(
    index = 138,
    label = "1990TSA1-68:101",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,T}
2 *1 C 1 {1,T}
""",
    product1 = 
"""
1    C 0 {2,T}
2 *1 C 0 {1,T} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:101",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. The author estimates the rate of disproportionation to be 1E-11 cm3/molecule/s. (p. 61, Entry 45,21)
""",
    history = [
        ("Tue Aug 28 19:49:48 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:101"""),
    ],
)

entry(
    index = 139,
    label = "1990TSA1-68:129",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (904000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:129",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. The author estimates the disproportionation rate coefficent as half the rate of H+n-C3H7=C3H6+H2 (due to the presence of 2 H-atoms on the alpha-carbon in n-C3H7 and only 1 on the alpha-carbon of i-C4H9). The author also states that the branching ratio is pressure-dependent and supplies fall-off tables and collisional efficiencies. (p. 53, Entry 45,4c)
""",
    history = [
        ("Tue Aug 28 19:52:25 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:129"""),
    ],
)

entry(
    index = 140,
    label = "1988TSA887:89",
    reactant1 = 
"""
1 *1 C 2T
""",
    reactant2 = 
"""
1 *2 C 0 {3,S} {4,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+07,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:89",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author suggests this is a minor channel, stating the main process should be combination, leading to chemically activated i-butyl radical. Rate coefficient is estimate. (p. 944, Entry 42,26)
""",
    history = [
        ("Thu Aug 30 12:12:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:89"""),
    ],
)

entry(
    index = 141,
    label = "1988TSA887:123",
    reactant1 = 
"""
1 *1 C 2T
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:123",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the rate coefficient expression of the addition rxn. The author then recommends that the disproportionation rate coefficient not exceed 10% of the combination rate. Thus, the rate coefficient is an upper limit. (p. 925, Entry 41,26)
""",
    history = [
        ("Thu Aug 30 12:23:28 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:123"""),
    ],
)

entry(
    index = 142,
    label = "1990TSA1-68:109",
    reactant1 = 
"""
1 *1 C 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+06,"m^3/(mol*s)","*|/",2),
        n = -0.32,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:109",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. The author estimates the disproportionation rate coefficient as half the rate of CH3+n-C3H7=C3H6+H2 (due to half as many H-atoms on the alpha-carbon). (p. 58, Entry 45,16b)
""",
    history = [
        ("Thu Aug 30 12:30:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:109"""),
    ],
)

entry(
    index = 143,
    label = "1990TSA1-68:130",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (843000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:130",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No direct measurements of either the addition or disproportionation rxns. The combination rate coefficient was computed using the geometric mean rule (of the rxns C2H5+C2H5-->adduct and i-C4H9+i-C4H9-->adduct). The disproportionation rate coefficient was computed using the disproportionation-to-combination ratio reported by Gibian and Corley (1973). (p. 59, Entry 45,17a)
""",
    history = [
        ("Thu Aug 30 12:34:53 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:130"""),
    ],
)

entry(
    index = 144,
    label = "1990TSA1-68:112",
    reactant1 = 
"""
1 *1 C 1 {2,S}
2    O 0 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (482000,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:112",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the disproportionation rate coefficient as half the rate of CH2OH+n-C3H7=C3H6+CH3OH (due to half as many H-atoms on the alpha-carbon). (p. 64, Entry 45,39c)
""",
    history = [
        ("Thu Aug 30 12:42:08 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:112"""),
    ],
)

entry(
    index = 145,
    label = "1990TSA1-68:98",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 1 {1,S} {2,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+07,"m^3/(mol*s)","*|/",2),
        n = -0.35,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:98",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the disproportionation rate coefficient as half the rate of i-C3H7+n-C3H7=C3H6+C3H8 (due to half as many H-atoms on the alpha-carbon). (p. 65, Entry 45,42b)
""",
    history = [
        ("Thu Aug 30 12:55:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:98"""),
    ],
)

entry(
    index = 146,
    label = "1990TSA1-68:86",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *1 C 1 {1,S}
""",
    reactant2 = 
"""
1 *2 C 0 {4,S} {5,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *1 C 0 {1,S} {5,S}
5 *4 H 0 {4,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08,"m^3/(mol*s)","*|/",2),
        n = -0.75,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:86",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the disproportionation rate coefficient as half the rate of t-C4H9+n-C3H7=C3H6+i-C4H10 (due to half as many H-atoms on the alpha-carbon). (p. 66, Entry 45,44b)
""",
    history = [
        ("Thu Aug 30 13:19:56 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:86"""),
    ],
)

entry(
    index = 147,
    label = "1990TSA1-68:115",
    reactant1 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S}
3 *4 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (843000,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:115",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the disproportionation rate coefficient based on the rate of C2H5+i-C4H9=i-C4H8+C2H6. (p. 60, Entry 45,19b)
""",
    history = [
        ("Thu Aug 30 13:31:22 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:115"""),
    ],
)

entry(
    index = 148,
    label = "1990TSA1-68:121",
    reactant1 = 
"""
1 *1 O 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:121",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the disproportionation rate coefficient as half the rate of OH+n-C3H7=C3H6+H2O (due to half as many H-atoms on the alpha-carbon). (p. 55, Entry 45,6a)
""",
    history = [
        ("Thu Aug 30 13:43:54 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:121"""),
    ],
)

entry(
    index = 149,
    label = "1991TSA221-273:110",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *3 C 1 {1,S}
3    C 0 {1,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+07,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:110",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Author assigns a rate coefficient of 3E-11 cm3/molecule/s for the disproportionation rxn. (p. 252, Entry 47,4c)
""",
    history = [
        ("Thu Aug 30 13:52:50 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:110"""),
    ],
)

entry(
    index = 150,
    label = "1991TSA221-273:97",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *1 C 1 {1,D}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,D}
2 *3 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:97",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Author recommends a rate coefficient of 4E-12 cm3/molecule/s for the disproportionation rxn. (p. 261-262, Entry 47,19d)
""",
    history = [
        ("Fri Aug 31 10:26:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:97"""),
    ],
)

entry(
    index = 151,
    label = "1991TSA221-273:102",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *3 C 1 {1,S}
3    C 0 {1,D}
4 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:102",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/31/09: No data available at the time. Author recommends a rate coefficient of 1E-11 cm3/molecule/s, based on "comparable rxns". (p. 253, Entry 47,6a)
""",
    history = [
        ("Fri Aug 31 10:30:45 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:102"""),
    ],
)

entry(
    index = 152,
    label = "1989GRO/RIE963-972:3",
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    reactant2 = 
"""
1 *1 O 2T
""",
    product1 = 
"""
1 *1 O 1 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+07,"m^3/(mol*s)","+|-",3e+07),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (298,"K"),
        Pmin = (99.99,"Pa"),
    ),
    reference = Article(
        authors = ["Grotheer, H.", "Riekert, G.", "Walter, D.", "Just, Th."],
        title = u'Reactions of hydroxymethyl and hydroxyethyl radicals with molecular and atomic oxygen',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """963-972""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989GRO/RIE963-972:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
    history = [
        ("Fri Aug 31 13:39:54 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989GRO/RIE963-972:3"""),
    ],
)

entry(
    index = 153,
    label = "1989GRO/RIE963-972:4",
    reactant1 = 
"""
1 *1 O 2T
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *4 H 0 {2,S}
2 *1 O 1 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+07,"m^3/(mol*s)","+|-",3e+07),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (298,"K"),
        Pmin = (99.99,"Pa"),
    ),
    reference = Article(
        authors = ["Grotheer, H.", "Riekert, G.", "Walter, D.", "Just, Th."],
        title = u'Reactions of hydroxymethyl and hydroxyethyl radicals with molecular and atomic oxygen',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """963-972""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989GRO/RIE963-972:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
    history = [
        ("Fri Aug 31 13:45:42 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1989GRO/RIE963-972:4"""),
    ],
)

entry(
    index = 154,
    label = "1987TSA471:53",
    reactant1 = 
"""
1 *1 C 2T
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+06,"m^3/(mol*s)","*|/",3),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:53",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.0

===

M. Harper, 8/30/09: No data at the time. Author estimates the rate of disproportionation as 2.0E-12 cm3/molecule/s. (p. 505, Entry 39,26b)
""",
    history = [
        ("Fri Aug 31 13:49:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:53"""),
    ],
)

entry(
    index = 155,
    label = "1992EDE/HOY661-668:3",
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07,"m^3/(mol*s)","+|-",1e+07),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (295,"K"),
        Pmin = (99.99,"Pa"),
    ),
    reference = Article(
        authors = ["Edelbuttel-Einhaus, J.", "Hoyermann, K.", "Rohde, G.", "Seeba, J."],
        title = u'The detection of the hydroxyethyl radical by REMPI/mass-spectrometry and the application to the study of the reactions CH3CHOH + O and CH3CHOH + H',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """661-668""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992EDE/HOY661-668:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Reference Reaction: ·C2H5 + H· → ·CH3 + ·CH3
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry

===

M. Harper, 9/1/09: The reported rate coefficient is for H+CH3CHOH --> products, making this an UPPER LIMIT. The rate coefficient was calculated based on the rate coefficient of the rxn C2H5+H --> CH3+CH3; the value the authors used was 3.6E13 cm3/mol/s. (p. 665-666)
""",
    history = [
        ("Fri Aug 31 13:54:48 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992EDE/HOY661-668:3"""),
    ],
)

entry(
    index = 156,
    label = "1987TSA471:47",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *4 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:47",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data at the time. Author estimates disproportionation rate will be faster than the H+C2H5=H2+C2H4 reaction and reports rate coefficient as 1.0E-11 cm3/molecule/s. (p. 496-497, Entry 39,4a)
""",
    history = [
        ("Fri Aug 31 14:00:36 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:47"""),
    ],
)

entry(
    index = 157,
    label = "1988PAG/MUN375:6",
    reactant1 = 
"""
1 *1 C 1
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.49e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (298,"K"),
        Pmin = (100000,"Pa"),
    ),
    reference = Article(
        authors = ["Pagsberg, P.", "Munk, J.", "Sillesen, A.", "Anastasi, C."],
        title = u'UV spectrum and kinetics of hydroxymethyl radicals',
        journal = "Chem. Phys. Lett.",
        volume = "146",
        pages = """375""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988PAG/MUN375:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Bath gas: Ar
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption

===

M. Harper, 9/1/09: Formation and decay rates of CH2OH, CH3, and OH observed by pulse radiolysis of gas mixtures of varying composition. Chemical composition of systems A-E as in Table 1. The authors note below Table 2 that the reported rate coefficient for CH3+CH2OH is an "adjustment of model to reproduce the observed decay rates of CH3 and CH2OH". MRH is skeptical of data, as this specific rxn is not directly referenced in the article, nor do the authors address whether other channels besides -->CH4+CH2O exist / are significant. The value of A in the database is consistent with that reported in Table 2. (p. 378)
""",
    history = [
        ("Fri Aug 31 14:25:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988PAG/MUN375:6"""),
    ],
)

entry(
    index = 158,
    label = "1990TSA1-68:126",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (600,"K"),
        Tmax = (900,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:126",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/31/09: The author recommends a rate coefficient based on the experiments performed by Baker et al. (yielding a disproportionation-to-decomposition ratio) and the current (Tsang) study's recommended iC4H9 unimolecular decomposition rate. (p. 52-53, Entry 45,3a)
""",
    history = [
        ("Fri Aug 31 14:51:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:126"""),
    ],
)

entry(
    index = 159,
    label = "2001ATK/BAU1-56:127",
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.14e+07,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (298,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:127",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Pressure dependence: None reported

===

M. Harper, 8/31/09: Recommended value is k298. This reference just gives a table of results, with no discussion on how the preferred numbers were arrived at.
""",
    history = [
        ("Fri Aug 31 15:08:13 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:127"""),
    ],
)

entry(
    index = 160,
    label = "2001ATK/BAU1-56:126",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (298,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:126",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Pressure dependence: None reported

===

M. Harper, 8/31/09: Recommended value is k298. This reference just gives a table of results, with no discussion on how the preferred numbers were arrived at.
""",
    history = [
        ("Fri Aug 31 15:13:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:126"""),
    ],
)

entry(
    index = 161,
    label = "1997DEM/SAN1-266:290",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.48e+06,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:290",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
M. Harper, 9/1/09: Recommended A-factor and E/R parameter values (p. 22)
""",
    history = [
        ("Fri Aug 31 15:16:46 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:290"""),
    ],
)

entry(
    index = 162,
    label = "1987TSA471:32",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:32",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/30/09: No data at the time. Author estimates ratio of disproportionation rate to addition rate to be 0.2, namely 4E-12 cm3/molecule/s. (p. 500-501, Entry 39,16b)
""",
    history = [
        ("Tue Sep  4 14:24:14 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:32"""),
    ],
)

entry(
    index = 163,
    label = "1987TSA471:49",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:49",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/30/09: No data at the time. Author estimates the disproportionation rate coefficient as 4E-12 cm3/molecule/s. (p. 502, Entry 39,17b)
""",
    history = [
        ("Tue Sep  4 14:29:08 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:49"""),
    ],
)

entry(
    index = 164,
    label = "1991TSA221-273:93",
    reactant1 = 
"""
1    C 0 {2,S} {3,D}
2 *1 C 1 {1,S}
3    C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+07,"m^3/(mol*s)","*|/",2.5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:93",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.5

===

M. Harper, 8/31/09: No data available at the time. Author notes that combination of these two reactants will form 3-butene-1-ol which should decompose under combustion conditions to form C3H6 + CH2O (same products). The author therefore recommends a rate coefficient of 3E-11 cm3/molecule/s. (p. 267, Entry 47,39)
""",
    history = [
        ("Tue Sep  4 14:33:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:93"""),
    ],
)

entry(
    index = 165,
    label = "1987TSA471:36",
    reactant1 = 
"""
1 *1 C 1 {2,S}
2    O 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+06,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:36",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09:

Meier, et al. (1985) measured the rate of addition + disproportionation. Tsang estimates a disproportionation-to-combination ratio of 0.5. (p. 506, Entry 39,39b)

NOTE: Rate coefficient given in table at beginning of reference (summarizing all data presented) gives k_a+b = 2.4E-11, leading to k_b = 8E-12. NIST's online database (kinetics.nist.gov) reports this number as well. However, the discussion on p. 506 suggests k_a+b = 1.5E-11, leading to k_b = 5E-12.
""",
    history = [
        ("Tue Sep  4 14:37:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:36"""),
    ],
)

entry(
    index = 166,
    label = "1988TSA887:64",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 1 {1,S} {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+06,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:64",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0

===

M. Harper, 8/30/09: No data available at the time. Author suggests rate coefficient based on rxn C2H5+i-C3H7=C3H8+C2H4, namely 3.9E-12 cm3/molecule/s. (p. 945, Entry 42,39b)
""",
    history = [
        ("Tue Sep  4 14:48:05 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:64"""),
    ],
)

entry(
    index = 167,
    label = "1990TSA1-68:75",
    reactant1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *1 C 1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.91e+08,"m^3/(mol*s)","*|/",2),
        n = -0.75,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:75",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0

===

M. Harper, 8/30/09: No data available at the time. Author estimates the addition rxn rate coefficient based on the rate for t-C4H9+C2H5-->adduct. The author uses a disproportionation-to-addition ratio of 0.52 to obtain the reported rate coefficient expression. (p. 44, Entry 44,39a)
""",
    history = [
        ("Tue Sep  4 14:54:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:75"""),
    ],
)

