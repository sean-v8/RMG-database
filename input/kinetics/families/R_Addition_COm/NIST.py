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

entry(
    index = 3,
    label = "1994BAU/COB847-1033:55",
    reactant1 = 
"""
1 *2 C 1
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S}
2 *1 C 1 {1,S} {3,D}
3    O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (506000,"m^3/(mol*s)","*|/",3.16),
        n = 0,
        Ea = (28.768,"kJ/mol"),
        T0 = 1,
        Tmin = (300,"K"),
        Tmax = (500,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:55",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 3.1600001

===

M. Harper, 8/31/09: RMG stores k_inf rate coefficient. The recommended rate coefficient comes from the preferred (from this reference) rxn rate and the equilibrium constant (from Bencsura et al.). (p. 973-974)
""",
    history = [
        ("Wed Sep  5 14:37:21 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:55"""),
    ],
)

entry(
    index = 4,
    label = "1986TSA/HAM1087:88",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 1 {1,S} {4,D}
4    O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000,"m^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (20.121,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:88",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 2.0
Bath gas: N2

===

M. Harper, 8/28/09: Recommended data (in the form of k_inf) comes from expression given by Watkins and Thompson. (p. 1178-1179) Fall-off corrections and collision efficiencies are also available (although we do not store them in RMG_database).
""",
    history = [
        ("Wed Sep  5 14:44:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:88"""),
    ],
)

entry(
    index = 5,
    label = "1986TSA/HAM1087:84",
    reactant1 = 
"""
1    C 0 {2,D}
2 *2 C 1 {1,D}
""",
    reactant2 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 1 {1,S} {4,D}
4    O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000,"m^3/(mol*s)","*|/",5),
        n = 0,
        Ea = (20.121,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:84",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
Uncertainty: 5.0
Bath gas: N2

===

M. Harper, 8/28/09: Recommended data (in the form of k_inf) is assumed to be equal to the rate expression for CO+C2H5-->H3C-CH2-C=O. Authors note the rxn is in the fall-off region under all conditions. (p. 1198-1199) Fall-off corrections and collision efficiencies are also available (although we do not store them in RMG_database).
""",
    history = [
        ("Wed Sep  5 14:51:24 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:84"""),
    ],
)

entry(
    index = 6,
    label = "2000NAM/XIA1233-1239:1",
    reactant1 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    reactant2 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *2 C 1 {4,B} {5,B}
""",
    product1 = 
"""
1 *2 C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *1 C 1 {1,S} {8,D}
8    O 0 {7,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (851000,"m^3/(mol*s)","+|-",280000),
        n = 0,
        Ea = (12.53,"kJ/mol","+|-",0.91),
        T0 = 1,
        Tmin = (295,"K"),
        Tmax = (500,"K"),
        Pmin = (1600,"Pa"),
        Pmax = (16000,"Pa"),
    ),
    reference = Article(
        authors = ["Nam, G.-J.", "Xia, W.", "Park, J.", "Lin, M.C."],
        title = u'The Reaction of C5H5 with CO: Kinetic Measurement and Theoretical Correlation with the Reverse Process',
        journal = "J. Phys. Chem. A",
        volume = "104",
        pages = """1233-1239""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000NAM/XIA1233-1239:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Bath gas: Ar
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Other
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

The cavity ring-down spectroscopic technique has been used. Phenyl radicals are produced from 248 nm photolysis of C6H5NO.  The time profile of phenyl radicals is directly probed at 504.8 nm. Experimental results are compared with the results of RRKM theory using the transition state parameters computed by the MP2 method with the 6-31G(d,p) basis set. A heat of formation of 32?.5 kcal/mol has been derived for C6H5CO.

===

M. Harper, 9/1/09:

Authors use a Beer-Lambert law type expression:

1/tc = 1/tc_0 + (c*l*epsilon / n*L) * [A](t)

where tc and tc_0 are the decay times of the injected probing photons in the presence and absence of absorbing species, c is the speed of light, l is the length of the absorbing medium, epsilon is the extinction coefficient, n is the refractive index of the medium, L is the length of the cavity, and [A](t) is the concentration of the absorbing species at time t. Assuming a simple association rxn, A decays exponentially: [A](t) = [A](0)*exp(-k'*t).

Combining this with the previous expression yields:

ln(1/tc - 1/tc_0) = B - k'*t    eq. (*)

However, the authors assume the reverse rxn will be significant (C6H5 + CO <--> C6H5CO). Thus, they propose the following rate equation:

dx/dt = kf([A](0) - x)[CO] - kr*x

where x is defined as [A](0) - [A](t), [A](t) is the concentration of the C6H5CO radical at time t, kf is the rate coefficient for C6H5+CO-->C6H5CO, and kr is the rate coefficient for C6H5CO-->C6H5+CO. Integrating the above differential equation, assuming constant [CO], yields:

x = (a/b) * (1-exp(-b*t))

where a = kf*[CO]*[A](0) and b = kf*[CO] + kr. Recalling that x = [A](0) - [A](t):

[A](t) = [A](0) - x = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b

Substituting this into the Beer-Lambert law expression:

1/tc - 1/tc_0 = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b    eq. (**)

C6H5 radical was generated from C6H5NO. The rate coefficient for the C6H5+CO reaction was measured in the temperature range 295-500K at 12-120 torr, with Ar as the carrier gas. The authors note that plots of ln(1/tc - 1/tc_0) vs. t exhibited linear behavior (for a given Temperature and [CO] concentration). The slope of the plot, computed using a "standard weighted least-squares analysis", yielded k', the pseudo first-order rate coefficient {eq. (*)}. The authors also note that above 400K, the plots became nonlinear with time, which the authors attribute to C6H5 re-generation from the reverse rxn C6H5CO --> C6H5 + CO. This data was analyzed using eq. (**), to yield b. The pseudo first-order rate coefficients (either k' or b) were plotted against [CO] to yield the second-order rate coefficient for C6H5+CO. The authors note that the evaluated kf calculated above and below 400K differ greatly. The authors performed a "weighted least-squares analysis" on all data to arrive at the reported bimolecular rate coefficient:

k1 = 10^11.93+/-0.14 * exp[(-1507+/-109)/T] cm3/mole/s

valid from 295-500K at 40 torr Ar pressure.

The authors also investigated the pressure dependence of the rxn at 347K, from 12-120 torr. At 347K, the authors do not observe any significant difference. However, at higher temperatures, pressure effects become significant. The authors performed RRKM calculations to account for falloff effects, and report the adjusted second-order rate coefficient as:

k1_inf = 10^12.17+/-0.18 * exp[(-1676+/-149)/T] cm3/mole/s
""",
    history = [
        ("Wed Sep  5 15:02:44 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2000NAM/XIA1233-1239:1"""),
    ],
)

entry(
    index = 7,
    label = "1999WAN/HOU8021-8029:14",
    reactant1 = 
"""
1 *1 C 2T {2,D}
2    O 0  {1,D}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *1 C 1 {2,S} {4,D}
4    O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18.7,"m^3/(mol*s)"),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = 1,
        Tmin = (2500,"K"),
        Pmin = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Wang, B.", "Hou, H.", "Gu. Y."],
        title = u'Ab Initio/Density Functional Theory and Multichannel RRKM Calculations for the CH3O + CO Reaction',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """8021-8029""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999WAN/HOU8021-8029:14",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
Pressure dependence: Rate constant is pressure dependent
""",
    history = [
        ("Wed Sep  5 15:17:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1999WAN/HOU8021-8029:14"""),
    ],
)

