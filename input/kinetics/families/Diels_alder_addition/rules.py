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

entry(
    index = 611,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_HDe",
    group1 = 
"""
1 *3 Cd     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 Cd     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {4,S}
8    H      0 {4,S}
""",
    group2 = 
"""
1 *4 Cd 0 {2,S} {3,S}
2 *5 Cd 0 {1,S} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.69,"kcal/mol"),
        Tmin = (352,"K"),
        Tmax = (423,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 612,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_HNd",
    group1 = 
"""
1 *3 Cd     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 Cd     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {4,S}
8    H      0 {4,S}
""",
    group2 = 
"""
1 *4 Cd 0 {2,S} {3,S}
2 *5 Cd 0 {1,S} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.69,"kcal/mol"),
        Tmin = (352,"K"),
        Tmax = (423,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

