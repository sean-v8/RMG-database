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

