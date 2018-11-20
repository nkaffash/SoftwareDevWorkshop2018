# -*- coding: utf-8 -*-
# 
# sum.py
#
# This file is written as an test example for the workshop.
#
# Copyright (C) 2018 N. Kaffashzadeh, FZ Jülich
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.

class MathFunc:

   name = "Abstract class for math functions"

   def __init__(self):
       pass

   def __str__(self):
       return self.name

class Sum(MathFunc):

    def __init__(self, value1=None, value2=None):
        x1 = value1
        x2 = value2
    def cal(self):
        return self.x1 + self.x2
        



