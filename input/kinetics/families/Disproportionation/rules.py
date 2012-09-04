#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 485,
    label = "Y_rad_birad;XH_Rrad",
    group1 = "OR{Y_1centerbirad, Y_rad}",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
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
    index = 487,
    label = "O2_birad;Cmethyl_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.23e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (15.99,"kcal/mol"),
        Tmin = (700,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'sp') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 501,
    label = "O2_birad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.5825e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (14.85,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (900,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'ss') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 543,
    label = "C_rad/H2/Cd;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C3H5 + CH2OH --> CH2O + C3H6

pg.267: Discussion on evaluated data

Entry 47,39: No data available at the time.  Author notes that combination of these two

reactants will form 3-butene-1-ol which should decompose under combustion conditions
to form C3H6 + CH2O (same products).  The author therefore recommends a rate
coefficient of 3x10^-11 cm3/molecule/s.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 544,
    label = "C_rad/H2/O;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.82e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH2OH + CH2OH --> CH3OH + CH2O

pg. 506: Discussion on evaluated data

Entry 39,39 (b): CH2OH + CH2OH --> CH3OH + CH2O

Meier, et al. (1985) measured the rate of addition + disproportionation.  Tsang estimates

a disproportionation to combination ratio of 0.5
NOTE: Rate coefficient given in table at beginning of reference (summarizing all data

presented) gives k_a+b = 2.4x10^-11, leading to k_b = 8x10^-12.  NIST's online
database (kinetics.nist.gov) reports this number as well.  However, the discussion
on pg. 506 suggests k_a+b = 1.5x10^-11, leading to k_b = 5x10^-12.
MRH 30-Aug-2009

*** NEED TO INVESTIGATE ***
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 545,
    label = "C_rad/H/NonDeC;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.35e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review: CH2OH + i-C3H7 = C3H8 + CH2O

pg. 945: Discussion on evaluated data

Entry 42,39 (b): No data available at the time.  Author suggests rate coefficient based

on rxn C2H5+i-C3H7=C3H8+C2H4, namely 3.9x10^-12 cm3/molecule/s
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 546,
    label = "C_rad/Cs3;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.47e+14,"cm^3/(mol*s)","*|/",3),
        n = -0.75,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: t-C4H9 + CH2OH = CH2O + i-C4H10

pg. 44: Discussion on evaluated data

Entry 44,39 (a): No data available at the time.  Author estimates the addition rxn rate

coefficient based on the rate for t-C4H9+C2H5-->adduct.  The author uses a
disproportionation-to-addition ratio of 0.52 to obtain the reported rate coefficient
expression.
*** NOTE: Previous value in RMG was for k_c (the addition rxn).  I have changed it to match

the rate for the disproportionation rxn. ***
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 547,
    label = "Cd_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH2OH + C2H3 --> C2H4 + CH2O

pg. 503: Discussion on evaluated data

Entry 39,19 (a): CH2OH + C2H3 --> C2H4 + CH2O

Author suggests a disproportionation rate coefficient near the collision limit, due

to rxn's exothermicity.  No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 548,
    label = "Ct_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,T}
2    C 0 {1,T}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.61e+13,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H + CH2OH --> C2H2 + CH2O

pg. 504: Discussion on evaluated data

Entry 39,21 (a): CH2OH + C2H --> C2H2 + CH2O

Author suggest a disproportionation rate coefficient of 6.0x10^-11 cm3/molecule/s, due

to very exothermic rxn.  No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 549,
    label = "CO_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+14,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: HCO + CH2OH --> CH2O + CH2O

pg. 500: Discussion on evaluated data

Entry 39,15 (b): CH2OH + HCO --> 2 CH2O

Author estimates a disproportionation rate coefficient of 3x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 550,
    label = "O_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: OH + CH2OH --> H2O + CH2O

pg. 497: Discussion on evaluated data

Entry 39,6: CH2OH + OH --> H2O + CH2O

Author estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 551,
    label = "O_rad/NonDeC;O_Csrad",
    group1 = 
"""
1 *1 O  1 {2,S}
2    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH3O + CH2OH --> CH3OH + CH2O

pg. 505: Discussion on evaluated data

Entry 39,24: CH2OH + CH3O --> CH3OH + CH2O

Author estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 552,
    label = "O_rad/NonDeO;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: HO2 + CH2OH --> CH3OH + H2O2

pg. 498: Discussion on evaluated data

Entry 39,7: CH2OH + HO2 --> H2O2 + CH2O

Author recommends a disproportionation rate coefficient of 2x10^-11 cm3/molecules/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 600,
    label = "O2_birad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.3413e+11,"cm^3/(mol*s)"),
        n = 0.3321,
        alpha = 0,
        E0 = (-1.0635,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Zador et al.""",
    longDesc = 
u"""
(Essentially) Pressure-independent rate coefficient for CH3CHOH + O2 = HO2 + CH3CHO [Zador2009]_.

Authors computed the following PES:
	Entrance channel: CH3CHOH+O2
	Product channels: CH3CHO+HO2, CH2CHOH+HO2, 2-oxiranol+OH
	Wells: CH3CH(OO)OH, CH3CH(OOH)O, CH2CH(OOH)OH, CH3CHO--HO2 (hydrogen-bonding)
Geometry optimizations and IRC scans were done using B3LYP/6-311++G(d,p).  Single-point energies were computed using
 RQCISD(T)/cc-pV(INF)Z.  For stationary points with large T1 diagnostics, CASPT2 and MRCI with Davidson corrections
 were employed.
The rate coefficients were computed using RRKM/ME techniques developed by Miller and Klippenstein.  Low-frequency
 torsional modes were treated as hindered rotors using Pitzer-Gwinn; the scan was performed at B3LYP/6-311++G(d,p) and fit
 to a Fourier series.  An asymmetric Eckart tunneling correction was employed.  A simple exponential-down model was used,
 where <delta_Ed> = 100 * (T/298) cm-1.  Lennard-Jones parameters for the C2H5O3 isomers were assumed to be sigma = 4.31 Angstroms
 and epsilon/kB = 297 K.
The authors solved the PES using VRC-TST, with the following exceptions, in Variflex:
	- The TS between CH3CH(OO)OH and CH3CHO--HO2 was treated as the product channel CH3CHO+HO2
	- The CH3CHO--HO2 well, and its TS to the product channel CH3CHO+HO2, were not included
	- The CH3CH(OOH)O well, and its TS to the well CH3CH(OO)OH, were not included
The authors calculated k1,zero (collisionless) and k1,inf (high-pressure-limit) over the range 250-1000 K.
 The two rate coefficients were similar over most of the temperature range, suggesting a pressure-independent rate
 coefficient is adequate.  The value reported in RMG is the high-pressure limit.
The authors conclude that the CH3CHO+HO2 product channel dominates at all temperatures and pressures.  Hence, the
 entire computed k1,inf is assigned to the reaction CH3CHOH+O2=HO2+CH3CHO.  Furthermore, the authors detected a strong
 signal from the m/z = 44 PIE scan; they concluded this was due to the CH3CHO and CH2CHOH isomers.
This rate coefficient recommendation is up to 3x slower than the previous RMG-employed recommendation, over the valid
 temperature range.
 
12-OCT-2010 amendement (MRH): Divided pre-exponential A factor by 2 (to account for symmetry of oxygen).

.. [Zador2009] J. Zador, R.X. Fernandes, Y. Georgievskii, G. Meloni, C.A. Taatjes, J.A. Miller
	"The reaction of hydroxyethyl radicals with O2: A theoretical analysis of experimental product study"
	Proc. Combust. Inst. 32 (2009) 271-277
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 20001,
    label = "O2_birad;XH_Rrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

