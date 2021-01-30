class TestClass:
    ### SETUP AND TEARDOWN CLASSMETHODS FOR BEFORE AND AFTER COMPLETION (respectively) OF TESTS AS A WHOLE  ###
    @classmethod
    def setup_class(cls):
        print("\n\nSetup TestClass Called")
    
    @classmethod                   
    def teardown_class(cls):
        print("\nTeardown TestClass Called")

    ### SETUP AND TEARDOWN METHODS FOR EACH TEST ###    

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unkown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unkown test")

    ### TESTS ###

    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True