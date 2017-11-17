from my_code import MyBasicMath

math_obj = 0


def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")
    global math_obj
    math_obj = MyBasicMath()


def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")
    global math_obj
    del math_obj


class TestClass02:
    @classmethod
    def setUpClass(cls):
        """called once, before any test in the class"""
        print("In setUpClass()...")

    def setUp(self):
        """called before every test method"""
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()")
        assert math_obj.add(2, 5) == 7

    def test_case02(self):
        print("In test_case02()")

    def tearDown(self):
        """called after every test method"""
        print("In tearDown()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after all tests, if setUpClass() successful"""
        print("\nIn tearDownClass()...")
