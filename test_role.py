import unittest
import pyrrole


class TestRole(unittest.TestCase):

    def test_role_class(self):
        class FallFromTree(metaclass=pyrrole.Role):
            a = 1

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

        class Fruit:
            pass

        @FallFromTree
        class Apple(Fruit):
            pass

        apple = Apple()

        self.assertIsInstance(apple, Fruit)
        self.assertIn('FallFromTree', apple.__roles__)
        self.assertEqual(apple.a, 1)
        apple.fall()
        apple.fall('apple tree')

        self.assertTrue(pyrrole.has_role(apple, FallFromTree))

    def test_roles_decorator(self):
        class FallFromTree(metaclass=pyrrole.Role):

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

        class Deciduous(metaclass=pyrrole.Role):
            pass

        class Fruit:
            pass

        @pyrrole.apply_roles(FallFromTree, Deciduous)
        class Apple(Fruit):
            pass

        apple = Apple()

        self.assertIsInstance(apple, Fruit)
        self.assertTrue(pyrrole.has_role(apple, FallFromTree))
        self.assertTrue(pyrrole.has_role(apple, Deciduous))

    def test_role_decorator(self):
        @pyrrole.role
        class FallFromTree:

            def __init__(self, cls):
                self.fruits = list()
                self.fruits.append(cls)

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

            def __str__(self):
                return "Fall from tree."

        class Fruit:
            pass

        @FallFromTree
        class Apple(Fruit):
            pass

        apple = Apple()
        self.assertIsInstance(FallFromTree, pyrrole.pyrrole.Role)
        self.assertIsInstance(apple, Fruit)
        self.assertIn('FallFromTree', apple.__roles__)
        self.assertTrue(pyrrole.pyrrole.has_role(apple, FallFromTree))

    def test_role_method_decorator(self):
        @pyrrole.role
        class FallFromTree:

            def __init__(self, cls):
                self.fruits = list()
                self.fruits.append(cls)

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

            @pyrrole.role_method
            def __str__(self):
                return "Fall from tree string."

        class Fruit:
            pass

        @FallFromTree
        class Apple(Fruit):
            pass

        apple = Apple()

        print(apple)

    def test_role_name_conflict(self):
        class FallFromTree(metaclass=pyrrole.Role):

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

        class Fruit:
            pass

        @FallFromTree
        @pyrrole.rename_role_methods(fall='fall_apple')
        class Apple(Fruit):
            def fall(self):
                print('Apple fell')

        apple = Apple()

        apple.fall_apple()

        self.assertIsInstance(apple, Fruit)
        self.assertTrue(pyrrole.has_role(apple, FallFromTree))

        @pyrrole.role
        class Deciduous:

            def fall(self, tree='tree'):
                print(f'Fall from {tree}')

        class Fruit:
            pass

        @Deciduous
        @pyrrole.rename_role_methods(fall='fall_apple')
        @FallFromTree
        @pyrrole.rename_role_methods(fall='fall_pear')
        class Pear(Fruit):
            def fall(self):
                print('Pear fell')

        pear = Pear()

        pear.fall_pear()
        pear.fall_apple()
        pear.fall()

        self.assertIsInstance(pear, Fruit)
        self.assertTrue(pyrrole.has_role(pear, Deciduous))
        self.assertTrue(pyrrole.has_role(pear, FallFromTree))


if __name__ == '__main__':
    unittest.main()
