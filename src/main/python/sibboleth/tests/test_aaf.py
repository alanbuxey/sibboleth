#############################################################################
#
# Copyright (c) 2011 Russell Sim <russell.sim@gmail.com> Contributors.
# Copyright (c) 2009 Victorian Partnership for Advanced Computing Ltd and
# Contributors.
# All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import unittest
import sibboleth
from sibboleth.shibboleth import Shibboleth
from sibboleth.credentials import Idp, SimpleCredentialManager, \
     AuthenticationException
import inspect

from os import path, environ
here = path.join(path.dirname(inspect.getsourcefile(sibboleth)), 'tests/')

aaf_sp_url = 'https://slcs1.arcs.org.au/SLCS/login'


class IdpListException(Exception):
    pass


class ListIDPs(Idp):

    def set_idps(self, idps):
        """
        set the list of possible idps
        """
        self.raw_idps = idps
        self.idps = idps.keys()
        self.idps.sort()
        raise IdpListException("Exit Auth Chain")


idps = ListIDPs()
c = SimpleCredentialManager('ARCS_test', 'ARCS_test')
shib = Shibboleth(idps, c)
try:
    shib.openurl(aaf_sp_url)
except IdpListException:
    pass


class TestShibboleth(unittest.TestCase):

    def setUp(self):
        pass

    def test_pass(self):
        """this test exists to prevent and error from the class
        defining no tests
        """
        pass


def add_test(cls, i):
    def tmpl_test_idp(self):
        idps = Idp(i)
        c = SimpleCredentialManager('ARCS_test', 'ARCS_test')
        shib = Shibboleth(idps, c)
        self.assertRaises(AuthenticationException, shib.openurl, aaf_sp_url)
    tmpl_test_idp.__doc__ = "%s Idp test function" % i
    tmpl_test_idp.__name__ = "test_idp_%s" % i
    setattr(cls, tmpl_test_idp.__name__, tmpl_test_idp)


for i in idps.idps:
    if i.startswith('Bootstrapped IdP utas.edu.au'):
        continue  # idp doesn't respond
    if i.startswith('Bootstrapped IdP aarnet.edu.au'):
        continue  # idp doesn't respond
    if i.startswith('Bootstrapped IdP csiro.au'):
        continue  # idp doesn't exist
    if i.startswith('Bootstrapped IdP unimelb.edu.au'):
        continue  # uses basic auth and just hangs for ages
    if i.startswith('Murdoch University'):
        continue  # invalid html
    if not 'SIBBOLETH_TEST' in environ:
        continue

    add_test(TestShibboleth, i)

del add_test
