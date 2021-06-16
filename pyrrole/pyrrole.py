#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# pyrrole -- pyrrole
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

"""Core module of pyrrole."""


class Role(type):
    """Metaclass of role type"""

    def __new__(cls, name, bases, dct):
        # Create a new instance role class
        role = super().__new__(cls, name, bases, dct)
        return role

    def __call__(self, cls):
        # Add role
        if hasattr(cls, '__roles__'):
            cls.__roles__.append(self.__name__)
        else:
            setattr(cls, '__roles__', [self.__name__])
        # Inject other attribute or method on role class
        for attr in dir(self):
            if self.__hasrolemethod__(attr):
                setattr(cls, attr, getattr(self, attr))
        return cls

    def __hasrolemethod__(self, method):
        # Check if is role metodh
        _method = getattr(self, method)
        if hasattr(_method, '__isrolemethod__'):
            return True
        else:
            return False
