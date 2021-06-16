import unittest
import pyrrole


class TestExecutor(unittest.TestCase):

    def test_role_class(self):
        class FallFromTree(metaclass=pyrrole.Role):

            @pyrrole.role_method
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


if __name__ == '__main__':
    unittest.main()
