#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1981ARA/NAG211:1",
    reactant1 = 
"""
1 *2 H 1
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *1 C 1 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (118000,"m^3/(mol*s)"),
        n = 0,
        Ea = (11.391,"kJ/mol"),
        T0 = 1,
        Tmin = (345,"K"),
        Tmax = (449,"K"),
        Pmin = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Arai, H.", "Nagai, S.", "Hatada, M."],
        title = u'Radiolysis of methane containing small amounts of carbon monoxide-formation of organic acids',
        journal = "Radiat. Phys. Chem.",
        volume = "17",
        pages = """211""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981ARA/NAG211:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
Bath gas: N2

===

M. Harper, 9/1/09:

p. 215, Table 2: Estimated values of k2 and the reference value of k3 used for the estimation of k2

Raw data is (Temperature [=] degC, k2 [=] cm3/molecule/s): (72, 3.9E-15), (120, 5.6E-15), (176, 9.8E-15)

Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results in "y = -1.3657x - 29.258" with an R^2 value of 0.9762. The A and Ea values calculated by MRH are thus: A=1.18x10^11 cm3/mol/s, Ea=2.71 kcal/mol, in agreement w/database.

The authors performed an electron beam irradiation of a CH4 gas stream, containing small amounts of CO, in a flow system at 1atm. Authors observe a large decrease in H2 with the addition of small amounts of CO. They assume that this observation must be due to H+CO-->HCO. They propose the following mechanism:

(1) CH4 = H + CH3		k1
(2) H + CO = HCO		k2
(3) H + CH4 = H2 + CH3	k3

The rate of H2 formation:

d[H2]/dt = RM(H2) + k3[H][CH4]

where RM(H2) is the production of H2 through reactions NOT involving H atoms.

Using PSSA on [H]:

d[H]/dt = k1*I*[CH4] - k2[H][CO] - k3[H][CH4] = 0

where I is the dosage rate.

Solving for [H] and substituting into the rate of [H2] formation:

d[H2]/dt = RM(H2) + k1*k3*I*[CH4]^2 / (k2[CO] + k3[CH4])

Subtracting RM(H2) from both sides, taking the inverse of the expression, and rearrangement yields:

{d[H2]/dt - RM(H2)}^-1 = {1 + (k2/k3)*([CO]/[CH4])} / {k1*I*[CH4]}

The authors then introduce this "G-value" (proportional to how they detect H2 and CH4???):

{G(H2) - GM(H2)}^-1 = {1 + (k2/k3)*([CO]/[CH4])} / G(H)

The authors present a plot of {G(H2) - GM(H2)}^-1 vs. [CO]/[CH4] to show it is linear.

*** NOTE: The authors assume a value of GM(H2) of 4.63, according to Okazaki et al. ***

From the plot, they extract a (k2/k3) ratio for each temperature tested. Using the k3 values reported by Sepehrad et al., they estimate a value of k2.

*** NOTE: Value of k3 used: (72C, 1.52E-18 cm3/molecule/s), (120C, 1.51E-17 cm3/molecule/s), (176C, 1.23E-16 cm3/molecule/s). ***
""",
    history = [
        ("Wed Sep  5 14:17:41 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1981ARA/NAG211:1"""),
    ],
)

entry(
    index = 2,
    label = "1978GOR/IVA79:13",
    reactant1 = 
"""
1 *2 H 1
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *1 C 1 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (187000,"m^3/(mol*s)"),
        n = 0,
        Ea = (6.386,"kJ/mol"),
        T0 = 1,
        Tmin = (305,"K"),
        Tmax = (375,"K"),
    ),
    reference = Article(
        authors = ["Gordon, E.B.", "Ivanov, B.I.", "Perminov, A.P.", "Balalaev, V.E."],
        title = u'A Measurement of Formation Rates and Lifetimes of Intermediate Complexes in Reversible Chemical Reactions Involving Hydrogen Atoms',
        journal = "Chem. Phys.",
        volume = "35",
        pages = """79""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978GOR/IVA79:13",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Rate constant is an upper limit.
Bath gas: H2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Other (RF)

===

M. Harper, 9/1/09:

pg.86, Table 1: H atom reactions with CO and SO2. Experimentally determined are line shifts dv and line broadening deltav/2; calculated are rate constants k and complex lifetimes tau_C.

Raw data is (Temperature [=] K, k [=] cm3/molecule/s): (305, >2.5E-14), (375, >4.0E-14)

Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results in "y = -0.768x - 28.802" with an R^2 value of 1. The A and Ea values calculated by MRH are thus: A=1.87x10^11 cm3/mol/s, Ea=1.53 kcal/mol, in agreement w/database.

*** NOTE: MRH interprets table and "H + CO --> HCO" discussion to mean that the rate coefficients reported are LOWER LIMITS. The discussion appears to suggest that the authors suspect oxygen contamination; they further note that the reaction between H-atom and O2 is 10^4 times faster than the H+CO-->HCO rxn. ***
""",
    history = [
        ("Wed Sep  5 14:31:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1978GOR/IVA79:13"""),
    ],
)

