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

    def __new__(mcs, name, bases, dct):
        # Create a new instance role class
        new_class = super().__new__(mcs, name, bases, dct)
        return new_class

    def __call__(cls, instance):
        # Add role
        if hasattr(instance, '__roles__'):
            instance.__roles__.append(cls.__name__)
        else:
            setattr(instance, '__roles__', [cls.__name__])
        # Inject other attribute or method on role class
        for attr in dir(cls):
            if cls.__hasrolemethod__(attr):
                setattr(instance, attr, getattr(cls, attr))
        return instance

    def __hasrolemethod__(self, method):
        # Check if is role method
        _method = getattr(self, method)
        if hasattr(_method, '__isrolemethod__'):
            return True
        else:
            return False


def role_method(objfunc):
    """Decorator method for role method"""
    setattr(objfunc, '__isrolemethod__', True)
    return objfunc


def has_role(instance, role_name):
    """Class has a role?"""
    if not hasattr(instance, '__roles__'):
        return False
    if role_name.__name__ in instance.__roles__:
        return True
    else:
        return False


def role(cls):
    """Decorator function for create role type"""
    return Role(cls.__name__, (), dict(cls.__dict__))


def apply_roles(*role_objects):
    """Decorator function for more roles"""
    def role_class(cls):
        for roleobj in role_objects:
            cls = roleobj(cls)
        return cls
    return role_class
