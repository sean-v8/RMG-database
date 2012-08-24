#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an old RMG-Java database and saves it to
the input directory in the new RMG-Py format.
"""

import math
import os
import subprocess
import sys
import time

from rmgpy.data.rmg import RMGDatabase

###############################################################################


def main():

    if len(sys.argv) != 2:
        raise Exception('You must provide the path to a folder containing '
                        'a valid RMG_database directory.')

    importDatabase(sys.argv[1])


###############################################################################


def importDatabase(oldPath):

    print 'Loading old RMG-Java database...'
    database = RMGDatabase()
    database.loadOld(os.path.join(oldPath, 'RMG_database'))

    print 'Setting history...'
    setHistory(database, user=getUsername())

    print 'Saving new RMG-Py database...'
    database.save('input')


###############################################################################


def getUsername():
    """
    Grab the user's name and email from git if possible.
    """

    try:
        name = subprocess.check_output(['git', 'config',
                                        '--get', 'user.name']).strip()
    except:
        print "Couldn't find user.name in git config."
        name = os.getlogin()

    try:
        email = subprocess.check_output(['git', 'config',
                                        '--get', 'user.email']).strip()
    except:
        print "Couldn't find user.email in git config."
        email = '{0}@{1}'.format(os.getlogin(), os.uname()[1])

    return '{0} <{1}>'.format(name, email)


###############################################################################


def setHistory(database, user):
    """
    Update the history of every entry in the database.
    """

    event = [time.asctime(),
             user,
             'action',
             'Imported from the old RMG database.'
             ]

    # Thermo
    for depository in database.thermo.depository.values():
        for entry in depository.entries.values():
            entry.history.append(event)
    for library in database.thermo.libraries.values():
        for entry in library.entries.values():
            entry.history.append(event)
    for groups in database.thermo.groups.values():
        for entry in groups.entries.values():
            entry.history.append(event)

    # Kinetics
    for family in database.kinetics.families.values():
        for entry in family.groups.entries.values():
            entry.history.append(event)
        for entry in family.rules.entries.values():
            entry.history.append(event)
        for depository in family.depositories.values():
            for entry in depository.entries.values():
                entry.history.append(event)
    for library in database.kinetics.libraries.values():
        for entry in library.entries.values():
            entry.history.append(event)

    # States
    groups = database.states.groups
    for entry in groups.entries.values():
        entry.history.append(event)

    # Forbidden structures
    for entry in database.forbiddenStructures.entries.values():
        entry.history.append(event)


###############################################################################


if __name__ == '__main__':

    main()
