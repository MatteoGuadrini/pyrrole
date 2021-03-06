#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# __init__.py -- pyrrole
#
#     Copyright (C) 2021 Matteo Guadrini <matteo.guadrini@hotmail.it>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Python library for create role."""

from .pyrrole import Role, role, role_method, has_role, apply_roles, rename_role_methods

__version__ = '0.0.7'
__author__ = 'Matteo Guadrini, Giacomo Montagner'
__email__ = 'matteo.guadrini@hotmail.it'
__homepage__ = 'https://github.com/MatteoGuadrini/pyrrole'
