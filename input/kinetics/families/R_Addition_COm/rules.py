#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = u""
longDesc = u"""
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
recommended = True

entry(
    index = 416,
    label = "COm;Y_rad",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 R 1
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5,"kcal/mol"),
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

entry(
    index = 421,
    label = "COm;Cd_pri_rad",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.51e+11,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (4.81,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J.Phys. Chem. Ref. Data 1986, 15, 1087.
CO + C2H3 --> CH2=CHCO.

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,14.

Verified by Karma James

NOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)

pg. 1198-1199: Discussion of evaluated data

Recommended data (in the form of k_inf) is assumed to be equal to the rate expression

for CO+C2H5-->H3C-CH2-C=O.  Authors note the rxn is in the fall-off region
under all conditions.
Fall-off corrections and collision efficiencies are also available
(although we do not store them in RMG_database).
MRH 28-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 422,
    label = "COm;Cb_rad",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1.48e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        alpha = 0,
        E0 = (3.33,"kcal/mol","+|-",0.3),
        Tmin = (295,"K"),
        Tmax = (500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Nam et al [104].""",
    longDesc = 
u"""
[104] Nam, G.-J.; Xia, W.; Park, J.; Lin, M. Phys. Chem. A 2000, 104, 1233.	
Phenyl + CO --> Benzoyl. Original deltaA = 2.8E+11

Absolute value measrued directly. Rate constant is high pressure limit. 

Pressure 0.02-0.16 atm. Excitation: flash photolysis, analysis: Vis-UV absorption.

Authors use a Beer-Lambert law type expression:

1/tc = 1/tc_0 + (c*l*epsilon / n*L) * [A](t)
where tc and tc_0 are the decay times of the injected probing photons in the presence

and absence of absorbing species, c is the speed of light, l is the length of the
absorbing medium, epsilon is the extinction coefficient, n is the refractive index
of the medium, L is the length of the cavity, and [A](t) is the concentration of
the absorbing species at time t.
Assuming a simple association rxn, A decays exponentially: [A](t) = [A](0)*exp(-k'*t).

Combining this with the previous expression yields:
ln(1/tc - 1/tc_0) = B - k'*t		eq. (*)
However, the authors assume the reverse rxn will be significant (C6H5 + CO <--> C6H5CO).

Thus, they propose the following rate equation:
dx/dt = kf([A](0) - x)[CO] - kr*x
where x is defined as [A](0) - [A](t), [A](t) is the concentration of
the C6H5CO radical at time t, kf is the rate coefficient for C6H5+CO-->C6H5CO,
and kr is the rate coefficient for C6H5CO-->C6H5+CO.
Integrating the above differential equation, assuming constant [CO], yields:

x = (a/b) * (1-exp(-b*t))
where a = kf*[CO]*[A](0) and b = kf*[CO] + kr
Recalling that x = [A](0) - [A](t):

[A](t) = [A](0) - x = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b
Substituting this into the Beer-Lambert law expression:

1/tc - 1/tc_0 = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b		eq. (**)
C6H5 radical was generated from C6H5NO.  The rate coefficient for the C6H5+CO reaction

was measured in the temperature range 295-500K at 12-120 torr, with Ar as the
carrier gas.  The authors note that plots of ln(1/tc - 1/tc_0) vs. t exhibited
linear behavior (for a given Temperature and [CO] concentration).  The slope of
the plot, computed using a "standard weighted least-squares analysis", yielded k',
the pseudo first-order rate coefficient {eq. (*)}.  The authors also note that above 400K,
the plots became nonlinear with time, which the authors attribute to C6H5
re-generation from the reverse rxn C6H5CO --> C6H5 + CO.  This data was analyzed
using eq. (**), to yield b.  The pseudo first-order rate coefficients (either k' or b)
were plotted against [CO] to yield the second-order rate coefficient for C6H5+CO.
The authors note that the evaluated kf calculated above and below 400K differ greatly.
The authors performed a "weighted least-squares analysis" on all data to arrive at
the reported bimolecular rate coefficient:
k1 = 10^11.93+/-0.14 * exp[(-1507+/-109)/T] cm3/mole/s
valid from 295-500K at 40 torr Ar pressure.
The authors also investigated the pressure dependence of the rxn at 347K, from 12-120 torr.

At 347K, the authors do not observe any significant difference.  However, at higher
temperatures, pressure effects become significant.  The authors performed RRKM
calculations to account for falloff effects, and report the adjusted second-order
rate coefficient as:
k1_inf = 10^12.17+/-0.18 * exp[(-1676+/-149)/T] cm3/mole/s
*** NOTE: RMG database was storing reported k1 value.  MRH has changed this so that RMG

now stores the k1_inf value. ***
MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 423,
    label = "COm;O_rad/NonDe",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 O      1 {2,S}
2    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.41e+07,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Wang et al. [105].""",
    longDesc = 
u"""
[105] Wang, B.; Hou, H.; Gu, Y. Phys. Chem. A 1999, 103, 8021.
RRK(M) extrapolation. CH3O + CO --> CH3OCO, 250K and 2500K

Data stored in RMG appears to be linear fit of the following data, presented on pg.8028

in the right-hand column under the section heading "3.Implications for Atmospheric
and Combustion Chemistry.": (250K, 5torr, 1.39x10^-19 cm3/molecule/s) and 
(2500K, 760torr, 3.10x10^-17 cm3/molecule/s).
Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results

in "y = -1.502x - 37.412" with an R^2 value of 1.  The A and Ea values calculated
by MRH are thus: A=3.40x10^7 cm3/mol/s, Ea=2.98 kcal/mol, in agreement w/database.
MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 424,
    label = "COm;C_methyl",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.06e+06,"cm^3/(mol*s)","*|/",3),
        n = 1.89,
        alpha = 0,
        E0 = (4.82,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3 + CO = CH3CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

Methyl (doublet): external symmetry number (EXTSYM) = 6
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
CH3CO (doublet): EXTSYM = 1, one hindered rotor (methyl group, symmetry = 3)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 425,
    label = "COm;CH2CH3",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (7.7e+07,"cm^3/(mol*s)","*|/",3),
        n = 1.37,
        alpha = 0,
        E0 = (5.69,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2 + CO = CH3CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

Ethyl (doublet): external symmetry number (EXTSYM) = 1, one hindered rotor (methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
CH3CH2CO (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 426,
    label = "COm;CH2CH2CH3",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     H 0 {4,S}
7     C 0 {4,S} {8,S} {9,S} {10,S}
8     H 0 {7,S}
9     H 0 {7,S}
10    H 0 {7,S}
""",
    kinetics = ArrheniusEP(
        A = (6.51e+10,"cm^3/(mol*s)","*|/",3),
        n = 0.45,
        alpha = 0,
        E0 = (6.68,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2CH2 + CO = CH3CH2CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

n-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 4)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 2; propyl group, symmetry = 1)
CH3CH2CH2CO (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "COm;CH[CH3]2",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     C 0 {1,S} {5,S} {6,S} {7,S}
4     C 0 {1,S} {8,S} {9,S} {10,S}
5     H 0 {3,S}
6     H 0 {3,S}
7     H 0 {3,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (8.61e+07,"cm^3/(mol*s)","*|/",3),
        n = 1.36,
        alpha = 0,
        E0 = (4.8,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CHCH3 + CO = CH3CH(CO)CH3
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

iso-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 6; methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
CH3CH(CO)CH3 (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

