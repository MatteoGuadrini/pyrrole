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

__all__ = ['Role', 'role', 'role_method', 'has_role', 'apply_roles']


class Role(type):
    """Metaclass of role type"""
    def __new__(mcs, name, bases, dct, **methods):
        # Create a new instance role class
        new_class = super().__new__(mcs, name, bases, dct)
        new_class.role_methods = methods
        return new_class

    def __call__(cls, instance):
        # Add role
        if hasattr(instance, '__roles__'):
            instance.__roles__.append(cls.__name__)
        else:
            setattr(instance, '__roles__', [cls.__name__])
        # Inject other attribute or method on role class
        for attr in dir(cls):
            # Check role_methods if is already specified
            if attr == 'role_methods':
                if hasattr(instance, attr):
                    cls.role_methods.update(getattr(instance, attr))
            # Method name conflict:
            # If attribute isn't in the instance and don't private
            if not hasattr(instance, attr) and not attr.startswith('_'):
                setattr(instance, attr, getattr(cls, attr))
            # If attribute is in the instance and in role methods
            elif hasattr(instance, attr) and attr in cls.role_methods:
                # Check if attribute is callable
                if not callable(getattr(instance, attr)):
                    raise RoleMethodError(f'{attr} is not a method')
                setattr(instance, cls.role_methods.get(attr), getattr(instance, attr))
            # If attribute isn't private and not role methods
            elif not attr.startswith('_') and not attr == 'role_methods':
                raise RoleAttributeNameError(f'Attribute or method name conflict: {attr}')
            # Role method decorator
            if cls._isrolemethod(attr) and attr.startswith('_'):
                setattr(instance, attr, getattr(cls, attr))
        return instance

    def _isrolemethod(self, method):
        # Check if is role method
        _method = getattr(self, method)
        if hasattr(_method, '__isrolemethod__') and callable(_method):
            return True
        else:
            return False


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


def role(**methods):
    """Decorator function for create role type"""
    def wrapper(cls):
        return Role(cls.__name__, cls.__bases__, dict(cls.__dict__), **methods)
    return wrapper


def apply_roles(*role_objects):
    """Decorator function to apply two or more roles"""
    def wrapped_class(cls):
        for role_obj in role_objects:
            cls = role_obj(cls)
        return cls
    return wrapped_class
