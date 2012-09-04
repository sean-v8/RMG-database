#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/depository"
shortDesc = u""
longDesc = u"""

"""
recommended = False


entry(
    index = 1,
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
        A = (2.3413e+05,"m^3/(mol*s)"),
        n = 0.3321,
        Ea = (-4.4497,"kJ/mol"),
        T0 = 1,
        Tmin = (250,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Zador, J.", "Fernandes, R.X.", "Georgievskii, Y.", "Meloni, G.", "Taatjes, C.A.", "Miller, J.A."],
        title = u'The reaction of hydroxyethyl radicals with O2: A theoretical analysis and experimental product study',
        journal = "Proc. Combust. Inst.",
        volume = "32",
        pages = """271-277""",
        year = "2009",
        url = "http://dx.doi.org/10.1016/j.proci.2008.05.020",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
(Essentially) Pressure-independent rate coefficient

Authors computed the following PES:
	Entrance channel: CH3CHOH+O2
	Product channels: CH3CHO+HO2, CH2CHOH+HO2, 2-oxiranol+OH
	Wells: CH3CH(OO)OH, CH3CH(OOH)O, CH2CH(OOH)OH, CH3CHO--HO2 (hydrogen-bonding)

Geometry optimizations and IRC scans were done using B3LYP/6-311++G(d,p). Single-point energies were computed using RQCISD(T)/cc-pV(INF)Z. For stationary points with large T1 diagnostics, CASPT2 and MRCI with Davidson corrections were employed.

The rate coefficients were computed using RRKM/ME techniques developed by Miller and Klippenstein. Low-frequency torsional modes were treated as hindered rotors using Pitzer-Gwinn; the scan was performed at B3LYP/6-311++G(d,p) and fit to a Fourier series. An asymmetric Eckart tunneling correction was employed.  A simple exponential-down model was used, where <delta_Ed> = 100 * (T/298) cm-1. Lennard-Jones parameters for the C2H5O3 isomers were assumed to be sigma = 4.31 Angstroms and epsilon/kB = 297 K.

The authors solved the PES using VRC-TST, with the following exceptions, in Variflex:
· The TS between CH3CH(OO)OH and CH3CHO--HO2 was treated as the product channel CH3CHO+HO2
· The CH3CHO--HO2 well, and its TS to the product channel CH3CHO+HO2, were not included
· The CH3CH(OOH)O well, and its TS to the well CH3CH(OO)OH, were not included

The authors calculated k1,zero (collisionless) and k1,inf (high-pressure-limit) over the range 250-1000 K. The two rate coefficients were similar over most of the temperature range, suggesting a pressure-independent rate coefficient is adequate. The value reported in RMG is the high-pressure limit.

The authors conclude that the CH3CHO+HO2 product channel dominates at all temperatures and pressures. Hence, the entire computed k1,inf is assigned to the reaction CH3CHOH+O2=HO2+CH3CHO. Furthermore, the authors detected a strong signal from the m/z = 44 PIE scan; they concluded this was due to the CH3CHO and CH2CHOH isomers.

This rate coefficient recommendation is up to 3x slower than the previous RMG-employed recommendation, over the valid temperature range.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Tue Sep  4 15:50:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Moved from rules to depository."""),
    ],
)

