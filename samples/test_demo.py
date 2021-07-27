import unittest


class Test(unittest.TestCase):
    """
    类似于pytest里面针对scope为class的情况
    """
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_01(self):
        print('test_01')
        self.assertTrue(True)

    def test_02(self):
        print('test_02')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
