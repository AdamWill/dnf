# Copyright (C) 2018 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

import dnf


class ListOptionTest(unittest.TestCase):

    def setUp(self):
        self.conf = dnf.conf.MainConf()

    def test_iadd(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var += ["b", "c"]
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])
        self.assertEqual(var, ["a", "b", "c"])

    def test_iadd_tuple(self):
        self.conf.pluginpath = ("a", )
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var += ("b", "c")
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])
        self.assertEqual(var, ["a", "b", "c"])

    def test_imul(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var *= 3
        self.assertEqual(self.conf.pluginpath, ["a", "a", "a"])
        self.assertEqual(var, ["a", "a", "a"])

    def test_setitem(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var[0] = "b"
        self.assertEqual(self.conf.pluginpath, ["b"])
        self.assertEqual(var, ["b"])

    def test_append(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var.append("b")
        self.assertEqual(self.conf.pluginpath, ["a", "b"])
        self.assertEqual(var, ["a", "b"])

    def test_clear(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var.clear()
        self.assertEqual(self.conf.pluginpath, [])
        self.assertEqual(var, [])

    def test_extend(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var.extend(["b", "c"])
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])
        self.assertEqual(var, ["a", "b", "c"])

    def test_insert(self):
        self.conf.pluginpath = ["a"]
        self.assertEqual(self.conf.pluginpath, ["a"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a"])

        var.insert(0, "b")
        self.assertEqual(self.conf.pluginpath, ["b", "a"])
        self.assertEqual(var, ["b", "a"])

    def test_pop(self):
        self.conf.pluginpath = ["a", "b", "c"]
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a", "b", "c"])

        var.pop()
        self.assertEqual(self.conf.pluginpath, ["a", "b"])
        self.assertEqual(var, ["a", "b"])

    def test_remove(self):
        self.conf.pluginpath = ["a", "b", "c"]
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a", "b", "c"])

        var.remove("b")
        self.assertEqual(self.conf.pluginpath, ["a", "c"])
        self.assertEqual(var, ["a", "c"])

    def test_reverse(self):
        self.conf.pluginpath = ["a", "b", "c"]
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a", "b", "c"])

        var.reverse()
        self.assertEqual(self.conf.pluginpath, ["c", "b", "a"])
        self.assertEqual(var, ["c", "b", "a"])

    def test_sort(self):
        self.conf.pluginpath = ["a", "c", "b"]
        self.assertEqual(self.conf.pluginpath, ["a", "c", "b"])

        var = self.conf.pluginpath
        self.assertEqual(var, ["a", "c", "b"])

        var.sort()
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c"])
        self.assertEqual(var, ["a", "b", "c"])

    def test_multiple_refs(self):
        self.conf.pluginpath = ["a", "b", "c"]
        ppath = self.conf.pluginpath
        # should be two refs to the same object
        self.assertIs(ppath, self.conf.pluginpath)
        ppath.append("d")
        # change should apply to both
        self.assertEqual(ppath, self.conf.pluginpath)
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c", "d"])
        self.conf.pluginpath.append("e")
        # again, change should apply to both
        self.assertEqual(ppath, self.conf.pluginpath)
        self.assertEqual(self.conf.pluginpath, ["a", "b", "c", "d", "e"])
        # reassign attribute
        self.conf.pluginpath = ["1", "2", "3"]
        # reference should *NO LONGER* be to the same object
        self.assertIsNot(ppath, self.conf.pluginpath)
        ppath.append("f")
        # change to ppath should not affect attribute
        self.assertEqual(ppath, ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(self.conf.pluginpath, ["1", "2", "3"])
