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

from .exception import RoleMethodError, RoleAttributeNameError
from types import new_class

__all__ = ['Role', 'role', 'role_method', 'has_role', 'apply_roles', 'rename_role_methods']


class Role(type):
    """Metaclass of role type"""

    def __new__(mcs, name, bases, dct):
        # Create a new instance role class
        new_cls = super().__new__(mcs, name, bases, dct)
        return new_cls

    def __call__(cls, class_):
        return cls._install_methods(class_)

    def _make_role_property(cls):

        def get_roles(self):
            return self.__roles

        def set_roles(self, value):
            if not isinstance(value, list):
                raise AttributeError('__roles__ must be a list')
            self.__roles = value

        cls.__roles = None
        cls.__roles__ = property(fget=get_roles, fset=set_roles)

    def _isrolemethod(cls, method):
        # Check if is role method
        _method = getattr(cls, method)
        if hasattr(_method, '__isrolemethod__') and callable(_method):
            return True
        else:
            return False

    def _install_methods(cls, class_):
        # Add role
        if hasattr(class_, '__roles__'):
            class_.__roles__.append(cls.__name__)
        else:
            cls._make_role_property()
            class_.__roles__ = [cls.__name__]
        # Inject other attribute or method on role class
        for attr in dir(cls):
            if attr == 'roled_class':
                continue
            # Role method decorator
            if cls._isrolemethod(attr) and attr.startswith('_'):
                setattr(class_, attr, getattr(cls, attr))
                continue
            # Method name conflict:
            # If attribute isn't in the instance and don't private
            if not hasattr(class_, attr) and not attr.startswith('_'):
                setattr(class_, attr, getattr(cls, attr))
            # If attribute isn't private and not role methods
            elif not attr.startswith('_'):
                raise RoleAttributeNameError(f'Attribute or method name conflict: {attr}')
        return class_


def role_method(objfunc):
    """Decorator method for role method"""
    if callable(objfunc):
        setattr(objfunc, '__isrolemethod__', True)
        return objfunc
    else:
        raise RoleMethodError(f'{objfunc} is not a function or method')


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
    new_cls = new_class(cls.__name__, cls.__bases__, {'metaclass': Role})
    for key, value in dict(cls.__dict__).items():
        if key != '__dict__':
            setattr(new_cls, key, value)
    return new_cls


def apply_roles(*role_objects):
    """Decorator function to apply two or more roles"""

    def wrapped_class(cls):
        for role_obj in role_objects:
            cls = role_obj(cls)
        return cls

    return wrapped_class


def rename_role_methods(**methods):
    """Decorator function for rename methods on Role based class"""

    def wrapped_role(cls):
        # Check if method is into class
        for name, new_name in methods.items():
            if name in dir(cls):
                setattr(cls, new_name, getattr(cls, name))
                delattr(cls, name)
        return cls

    return wrapped_role
