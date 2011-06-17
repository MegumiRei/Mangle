#!/usr/bin/env python

# Copyright (C) 2010  Alex Yatskov
# Copyright (C) 2011  Stanislav (proDOOMman) Kosolapov <prodoomman@gmail.com>
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
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QTranslator
import locale

from book import MainWindowBook

application = QtGui.QApplication(sys.argv)
tr = QTranslator()
tr.load("mangle_%s.qm"%locale.getlocale()[0])
application.installTranslator(tr)
filename = sys.argv[1] if len(sys.argv) > 1 else None
window = MainWindowBook(filename)
window.show()
application.exec_()
