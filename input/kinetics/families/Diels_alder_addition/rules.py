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
    index = 599,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 600,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.09e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (28.81,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 601,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7.08e+08,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.23,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 602,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (28.62,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 603,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.72e+08,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 604,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.95e+08,"cm^3/(mol*s)","*|/",1.1),
        n = 0,
        alpha = 0,
        E0 = (28.42,"kcal/mol"),
        Tmin = (486,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 605,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_2H",
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
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 606,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
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
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 607,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
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
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+08,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.87,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2beta, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 608,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
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
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.15e+10,"cm^3/(mol*s)","*|/",1.05),
        n = 0,
        alpha = 0,
        E0 = (26.83,"kcal/mol"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 609,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
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
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.8e+09,"cm^3/(mol*s)","*|/",1.05),
        n = 0,
        alpha = 0,
        E0 = (24.84,"kcal/mol"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 610,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_2H",
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
6    H             0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
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

