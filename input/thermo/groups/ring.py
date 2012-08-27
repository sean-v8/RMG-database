#!/usr/bin/env python
# encoding: utf-8

name = "Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R 0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Dummy Root""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "ThreeMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {3,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {1,{S,D}} {2,{S,D}}
""",
    thermo = 'Cyclopropane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 1,
    label = "Cyclopropane",
    group = 
"""
1 * Cs 0 {2,S} {3,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],"cal/(mol*K)"),
        H298 = (27.53,"kcal/mol"),
        S298 = (32.0088,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopropane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "Cyclopropene",
    group = 
"""
1 * Cs 0 {2,S} {3,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],"cal/(mol*K)"),
        H298 = (55.4702,"kcal/mol"),
        S298 = (33.3257,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopropene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "Cyclopropadiene",
    group = 
"""
1 * Cd  0 {2,S} {3,D}
2   Cd  0 {1,S} {3,D}
3   Cdd 0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],"cal/(mol*K)"),
        H298 = (73.04,"kcal/mol"),
        S298 = (33.3257,"cal/(mol*K)"),
    ),
    shortDesc = u"""Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "Cyclopropatriene",
    group = 
"""
1 * Cdd 0 {2,D} {3,D}
2   Cdd 0 {1,D} {3,D}
3   Cdd 0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],"cal/(mol*K)"),
        H298 = (78,"kcal/mol"),
        S298 = (33.3257,"cal/(mol*K)"),
    ),
    shortDesc = u"""Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "Ethylene_oxide",
    group = 
"""
1 * O  0 {2,S} {3,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.891,-2.459,-2.221,-1.969,-1.965,-1.759,2.564],"cal/(mol*K)"),
        H298 = (26.82,"kcal/mol"),
        S298 = (31.1767,"cal/(mol*K)"),
    ),
    shortDesc = u"""CY/C2O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "dioxirane",
    group = 
"""
1 * Os 0 {2,S} {3,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.099,-3.194,-3.095,-3.038,-3.281,-3.818,-1.346],"cal/(mol*K)"),
        H298 = (25.1977,"kcal/mol"),
        S298 = (32.3877,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "2(co)oxirane",
    group = 
"""
1   CO 0 {2,S} {3,S}
2 * Os 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.147,-1.715,-2.067,-2.254,-2.546,-2.592,-1.488],"cal/(mol*K)"),
        H298 = (40.7699,"kcal/mol"),
        S298 = (34.529,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "cyclopropanedione",
    group = 
"""
1   CO 0 {2,S} {3,S}
2 * CO 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.85,1.69,0.674,-0.137,-1.157,-2.068,0.878],"cal/(mol*K)"),
        H298 = (67.2975,"kcal/mol"),
        S298 = (38.9107,"cal/(mol*K)"),
    ),
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
    label = "cyclopropenone",
    group = 
"""
1   Cd 0 {2,S} {3,D}
2 * CO 0 {1,S} {3,S}
3   Cd 0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.734,-1.275,-1.673,-1.861,-2.134,-2.557,-1.78],"cal/(mol*K)"),
        H298 = (56.774,"kcal/mol"),
        S298 = (35.6157,"cal/(mol*K)"),
    ),
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
    label = "Methylene_cyclopropane",
    group = 
"""
1 * Cd 0 {2,S} {3,S} {4,D}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
4   Cd 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.1,-2.121,-2.081,-2.005,-1.98,-1.903,-1.541],"cal/(mol*K)"),
        H298 = (40.92,"kcal/mol"),
        S298 = (31.4507,"cal/(mol*K)"),
    ),
    shortDesc = u"""Methylene cyclopropane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "cyclopropanone",
    group = 
"""
1 * C 0 {2,S} {3,S} {4,D}
2   C 0 {1,S} {3,S}
3   C 0 {1,S} {2,S}
4   O 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.274,-1.932,-1.307,-0.838,-1.06,-1.032,-0.271],"cal/(mol*K)"),
        H298 = (45.6,"kcal/mol"),
        S298 = (30.7247,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "methylenecyclopropene",
    group = 
"""
1   Cd 0 {2,S} {3,D}
2 * Cd 0 {1,S} {3,S} {4,D}
3   Cd 0 {1,D} {2,S}
4   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.457,-0.093,-0.645,-1.124,-1.936,-2.246,-2.962],"cal/(mol*K)"),
        H298 = (69.316,"kcal/mol"),
        S298 = (39.8857,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "methylenecyclopropanone",
    group = 
"""
1   CO 0 {2,S} {3,S}
2 * Cd 0 {1,S} {3,S} {4,D}
3   Cs 0 {1,S} {2,S}
4   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.13,-1.101,-1.774,-2.139,-2.509,-2.858,-0.084],"cal/(mol*K)"),
        H298 = (57.7946,"kcal/mol"),
        S298 = (37.18,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "methyleneoxirane",
    group = 
"""
1   Os 0 {2,S} {3,S}
2 * Cd 0 {1,S} {3,S} {4,D}
3   Cs 0 {1,S} {2,S}
4   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.101,-2.381,-2.338,-2.236,-2.424,-2.639,-2.068],"cal/(mol*K)"),
        H298 = (36.0543,"kcal/mol"),
        S298 = (29.893,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "12Methylenecyclopropane",
    group = 
"""
1   Cd 0 {2,S} {3,S} {4,D}
2 * Cd 0 {1,S} {3,S} {5,D}
3   Cs 0 {1,S} {2,S}
4   Cd 0 {1,D}
5   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.326,-3.139,-3.361,-3.148,-2.736,-2.412,-1.706],"cal/(mol*K)"),
        H298 = (51.4711,"kcal/mol"),
        S298 = (35.3587,"cal/(mol*K)"),
    ),
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
    label = "FourMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {4,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {1,{S,D}} {3,{S,D}}
""",
    thermo = 'Cyclobutane',
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
    label = "Cyclobutane",
    group = 
"""
1 * Cs 0 {2,S} {4,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],"cal/(mol*K)"),
        H298 = (26.2,"kcal/mol"),
        S298 = (29.8,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclobutane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Cyclobutene",
    group = 
"""
1 * Cs 0 {2,S} {4,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],"cal/(mol*K)"),
        H298 = (29.84,"kcal/mol"),
        S298 = (29.8677,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclobutene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Oxetane",
    group = 
"""
1 * O  0 {2,S} {4,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.08,-4.28,-3.636,-3.016,-2.451,-1.896,2.84],"cal/(mol*K)"),
        H298 = (25.08,"kcal/mol"),
        S298 = (28.5487,"cal/(mol*K)"),
    ),
    shortDesc = u"""CY/C3O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O  0 {2,S} {4,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   CO 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.434,-4.019,-3.31,-2.703,-2.253,-2.012,1.3],"cal/(mol*K)"),
        H298 = (22.98,"kcal/mol"),
        S298 = (30.392,"cal/(mol*K)"),
    ),
    shortDesc = u"""Beta-Propiolactone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "Cyclobutanone",
    group = 
"""
1 * CO 0 {2,S} {4,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.62,-4.96,-3.744,-2.671,-1.962,-1.415,-0.3],"cal/(mol*K)"),
        H298 = (22.53,"kcal/mol"),
        S298 = (29.8337,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclobutanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "12dioxetane",
    group = 
"""
1   Cs 0 {2,S} {4,S}
2 * Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4   Os 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.586,-4.031,-3.818,-3.503,-3.252,-3.45,1.262],"cal/(mol*K)"),
        H298 = (28.0736,"kcal/mol"),
        S298 = (29.0217,"cal/(mol*K)"),
    ),
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
    label = "dioxerene",
    group = 
"""
1   Cd 0 {2,D} {4,S}
2 * Cd 0 {1,D} {3,S}
3   Os 0 {2,S} {4,S}
4   Os 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.375,-4.281,-4.206,-4.037,-3.926,-3.327,-2.473],"cal/(mol*K)"),
        H298 = (24.4413,"kcal/mol"),
        S298 = (29.7827,"cal/(mol*K)"),
    ),
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
    label = "cyclobutadiene",
    group = 
"""
1   Cd 0 {2,D} {4,S}
2 * Cd 0 {1,D} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.336,-3.24,-3.526,-3.419,-3.071,-2.761,-2.346],"cal/(mol*K)"),
        H298 = (77.2135,"kcal/mol"),
        S298 = (36.4303,"cal/(mol*K)"),
    ),
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
    label = "4-Methylene-2-oxetanone",
    group = 
"""
1 * O  0 {2,S} {4,S}
2   Cd 0 {1,S} {3,S} {5,D}
3   Cs 0 {2,S} {4,S}
4   CO 0 {1,S} {3,S}
5   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.912,-1.903,-1.567,-1.378,-1.566,-1.528,1.547],"cal/(mol*K)"),
        H298 = (16.94,"kcal/mol"),
        S298 = (35.477,"cal/(mol*K)"),
    ),
    shortDesc = u"""4-Methylene-2-oxetanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "methylenecyclobutane",
    group = 
"""
1   Cs 0 {2,S} {4,S}
2 * Cd 0 {1,S} {3,S} {5,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
5   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.91,-3.339,-2.739,-2.2,-1.51,-1.051,-62.52],"cal/(mol*K)"),
        H298 = (26.9,"kcal/mol"),
        S298 = (28.8887,"cal/(mol*K)"),
    ),
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
    label = "2methyleneoxetane",
    group = 
"""
1   Os 0 {2,S} {4,S}
2 * Cd 0 {1,S} {3,S} {5,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
5   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.33,-3.553,-3.213,-2.78,-2.445,-2.331,0.556],"cal/(mol*K)"),
        H298 = (23.79,"kcal/mol"),
        S298 = (25.597,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "12methylenecyclobutane",
    group = 
"""
1 * Cd 0 {2,S} {4,S} {5,D}
2   Cd 0 {1,S} {3,S} {6,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {1,S} {3,S}
5   Cd 0 {1,D}
6   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.313,-4.605,-4.416,-3.887,-3.024,-2.355,-1.276],"cal/(mol*K)"),
        H298 = (28.04,"kcal/mol"),
        S298 = (31.4877,"cal/(mol*K)"),
    ),
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
    label = "FiveMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {5,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {3,{S,D}} {5,{S,D}}
5   R!H 0 {1,{S,D}} {4,{S,D}}
""",
    thermo = 'Cyclopentane',
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
    label = "Cyclopentane",
    group = 
"""
1 * Cs 0 {2,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],"cal/(mol*K)"),
        H298 = (6.3,"kcal/mol"),
        S298 = (27.3,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopentane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "Cyclopentene",
    group = 
"""
1   Cs 0 {2,S} {5,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5 * Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],"cal/(mol*K)"),
        H298 = (5.97,"kcal/mol"),
        S298 = (25.8284,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopentene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Cyclopentadiene",
    group = 
"""
1 * Cs 0 {2,S} {5,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.7845,-3.72708,-3.2688,-2.74383,-2.05359,-1.65464,-0.98756],"cal/(mol*K)"),
        H298 = (6.05,"kcal/mol"),
        S298 = (27.9821,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopentadiene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O  0 {2,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.93,-5.71,-4.67,-3.721,-2.689,-1.856,3.213],"cal/(mol*K)"),
        H298 = (5.96,"kcal/mol"),
        S298 = (21.1624,"cal/(mol*K)"),
    ),
    shortDesc = u"""CY/C4O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "2,3-Dihydrofuran",
    group = 
"""
1 * O  0 {2,S} {5,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.56,-5.96,-5.695,-5.144,-4.218,-3.708,-0.284],"cal/(mol*K)"),
        H298 = (4.57,"kcal/mol"),
        S298 = (23.83,"cal/(mol*K)"),
    ),
    shortDesc = u"""2,3-Dihydrofuran ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "1,3-Dioxolane",
    group = 
"""
1 * Cs 0 {2,S} {5,S}
2   O  0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   O  0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.655,-6.405,-6.306,-6.405,-7.631,-8.27,-3.21],"cal/(mol*K)"),
        H298 = (5.13,"kcal/mol"),
        S298 = (20.4021,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3-Dioxolane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "Furan",
    group = 
"""
1   Cd 0 {2,D} {5,S}
2   Cd 0 {1,D} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5 * O  0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.058,-7.002,-6.774,-6.09,-4.988,-3.95,-2.882],"cal/(mol*K)"),
        H298 = (6.89,"kcal/mol"),
        S298 = (30.0857,"cal/(mol*K)"),
    ),
    shortDesc = u"""Furan ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "Dihydro-2,5-furandione",
    group = 
"""
1 * O  0 {2,S} {5,S}
2   CO 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   CO 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.235,-4.726,-3.615,-1.82,-1.835,-1.084,1.104],"cal/(mol*K)"),
        H298 = (1.4,"kcal/mol"),
        S298 = (37.7647,"cal/(mol*K)"),
    ),
    shortDesc = u"""Dihydro-2,5-furandione ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "2,5-Furandione",
    group = 
"""
1 * O  0 {2,S} {5,S}
2   CO 0 {1,S} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   CO 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (3.6,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""2,5-Furandione ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "Cyclopentanone",
    group = 
"""
1 * CO 0 {2,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.06,-4.927,-3.392,-2.097,-1.093,-0.322,1.29],"cal/(mol*K)"),
        H298 = (4.47,"kcal/mol"),
        S298 = (24.6287,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclopentanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "butyrolactone",
    group = 
"""
1 * CO 0 {2,S} {5,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.836,-5.134,-4.114,-3.222,-2.341,-1.822,1.888],"cal/(mol*K)"),
        H298 = (7.92,"kcal/mol"),
        S298 = (27.4547,"cal/(mol*K)"),
    ),
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
    label = "25dihydrofuran",
    group = 
"""
1 * Cs 0 {2,S} {5,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.946,-3.361,-2.438,-1.799,-1.458,-1.056,-0.254],"cal/(mol*K)"),
        H298 = (4.23674,"kcal/mol"),
        S298 = (25.1504,"cal/(mol*K)"),
    ),
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
    label = "12dioxolane",
    group = 
"""
1 * Os 0 {2,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.95,-4.859,-4.265,-3.679,-3.089,-3.091,1.915],"cal/(mol*K)"),
        H298 = (6.05383,"kcal/mol"),
        S298 = (25.0554,"cal/(mol*K)"),
    ),
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
    label = "12dioxolene",
    group = 
"""
1 * Os 0 {2,S} {5,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.159,-4.213,-3.754,-3.376,-3.14,-2.919,-1.982],"cal/(mol*K)"),
        H298 = (4.56853,"kcal/mol"),
        S298 = (29.97,"cal/(mol*K)"),
    ),
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
    label = "123trioxolane",
    group = 
"""
1 * Os 0 {2,S} {5,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.566,-3.543,-3.344,-2.829,-2.487,-2.78,2.13],"cal/(mol*K)"),
        H298 = (10.1971,"kcal/mol"),
        S298 = (23.316,"cal/(mol*K)"),
    ),
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
    label = "124trioxolane",
    group = 
"""
1 * Os 0 {2,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.648,-4.764,-3.63,-2.89,-2.711,-2.859,2.25],"cal/(mol*K)"),
        H298 = (9.45319,"kcal/mol"),
        S298 = (25.1104,"cal/(mol*K)"),
    ),
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
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {6,D}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cd 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.861,-4.909,-3.91,-3.01,-1.769,-0.969,0],"cal/(mol*K)"),
        H298 = (5.21,"kcal/mol"),
        S298 = (24.6287,"cal/(mol*K)"),
    ),
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
    label = "Fulvene",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {6,D}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D}
6   Cd 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.1,-3.4,-3.4,-3.2,-3,-2.6,-2.6],"cal/(mol*K)"),
        H298 = (14.73,"kcal/mol"),
        S298 = (34.1,"cal/(mol*K)"),
    ),
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
    label = "12methylenecyclopentane",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {6,D}
2   Cd 0 {1,S} {3,S} {7,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cd 0 {1,D}
7   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.844,-5.197,-4.882,-4.175,-2.988,-2.088,-0.655],"cal/(mol*K)"),
        H298 = (6.67,"kcal/mol"),
        S298 = (31.384,"cal/(mol*K)"),
    ),
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
    label = "SixMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {6,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {3,{S,D}} {5,{S,D}}
5   R!H 0 {4,{S,D}} {6,{S,D}}
6   R!H 0 {1,{S,D}} {5,{S,D}}
""",
    thermo = 'Cyclohexane',
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
    label = "sixnosidedouble",
    group = 
"""
1 * {Cs,Os} 0 {2,S} {6,S}
2   {Cs,Os} 0 {1,S} {3,S}
3   {Cs,Os} 0 {2,S} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = 'Cyclohexane',
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
    label = "Cyclohexane",
    group = 
"""
1 * Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.8,-4.1,-2.9,-1.3,1.08,2.16,3],"cal/(mol*K)"),
        H298 = (0.08,"kcal/mol"),
        S298 = (18.1277,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclohexane ring BENSON https:""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "12dioxane",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4 * Cs 0 {3,S} {5,S}
5   Os 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.66,-5.11,-4.17,-3.36,-2.52,-2.4,2.76],"cal/(mol*K)"),
        H298 = (3.9,"kcal/mol"),
        S298 = (19.6424,"cal/(mol*K)"),
    ),
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
    label = "1,3-Dioxane",
    group = 
"""
1   O  0 {2,S} {6,S}
2 * Cs 0 {1,S} {3,S}
3   O  0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.28,-5.951,-4.458,-3.15,-1.967,-0.83,6.799],"cal/(mol*K)"),
        H298 = (1.88,"kcal/mol"),
        S298 = (16.1924,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3-Dioxane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3 * O  0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   O  0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.6,-5,-3.8,-2.6,-1.5,-0.4,8.9],"cal/(mol*K)"),
        H298 = (3.4,"kcal/mol"),
        S298 = (17.8049,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,4-Dioxane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   O  0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4 * O  0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   O  0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-7.01,-5.719,-3.632,-2.189,-1.525,-0.624,7.031],"cal/(mol*K)"),
        H298 = (4.09,"kcal/mol"),
        S298 = (16.1953,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3,5-Trioxane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "124trioxane",
    group = 
"""
1   Os 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4 * Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.68,-4.07,-2.95,-2.09,-1.73,-1.8,5.2],"cal/(mol*K)"),
        H298 = (3.6,"kcal/mol"),
        S298 = (19.9,"cal/(mol*K)"),
    ),
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
    label = "123trioxane",
    group = 
"""
1   Os 0 {2,S} {6,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4 * Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.08,-2.81,-2.55,-1.93,-1.55,-1.9,3.09],"cal/(mol*K)"),
        H298 = (4.87,"kcal/mol"),
        S298 = (17.2,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "Oxane",
    group = 
"""
1 * Cs 0 {2,S} {6,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6,-5.5,-4.2,-3,-1.6,-0.5,4.9],"cal/(mol*K)"),
        H298 = (0.7,"kcal/mol"),
        S298 = (18.8,"cal/(mol*K)"),
    ),
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
    label = "six-sidedoubles",
    group = 
"""
1   {C,O}   0 {2,S} {6,S}
2 * {Cd,CO} 0 {1,S} {3,S}
3   {C,O}   0 {2,S} {4,S}
4   {C,O}   0 {3,S} {5,S}
5   {C,O}   0 {4,S} {6,S}
6   {C,O}   0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10,10,10,10,10,10,0],"cal/(mol*K)"),
        H298 = (10,"kcal/mol"),
        S298 = (10,"cal/(mol*K)"),
    ),
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
    label = "six-onesidedouble",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * {Cd,CO} 0 {1,S} {3,S}
3   {Cs,Os} 0 {2,S} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = 'Cyclohexanone',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "Cyclohexanone",
    group = 
"""
1 * CO 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.4,-3.9,-2.3,-1,0.1,0.9,0],"cal/(mol*K)"),
        H298 = (1.29,"kcal/mol"),
        S298 = (19.1,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclohexanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * {Cd,CO} 0 {1,S} {3,S}
3   {Cs,Os} 0 {2,S} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   {Cd,CO} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = '14methylenecyclohexane',
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
    label = "14methylenecyclohexane",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2 * Cd 0 {1,S} {3,S} {7,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {4,S} {6,S} {8,D}
6   Cs 0 {1,S} {5,S}
7   Cd 0 {2,D}
8   Cd 0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6,-5.349,-4.468,-3.521,-2.203,-1.238,0.384],"cal/(mol*K)"),
        H298 = (1.23,"kcal/mol"),
        S298 = (15.7314,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "sixmembd-allsingles-twosidedoubles-ortho",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * {Cd,CO} 0 {1,S} {3,S}
3   {Cd,CO} 0 {2,S} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * {Cd,CO} 0 {1,S} {3,S}
3   {Cs,Os} 0 {2,S} {4,S}
4   {Cd,CO} 0 {3,S} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "six-inringonedouble",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = 'Cyclohexene',
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
    label = "34dihydro12dioxin",
    group = 
"""
1   O  0 {2,S} {6,S}
2   O  0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5 * Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.7,-4.9,-4.3,-3.7,-3.11,-2.62,0.62],"cal/(mol*K)"),
        H298 = (1.07,"kcal/mol"),
        S298 = (20.3,"cal/(mol*K)"),
    ),
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
    label = "36dihydro2hpyran",
    group = 
"""
1 * Cd 0 {2,S} {6,D}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Os 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cd 0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.4,-4,-3,-2.2,-1.5,-0.8,2.3],"cal/(mol*K)"),
        H298 = (1.43,"kcal/mol"),
        S298 = (19.2,"cal/(mol*K)"),
    ),
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
    label = "Cyclohexene",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3 * Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.1,-4.3,-3.3,-2.5,-1.4,-0.7,0.4],"cal/(mol*K)"),
        H298 = (1.17,"kcal/mol"),
        S298 = (21.2114,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclohexene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   O  0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5 * Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.26,-6.496,-5.96,-5.142,-3.74,-2.915,0.529],"cal/(mol*K)"),
        H298 = (3.94,"kcal/mol"),
        S298 = (22.01,"cal/(mol*K)"),
    ),
    shortDesc = u"""3,4-Dihydro-2H-pyran ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "36dihydro12dioxin",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2 * Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Os 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.45,-4.66,-3.81,-3.16,-2.65,-2.68,-1.53],"cal/(mol*K)"),
        H298 = (3.32,"kcal/mol"),
        S298 = (18.72,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "24dihydro13dioxin",
    group = 
"""
1   Cd 0 {2,D} {6,S}
2 * Cd 0 {1,D} {3,S}
3   Cs 0 {2,S} {4,S}
4   Os 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.5,-5.1,-4.2,-3.4,-2.8,-2.3,0.9],"cal/(mol*K)"),
        H298 = (3.1,"kcal/mol"),
        S298 = (20.2,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "23dihydro14dioxin",
    group = 
"""
1   Cd 0 {2,D} {6,S}
2 * Cd 0 {1,D} {3,S}
3   Os 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-6.3,-7.5,-7.5,-6.9,-5.5,-4.9,0.7],"cal/(mol*K)"),
        H298 = (7.9,"kcal/mol"),
        S298 = (19.3,"cal/(mol*K)"),
    ),
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
    label = "124trioxene",
    group = 
"""
1   Os 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4 * Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.51,-5.86,-5.48,-4.98,-4.44,-4.15,-0.75],"cal/(mol*K)"),
        H298 = (6.98,"kcal/mol"),
        S298 = (24.5,"cal/(mol*K)"),
    ),
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
    label = "123trioxene",
    group = 
"""
1   Os 0 {2,S} {6,S}
2   Os 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4 * Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.73,-2.67,-2.62,-2.27,-2.14,-2.08,-0.97],"cal/(mol*K)"),
        H298 = (4,"kcal/mol"),
        S298 = (21.57,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "six-inringtwodouble-13",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4   Cd      0 {3,S} {5,D}
5   Cd      0 {4,D} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = '1,3-Cyclohexadiene',
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
    label = "1,3-Cyclohexadiene",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {3,S}
3 * Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-4.8,-4.7,-4.2,-3.5,-2.5,-1.8,-0.7],"cal/(mol*K)"),
        H298 = (3.78,"kcal/mol"),
        S298 = (23.9824,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3-Cyclohexadiene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "six-inringtwodouble-14",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4   {Cs,Os} 0 {3,S} {5,S}
5   Cd      0 {4,S} {6,D}
6   Cd      0 {1,S} {5,D}
""",
    thermo = '1,4-Cyclohexadiene',
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
    label = "1,4-Cyclohexadiene",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2 * Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.4,-3.2,-2.6,-1.9,-1.2,-0.8,0.2],"cal/(mol*K)"),
        H298 = (0.52,"kcal/mol"),
        S298 = (25.3849,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,4-Cyclohexadiene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "14dioxin",
    group = 
"""
1   Cd 0 {2,D} {6,S}
2   Cd 0 {1,D} {3,S}
3   Os 0 {2,S} {4,S}
4 * Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6   Os 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.9,-7.5,-7.5,-7.5,-6.8,-5.6,-4.2],"cal/(mol*K)"),
        H298 = (11.71,"kcal/mol","+|-",-2.9),
        S298 = (27.6,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "six-inringtwodouble-12",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2 * Cd      0 {1,S} {3,D}
3   C       0 {2,D} {4,D}
4   Cd      0 {3,D} {5,S}
5   {Cs,Os} 0 {4,S} {6,S}
6   {Cs,Os} 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10,10,10,10,10,10,10],"cal/(mol*K)"),
        H298 = (10,"kcal/mol"),
        S298 = (10,"cal/(mol*K)"),
    ),
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
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2   Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4 * {Cd,CO} 0 {3,S} {5,S}
5   Cd      0 {4,S} {6,D}
6   Cd      0 {1,S} {5,D}
""",
    thermo = '14cyclohexadiene3methylene',
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
    label = "25cyclohexadienone",
    group = 
"""
1 * CO 0 {2,S} {6,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.3,-3.342,-3.034,-2.574,-1.976,-1.883,-0.24],"cal/(mol*K)"),
        H298 = (-7.63,"kcal/mol"),
        S298 = (22.5264,"cal/(mol*K)"),
    ),
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
    label = "14cyclohexadiene3methylene",
    group = 
"""
1   Cd 0 {2,D} {6,S}
2   Cd 0 {1,D} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6 * Cd 0 {1,S} {5,S} {7,D}
7   Cd 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.818,-2.82,-2.578,-2.314,-2.091,-1.771,-1.49],"cal/(mol*K)"),
        H298 = (-2.31,"kcal/mol"),
        S298 = (27.775,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "six-oneside-twoindoubles-24",
    group = 
"""
1   {Cs,Os} 0 {2,S} {6,S}
2   Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4   Cd      0 {3,S} {5,D}
5   Cd      0 {4,D} {6,S}
6 * {Cd,CO} 0 {1,S} {5,S}
""",
    thermo = '13cyclohexadiene5methylene',
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
    label = "24cyclohexadienone",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6 * CO 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.46,-4.214,-4.306,-4.049,-3.424,-3.243,0.32],"cal/(mol*K)"),
        H298 = (-10.77,"kcal/mol"),
        S298 = (29.286,"cal/(mol*K)"),
    ),
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
    label = "13cyclohexadiene5methylene",
    group = 
"""
1   Cs 0 {2,S} {6,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6 * Cd 0 {1,S} {5,S} {7,D}
7   Cd 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.437,-6.088,-5.788,-4.994,-3.626,-2.664,-1.187],"cal/(mol*K)"),
        H298 = (-4.78,"kcal/mol"),
        S298 = (28.295,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "six-twoin13-twoout",
    group = 
"""
1   {CO,Cd} 0 {2,S} {6,S}
2   Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4   Cd      0 {3,S} {5,D}
5   Cd      0 {4,D} {6,S}
6 * {Cd,CO} 0 {1,S} {5,S}
""",
    thermo = 'oxylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "fg6",
    group = 
"""
1 * CO 0 {2,S} {6,S}
2   Cd 0 {1,S} {3,S} {7,D}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {1,S} {5,D}
7   Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-5.597,-6.43,-6.331,-5.573,-4.198,-3.361,-1.155],"cal/(mol*K)"),
        H298 = (-4.62,"kcal/mol"),
        S298 = (28.901,"cal/(mol*K)"),
    ),
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
    label = "oxylene",
    group = 
"""
1 * Cd 0 {5,S} {6,S} {8,D}
2   Cd 0 {3,D} {6,S}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D}
6   Cd 0 {1,S} {2,S} {7,D}
7   Cd 0 {6,D}
8   Cd 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.078,-2.192,-2.249,-2.275,-2.541,-2.331,-2.797],"cal/(mol*K)"),
        H298 = (4.16,"kcal/mol"),
        S298 = (32.519,"cal/(mol*K)"),
    ),
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
    label = "obenzoquinone",
    group = 
"""
1 * C  0 {5,S} {6,S} {8,D}
2   Cd 0 {3,D} {6,S}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D}
6   C  0 {1,S} {2,S} {7,D}
7   Od 0 {6,D}
8   Od 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.887,-3.225,-3.233,-2.897,-2.4,-2.365,-0.077],"cal/(mol*K)"),
        H298 = (11,"kcal/mol"),
        S298 = (25.331,"cal/(mol*K)"),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "six-twoin14-twoout",
    group = 
"""
1   {Cd,CO} 0 {2,S} {6,S}
2   Cd      0 {1,S} {3,D}
3   Cd      0 {2,D} {4,S}
4 * {Cd,CO} 0 {3,S} {5,S}
5   Cd      0 {4,S} {6,D}
6   Cd      0 {1,S} {5,D}
""",
    thermo = 'pxylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "pbenzoquinone",
    group = 
"""
1 * CO 0 {4,S} {5,S}
2   Cd 0 {5,D} {6,S}
3   Cd 0 {4,D} {6,S}
4   Cd 0 {1,S} {3,D}
5   Cd 0 {1,S} {2,D}
6   CO 0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.957,-3.282,-3.278,-2.934,-2.427,-2.627,-0.312],"cal/(mol*K)"),
        H298 = (15.52,"kcal/mol"),
        S298 = (24.9239,"cal/(mol*K)"),
    ),
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
    label = "pxylene",
    group = 
"""
1 * Cd 0 {4,S} {5,S} {6,D}
2   Cd 0 {5,D} {7,S}
3   Cd 0 {4,D} {7,S}
4   Cd 0 {1,S} {3,D}
5   Cd 0 {1,S} {2,D}
6   Cd 0 {1,D}
7   Cd 0 {2,S} {3,S} {8,D}
8   Cd 0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.139,-2.309,-2.384,-2.407,-2.643,-2.403,-2.826],"cal/(mol*K)"),
        H298 = (1.16,"kcal/mol"),
        S298 = (31.3499,"cal/(mol*K)"),
    ),
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
    label = "SevenMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {7,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {3,{S,D}} {5,{S,D}}
5   R!H 0 {4,{S,D}} {6,{S,D}}
6   R!H 0 {5,{S,D}} {7,{S,D}}
7   R!H 0 {1,{S,D}} {6,{S,D}}
""",
    thermo = 'Cycloheptane',
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
    label = "Cycloheptane",
    group = 
"""
1 * Cs 0 {2,S} {7,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (6.4,"kcal/mol"),
        S298 = (15.9,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cycloheptane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "Cycloheptene",
    group = 
"""
1 * Cs 0 {2,S} {7,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (5.4,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cycloheptene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "1,3-Cycloheptadiene",
    group = 
"""
1 * Cs 0 {2,S} {7,S}
2   Cs 0 {1,S} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {5,D} {7,S}
7   Cs 0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (6.6,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3-Cycloheptadiene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "1,3,5-Cycloheptatriene",
    group = 
"""
1 * Cs 0 {2,S} {7,S}
2   Cd 0 {1,S} {3,D}
3   Cd 0 {2,D} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {4,D} {6,S}
6   Cd 0 {5,S} {7,D}
7   Cd 0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (4.7,"kcal/mol"),
        S298 = (23.7,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3,5-Cycloheptatriene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "Cycloheptanone",
    group = 
"""
1 * CO 0 {2,S} {7,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (2.3,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cycloheptanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "EightMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {8,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {3,{S,D}} {5,{S,D}}
5   R!H 0 {4,{S,D}} {6,{S,D}}
6   R!H 0 {5,{S,D}} {7,{S,D}}
7   R!H 0 {6,{S,D}} {8,{S,D}}
8   R!H 0 {1,{S,D}} {7,{S,D}}
""",
    thermo = 'Cyclooctane',
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
    label = "Cyclooctane",
    group = 
"""
1 * Cs 0 {2,S} {8,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (9.9,"kcal/mol"),
        S298 = (16.5,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclooctane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "1,3,5-Cyclooctatriene",
    group = 
"""
1 * Cs 0 {2,S} {8,S}
2   Cs 0 {1,S} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {5,D} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (8.9,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""1,3,5-Cyclooctatriene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "Cyclooctatetraene",
    group = 
"""
1 * Cd 0 {2,D} {8,S}
2   Cd 0 {1,D} {3,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {5,D} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (17.1,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclooctatetraene ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "Cyclooctanone",
    group = 
"""
1 * CO 0 {2,S} {8,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (1.5,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclooctanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "NineMember",
    group = 
"""
1 * R!H 0 {2,{S,D}} {9,{S,D}}
2   R!H 0 {1,{S,D}} {3,{S,D}}
3   R!H 0 {2,{S,D}} {4,{S,D}}
4   R!H 0 {3,{S,D}} {5,{S,D}}
5   R!H 0 {4,{S,D}} {6,{S,D}}
6   R!H 0 {5,{S,D}} {7,{S,D}}
7   R!H 0 {6,{S,D}} {8,{S,D}}
8   R!H 0 {7,{S,D}} {9,{S,D}}
9   R!H 0 {1,{S,D}} {8,{S,D}}
""",
    thermo = 'Cyclononane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "Cyclononane",
    group = 
"""
1 * Cs 0 {2,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (12.8,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclononane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "Cyclononanone",
    group = 
"""
1 * CO 0 {2,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (4.7,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclononanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "TenMember",
    group = 
"""
1  * R!H 0 {2,{S,D}} {10,{S,D}}
2    R!H 0 {1,{S,D}} {3,{S,D}}
3    R!H 0 {2,{S,D}} {4,{S,D}}
4    R!H 0 {3,{S,D}} {5,{S,D}}
5    R!H 0 {4,{S,D}} {6,{S,D}}
6    R!H 0 {5,{S,D}} {7,{S,D}}
7    R!H 0 {6,{S,D}} {8,{S,D}}
8    R!H 0 {7,{S,D}} {9,{S,D}}
9    R!H 0 {8,{S,D}} {10,{S,D}}
10   R!H 0 {1,{S,D}} {9,{S,D}}
""",
    thermo = 'Cyclodecane',
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
    label = "Cyclodecane",
    group = 
"""
1  * Cs 0 {2,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (12.6,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclodecane ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "Cyclodecanone",
    group = 
"""
1  * CO 0 {2,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (3.6,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""Cyclodecanone ring BENSON""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

tree(
"""
L1: Ring
    L2: ThreeMember
        L3: Cyclopropane
        L3: Cyclopropene
        L3: Cyclopropadiene
        L3: Cyclopropatriene
        L3: Ethylene_oxide
        L3: dioxirane
        L3: 2(co)oxirane
        L3: cyclopropanedione
        L3: cyclopropenone
        L3: Methylene_cyclopropane
        L3: cyclopropanone
        L3: methylenecyclopropene
        L3: methylenecyclopropanone
        L3: methyleneoxirane
        L3: 12Methylenecyclopropane
    L2: FourMember
        L3: Cyclobutane
        L3: Cyclobutene
        L3: Oxetane
        L3: Beta-Propiolactone
        L3: Cyclobutanone
        L3: 12dioxetane
        L3: dioxerene
        L3: cyclobutadiene
        L3: 4-Methylene-2-oxetanone
        L3: methylenecyclobutane
        L3: 2methyleneoxetane
        L3: 12methylenecyclobutane
    L2: FiveMember
        L3: Cyclopentane
        L3: Cyclopentene
        L3: Cyclopentadiene
        L3: Tetrahydrofuran
        L3: 2,3-Dihydrofuran
        L3: 1,3-Dioxolane
        L3: Furan
        L3: Dihydro-2,5-furandione
        L3: 2,5-Furandione
        L3: Cyclopentanone
        L3: butyrolactone
        L3: 25dihydrofuran
        L3: 12dioxolane
        L3: 12dioxolene
        L3: 123trioxolane
        L3: 124trioxolane
        L3: methylenecyclopentane
        L3: Fulvene
        L3: 12methylenecyclopentane
    L2: SixMember
        L3: sixnosidedouble
            L4: Cyclohexane
            L4: 12dioxane
            L4: 1,3-Dioxane
            L4: 1,4-Dioxane
            L4: 1,3,5-Trioxane
            L4: 124trioxane
            L4: 123trioxane
            L4: Oxane
        L3: six-sidedoubles
            L4: six-onesidedouble
                L5: Cyclohexanone
            L4: sixmembd-allsingles-twosidedoubles-para
                L5: 14methylenecyclohexane
            L4: sixmembd-allsingles-twosidedoubles-ortho
            L4: sixmembd-allsingles-twosidedoubles-meta
        L3: six-inringonedouble
            L4: 34dihydro12dioxin
            L4: 36dihydro2hpyran
            L4: Cyclohexene
            L4: 3,4-Dihydro-2H-pyran
            L4: 36dihydro12dioxin
            L4: 24dihydro13dioxin
            L4: 23dihydro14dioxin
            L4: 124trioxene
            L4: 123trioxene
        L3: six-inringtwodouble-13
            L4: 1,3-Cyclohexadiene
        L3: six-inringtwodouble-14
            L4: 1,4-Cyclohexadiene
            L4: 14dioxin
        L3: six-inringtwodouble-12
        L3: six-oneside-twoindoubles-25
            L4: 25cyclohexadienone
            L4: 14cyclohexadiene3methylene
        L3: six-oneside-twoindoubles-24
            L4: 24cyclohexadienone
            L4: 13cyclohexadiene5methylene
        L3: six-twoin13-twoout
            L4: fg6
            L4: oxylene
            L4: obenzoquinone
        L3: six-twoin14-twoout
            L4: pbenzoquinone
            L4: pxylene
    L2: SevenMember
        L3: Cycloheptane
        L3: Cycloheptene
        L3: 1,3-Cycloheptadiene
        L3: 1,3,5-Cycloheptatriene
        L3: Cycloheptanone
    L2: EightMember
        L3: Cyclooctane
        L3: 1,3,5-Cyclooctatriene
        L3: Cyclooctatetraene
        L3: Cyclooctanone
    L2: NineMember
        L3: Cyclononane
        L3: Cyclononanone
    L2: TenMember
        L3: Cyclodecane
        L3: Cyclodecanone
"""
)

