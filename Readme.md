## Pytest

- PyTest is a Python unit testing framework.

- It provides the ability to create tests, test modules, test classes, and test fixtures.

- It uses the built-in Python assert statement which makes implementing unit tests much simpler than other Python unit testing frameworks.
- It also adds many useful command line arguments to help specify what tests should be run and in what order.

### How do you create a unit test in Python with PyTest?

- In PyTest, individual tests are Python functions with test at the beginning of the function name.
- The unit tests then execute production code and use the standard Python assert statement to perform verifications on results.
- Similar tests can be grouped together by including them in the same module or class.

### Run pytest

```
# In root of the project

> pytest -v
```

The `-v ` argument tells PyTest to run in `verbose mode` and it will tell me which unit test it's running and if they pass or not.

The `-s` argument, which tells pytest not to capture the console output, so you can see the results of the print statements on the console.

### Test discovery

PyTest will automatically find your tests when you run it from the command line using several naming rules for the test files, test classes, and test functions.

Test `function` names should begin with test.

`Classes` with tests in them should have the word `Test` with a capital `T` at the beginning of the class name. **These classes should also have no \_\_init\_\_ method.**

The `file names` for test modules should start with `test_ ` or end with `_test`.

### An xunit-style setup and teardown

One key feature of all unit test frameworks is providing the ability to execute setup code before and after the test. pytest provides this capability with both `xUnit-style` setup and `teardown functions` and with pytest `fixtures`.

The xUnit-style setup and `teardown functions` allow you to execute code before and after:

- Test modules,

```
    def setup_module():
    def teardown_module():
```

- Test functions,

```
    def setup_function():
    def teardown_function():
```

- Test classes, and

```
    def setup_classe():
    def teardown_classe():
```

- Test methods in Test classes.

```
def setup_method():
def teardown_method():

```

#### Test functions

Using these `setup` and `teardown functions` can help reduce code duplication by letting you specify the setup and teardown code once at each of the different levels as necessary rather than repeating the code in each individual unit test. This can help keep your code clean and manageable.

> I've got two unit tests defined, test one and test two. I've also got the functions setup function and teardown function defined. `pytest` will automatically call setup function before each unit test in that module that is not in a class. It will then call teardown function after each unit test has completed executing.

`Setup function` and `teardown function` are passed in the unit test that is being executed, so the setup and teardown code can be customized per unit test if necessary.

Now lets run this in pytest and see the output.

Test Code:

```
def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unkown test")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down unkown test")

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
```

The pytest output shows that the setup function is called before test one executes and is called again before test two executes.

The `teardown function` is called after test one executes and again after test two executes. Which unit test is being executed is passed in, so the setup and teardown code can easily be customized per unit test.

Pytest result:

```

(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 2 items

test_xUnitStyle.py::test1
Setting up test1 👈
Executing test1 👈
PASSED
Tearing down test1 👈

test_xUnitStyle.py::test2
Setting up test2 👈
Executing test2 👈
PASSED
Tearing down test2 👈

======== 2 passed in 0.01s =========
```

#### Test Modules (with Test Functions)

Lets extend above example to include setup and teardown functions for the `module` itself. These functions will be **called once before** any of the unit tests in the `module` are **executed and again after all the unit tests in the `module` have completed executing**.

Now update the code to include `setup module` and `teardown module` functions with print statements and then execute pytest again to see the updated results.

Updated Pytest Code:

```
def setup_module(module):
    print("\n\nSetup Module Called")

def teardown_module(module):
    print("\nTeardown Module Called")

# ... rest of the above code
```

The pytest output shows that now the `setup module function` is called once before any of the unit tests or the unit test `setup and teardown functions` are executed. And the `teardown module function` is called once after all the unit tests in the module and their `setup and teardown functions` have completed.

Updated Pytest Outut:

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

test_xUnitStyle.py::test1

Setup Module Called 👈

Setting up test1
Executing test1
PASSED
Tearing down test1

test_xUnitStyle.py::test2
Setting up test2
Executing test2
PASSED
Tearing down test2

Teardown Module Called 👈

======== 2 passed in 0.01s =========
```

#### Test Class (with Test Modules & Functions)

Let's move the `test one` and `test two` unit test functions into a `class` called `TestClass`. Let's also add the **method** `setup class`, `teardown class`, `setup method`, and `teardown method`.

The `setup class` and `teardown class` **methods** have the `@classmethod` **decorator** applied, as they are passed in the uninstantiated class object rather than a unique instance of the class.

- The setup class method will be executed by pytest before any of the unit tests in the class are executed.
- The teardown class method will be executed by pytest after all of the unit tests in the class are executed.
- `Setup method` will be called before each unit test in the class is executed, and the `teardown method` will be executed after each unit test in the class has completed.

Pytest Test Class Code:

```
class TestClass:
    @classmethod
    def setup_class(cls):
        print("\n\nSetup TestClass Called")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown TestClass Called")

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

    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True

```

Let's run this in `pytest` and see the results. The pytest output shows that the `setup class method` is called before anything else. Then `setup method` is called before `test one`, and `teardown method` is called after `test one` completes. Then `setup method` is called again before test two, and `teardown method` is called again after test two completes. Lastly, teardown class is called.

Pytest TestClass Output:

```
collected 2 items

test_xUnitClassStyle.py::TestClass::test1

Setup TestClass Called 👈

Setting up test1
Executing test1
PASSED
Tearing down test1

test_xUnitClassStyle.py::TestClass::test2
Setting up test2
Executing test2
PASSED
Tearing down test2

Teardown TestClass Called
```

### Pytest Fixtures

Pytest fixtures is feature, which is a powerful alternative to the xUnit style of setup/teardown functions, which utilizes dependency injection.

- Test Fixtures allow for re-use of code across tests by specifying functions that should be executed before the unit test runs.
- Specifying that a function is a Test Fixture is done by applying the pytest.fixture decorator to the function.
- Individual unit tests can specify they wanna use that function by specifying it in their parameter list, or by using the `pytest.mark.usefixture` decorator.
- The fixture can also set its autouse parameter to true, which will cause all tests in the fixture scope to automatically execute the fixture before the test executes.
