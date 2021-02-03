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

**Example Code:**
`In ./lessons-guided-by-readme-doc/test_xUnitStyle.py`

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

**Pytest Output:**

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

**Updated Example Code:**
`In ./lessons-guided-by-readme-doc/test_xUnitStyle.py`

```
def setup_module(module):
    print("\n\nSetup Module Called")

def teardown_module(module):
    print("\nTeardown Module Called")

# ... rest of the above code
```

The pytest output shows that now the `setup module function` is called once before any of the unit tests or the unit test `setup and teardown functions` are executed. And the `teardown module function` is called once after all the unit tests in the module and their `setup and teardown functions` have completed.

**Updated Pytest Output:**

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

**Pytest Test Class Code:**
`In ./lessons-guided-by-readme-doc/test_xUnitClassStyle.py`

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

**Pytest TestClass Output:**

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
- Specifying that a function is a Test Fixture is done by applying the `pytest.fixture` decorator to the function.
- Individual unit tests can specify they want to use that function by specifying it in their parameter list, or by using the `pytest.mark.usefixture` decorator.
- The fixture can also set its autouse parameter to true, which will cause all tests in the fixture scope to automatically execute the fixture before the test executes.

#### Test Fixture "Setup"

Example Code::
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg1.py`

```
import pytest

### SETUP FIXTURES ###

@pytest.fixture
def setup():
    print("\n\nInitial Setup")

### TESTS ###

def test1(setup):
    print("Executing test1")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2")
    assert True
```

> If you do not put 'setup' or '@pytest.mark.usefixtures("setup")' in test functions or methods, then the `setup()` fixture will not run.

Pytest Output:

```
======== test session starts ========

test_PyTestFixtureStyleEg1.py::test1

Initial Setup
Executing test1
PASSED
test_PyTestFixtureStyleEg1.py::test2

Initial Setup
Executing test2
PASSED

======== 2 passed in 0.01s =========
```

It can be very useful for each individual test to be able to specify which test fixtures it needs executed before the test is run. But this can also be cumbersome for those cases where all the tests need to run the same test fixture. In this case, the `autouse `parameter of the test fixture can be set to `true`, and then the fixture will automatically be executed before each test that is in the fixture scope.

Example Code:
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg1.py`

```
### SETUP FIXTURES ###

@pytest.fixture(autouse = true)
def setup():
    print("\nInitial Setup")

### TESTS ###

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
```

#### Test Fixture "Teardown"

Often, there is some type of teardown or cleanup that a test, class or module needs to perform after testing has been completed. Each Test Fixture can specify their own teardown code that should be executed. There are two methods of specifying a teardown code for a Test Fixture. The `yield` keyword, and the `request-context` object's `addfinalizer` method.

`yield`: The `yield` keyword is the simpler of the two options for teardown code. The code after the yield statement is executed after the fixture goes out of scope. The yield keyword is a replacement for return, and any return values should be passed to it. The addfinalizer method of adding teardown code is a little more complicated, but also a little more capable than the yield statement.

```
@pytest.fixture()
def setup():
    print("Setup")
    yield
    print("Teardown!")
```

`addfinalizer`: With the `addfinalizer` method, one or more finalizer functions are added via the `request-context`'s addfinalizer method. **One of the big differences between this method and the `yield` keyword is that this method allows for multiple finalization functions to be specified.**

```
@pytest.fixture()
def setup():
    print("Setup")
    def teardown():
        print("Teardown!")
    request.addfinalizer(teardown)
```

Example Code:
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg2.py`

```

import pytest

### SETUP FIXTURES ###

@pytest.fixture()
def setup1():
    print("\n\nSetup1")
    yield
    print("\nTeardown1!")

@pytest.fixture()
def setup2(request):
    print("\nSetup2")

    def teardown_a():
        print("TeardownA!")

    def teardown_b():
        print("\nTeardownB!")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

### TESTS ###

def test1(setup1):
    print("Executing test1")
    assert True

def test2setup2(setup2):
    print("Executing test2")
    assert True

```

Pytest Output:

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 2 items

test_PyTestFixtureStyleEg2.py::test1

Setup1 👈
Executing test1
PASSED
Teardown1! 👈

test_PyTestFixtureStyleEg2.py::test2setup2

Setup2 👈
Executing test2
PASSED
TeardownB! 👈
TeardownA! 👈

======== 2 passed in 0.01s =========
```

In the output from above pytest, we can see that the teardown code for `setup1` is called after `test1` finishes executing. And the two teardown functions for `setup2` are called after `test2` finishes.

### Test Fixtures Scopes

Which test a fixture applies to, and how often it is run, depends on the fixture scope. Test Fixtures have four different scopes that are possible.

Test fixtures can have the following four different scopes which specify how often the fixture will be called:

`Function scope`: By default, the scope is set to `Function`. And this specifies that the fixture should be called for all tests in the module.
`Class scope`: specifies that the Test Fixture should be executed once per test class.
`Module scope`: specifies that the fixture should be executed once per module.
`Session scope`: specifies that the fixture should be executed once when `pytest` starts.

**Example #1:**

In this example, I've implemented two modules. In the first module, I have three different test fixtures, each at a different scope. Function fixture, Module fixture, and Session fixture. I've also implemented unit tests test1, and test2.

`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg3a.py`

```
import pytest

### SETUP FIXTURES ###

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("Setup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")

### TESTS ###
def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
```

**Pytest Output of Example #1:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 4 items

test_PyTestFixtureStyleEg3a.py::test1
Setup Session
Setup Module

Setup Function
Executing test1
PASSED

test_PyTestFixtureStyleEg3a.py::test2
Setup Function
Executing test2
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the Session fixture runs first, and is run once. Then the Module fixture is run once for the first module, and then the Function fixture in the first module is run once for each test in the first module.

**Example #2:**

In the second module, I also have three different test fixtures at three different scopes. Function fixture, Class fixture, and Module fixture. And I've implemented a test class to unit test.

`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg3b.py`

```
import pytest

### SETUP FIXTURES ###

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")

### TESTS ###
class TestClass:
    def test1b(self):
        print("Executing test1b")
        assert True

    def test2b(self):
        print("Executing test2b")
        assert True
```

**Pytest Output of Example #2:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

test_PyTestFixtureStyleEg3b.py::TestClass::test1b

Setup Module2
Setup Class2

Setup Function2
Executing test1b
PASSED

test_PyTestFixtureStyleEg3b.py::TestClass::test2b
Setup Function2
Executing test2b
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the Module fixture is run first, and its run once. The Class fixture runs next, and then the Function fixture is run once before each of the test classes unit tests.

### Test Fixture Return Objects and Params

- Pytest fixtures allow you to optionally return `data` from the fixture that can be used in the test.
- The optional `params` array argument in the fixture decorator can be used to specify one or more values that should be passed to the test.
- When a `params` argument has multiple values, the test will be called once with each value.

**Example Code:**
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg4.py`

```
import pytest

### SETUP FIXTURES ###
@pytest.fixture(params=[1,2,3])
def _param(request):
    retVal = request.param
    print(f"\nSetup return val={retVal}")
    return retVal

### TESTS ###
def test(_param):
    print(f"Param from fixture={_param}")
    assert True
```

**Pytest Output of Example code:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========
collected 3 items

test_PyTestFixtureStyleEg4.py::test[1]
Setup return val=1
Param from fixture=1
PASSED

test_PyTestFixtureStyleEg4.py::test[2]
Setup return val=2
Param from fixture=2
PASSED

test_PyTestFixtureStyleEg4.py::test[3]
Setup return val=3
Param from fixture=3
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the test fixture and unit test are both run once for each value specified in the params list, as expected. The params feature can be a powerful and easy way to run your unit test with various values. **Care should be taken with this approach, though, as you generally still want to have different test cases and separate unit tests with unique names so that they can be easily identified when they fail.**

## Assert and Testing Exceptions

### Assert

- Pytests allows the use of the built in Python assert statement for performing verifications in a unit test.
- The normal comparison operators can be used on all Python data types. Less than `<`, greater than `>`, less than or equal `<=`, greater than or equal `>=`, equal `==` or non equal `!=`.
- Pytests expands on the messages that are reported for assert failures to provide more context in the test results.

**Eamples:**
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg5a.py`

```
def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_FloatAssert():
    assert "1.0" == "1.0"

def test_arrayAssert():
    assert [1,3,4] == [1,3,4]

def test_dictAssert():
    assert {"1":1} == {"1":1}
```

#### Comparing FLoating Point Values

- Validating floating point values can sometimes be difficult, as internally the value is stored as a series of binary fractions (i.e. 1/3 is internally 0.333333333...). **Because of this, some comparisons that we'd expect to pass, will fail.**
- Pytests provides the `approx` function, which will validate the two floating point values, or approximately the same value, as each other, to then a default tolerance of one times e to the negative six value.

**Example:**
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg5a.py`

```
# Failing Test
def test_BadFloatCompare():
    assert (0.1 + 0.2) == 0.3

# Passing Test
from pytest import approx
def test_BadFloatCompare():
    assert (0.1 + 0.2) == approx(0.3)
```

### Verifing Exceptions

- In some test cases, we need to verify that a function raises an exception under certain conditions.
- Pytest provides the raises helper to perform this verification, using the `with` keyword.
- When the raises helper is used, the unit test will fail, if the specified exception is not thrown in the code block, after the `raises` line.

**Example:**
`In ./lessons-guided-by-readme-doc/test_PyTestFixtureStyleEg5b.py`

```
from pytest import raises

def raisesValueException():
    raise ValueError

def test_Exception():
    with raises(ValueError):
        raisesValueException()
```

## PyTest Command Line Arguments

- By default, PyTest runs all tests that it finds in the current working directory and sub-directory using the naming conventions for automatic test discovery.
- There are several PyTest command line arguments that can be specified to try and be more selective about which tests will be executed.
  - `moduleName`: You can simply pass in the `moduleName` to execute only the unit tests in that one particular module.
  - `directoryName/`: You can also simply pass in a directory path to have PyTest run only the tests in that directory.
  - `-k "expression"`: You can also use the `-k` option to specify an evaluation experssion in the string based on keywords such as the module name, the class name, and the function name. (e.g. "TestClass and TestFunction")
  - `-m "expression"`: You can also use the `-m` option to specify that any tests that have a `@pytest.mark` decorator that matches the specified expression string will be executed.
    - Marks can only be applied to tests, having no effect on fixtures.
    - Unregistered marks applied with the @pytest.mark.name_of_the_mark decorator will always emit a warning in order to avoid silently doing something surprising due to mistyped names. You can disable the warning for custom marks by registering them in your `pytest.ini` file or using a custom `pytest_configure` hook. - [how-to-disable-warning-for-custom-marks](https://docs.pytest.org/en/stable/mark.html)

### Additional command line arguments that can be very useful.

- `-v`: The `-v` option specifies that verbose output from PyTest should be enabled.
- `-q`: The `-q` option specifies the opposite. It specifies that the test should be run quietly, or with minimal output. This can be helpful from a performance perspective when you're running hundreds or thousands of tests.
- `-s`: The `-s` option specifies that PyTest should not capture the console output, allowing you to see the printouts from the print, from the tests.
- `--ignore`: The `--ignore` option allows you to specify a path that should be ignored during test discovery.
- `--maxfail`: The `--maxfail` option specifies that PyTest should stop after _n_ number of test failures.

**Examples:**

We've got three test modules named:

- test_file1.py, containing test1
- test_file2.py, containing test2, and
- test_file3.py, containing test3.

Test_file3.py is in a sub-directory of the project named `testSubDirectory`.

**Example of test files and test-sub-folder structure:**

> These files are not present in this repo.

```
.
├── testSubDirectory
│   └── test_file3.py
├── test_file1.py
└── test_file2.py
```

`In testSubDirectory/test_file3.py`

```
def test3():
    print("Test3")
    assert True
```

`In test_file1.py`

```
def test1():
    print("Test1")
    assert True
```

`In test_file2.py`

```
def test2():
    print("Test2")
    assert True
```

- First we'll run PyTest with just the -v and -s arguments to verify that all the tests are discovered and run by PyTest.

Command: `pytest -v -s`

And we see that PyTest found the three tests and executed them.

```
======== test session starts ========

collected 3 items

test_file1.py::test1 Test1
PASSED
test_file2.py::test2 Test2
PASSED
testSubDirectory/test_file3.py::test3 Test3
PASSED

======== 2 passed in 0.01s =========
```

- Now let's run just the tests in the `test_file1.py` file, by passing that `module name` in on the command line.

Command: `pytest -v -s test_file1.py`

And in the PyTest output, we can see that only `test1` has run.

```
======== test session starts ========

test_file1.py::test1 Test1
PASSED

======== 2 passed in 0.01s =========
```

- Next, I'll have just the tests found in the `testSubDirectory` executed by passing that directory in on the command line.

Command: `pytest -v -s testSubDirectory`

And we see that only test3 is executed.

```
======== test session starts ========

testSubDirectory/test_file3.py::test3 Test3
PASSED

======== 2 passed in 0.01s =========
```

- Now we'll execute just `test2` by using the `-k` or keyword argument, and specifying `test2` as the `keyword`.

Command: `pytest -v -s -k "test2"`

And we see that only `test2` was executed.

```
======== test session starts ========

collected 3 items / 2 deselected / 1 selected

test_file2.py::test2 Test2
PASSED

======== 2 passed in 0.01s =========
```

- Now I'll expand that to run only tests 2 and 3 with an `or` statement in the keyword expression.

Command: `pytest -v -s -k "test2 or test3"`

And we see that `test2` and `test3` are run.

```
======== test session starts ========

collected 3 items / 1 deselected / 2 selected

test_file2.py::test2 Test2
PASSED
testSubDirectory/test_file3.py::test3 Test3
PASSED

======== 2 passed in 0.01s =========
```

Now we'll mark `test1` and `test3` using the PyTest `mark decorator`, and have PyTest run just those tests using the `-m` or mark expression.

**Marking test1:**

```
import pytest

@pytest.mark.test1
def test1():
    print("Test1")
    assert True
```

**Marking test3:**

```
import pytest

@pytest.mark.test3
def test3():
    print("Test3")
    assert True
```

And we see just those tests are run.

```
======== test session starts ========

collected 3 items / 1 deselected / 2 selected

test_file1.py::test1 Test1
PASSED
testSubDirectory/test_file3.py::test3 Test3
PASSED

======== 2 passed in 0.01s =========
```

## Unit Test Isolation with Dummies, Fakes, Stubs, Spies & Mocks

### Test Doubles

- Almost all code that gets implemented will depend on another piece of code in the system.
- Those other pieces of code are often times trying to do things or communicate with things that are not available in the unit testing environment, or are so slow they would make our unit tests extremely slow. For example, if your code queries a third-party rest API on the internet, and that server is down for any reason, you can't run your test.
- `Test doubles` are the answer to that problem. They are objects that are created in the test to replace the real production system collaborators. **There are many types of test doubles.**
  - `Dummy` objects are the simplest. They are simply placeholders that are intended to be passed around but not actually called or used in any real way. They'll often generate exceptions if they're called.
  - `Fake` objects have a different and usually simplified implementation from the production collaborator that make them usable in the test code, but not suitable for production.
  - `Stubs` provide implementations that do expect to be called, but respond with basic canned responses.
  - `Spies` provide implementations that record the values that are passed into them. The tests can then use those recorded values for validating the code under test.
  - `Mock` objects are the most sophisticated of all the test doubles. They have pre-programmed expectations about the ordering of calls, the number of times functions will be called, and the values that will be passed in. Mock objects will generate their own exceptions when these pre-programmed expectations are not met.

#### Mock frameworks

- Mock frameworks are libraries that provide easy-to-use API's for automatically creating any of these types of test doubles at runtime.
- They provide easy API's for specifying the Mocking expectations in your unit test.
- They can be much more efficient than implementing your own custom Mock objects, because creating your own custom Mock objects can be time consuming, tedious, and error prone.

##### Unittest.mock

- `Unittest.mock` is a **Mocking framework** for Python.
- It's build into the standard unit test for Python, in version 3.3 and newer, and for older versions of Python, a back-ported version of the library is available on Py Py, called Mock, and can be installed with the command pip install Mock.
- **Unittest.mock provides the Mock class**, which is an extremely powerful class that can be used to create test objects that can be used as fakes, stubs, spies, or true Mocks for other classes or functions.
  - The Mock class has many initialization parameters for specifying how the object should behave, such as what in interface it should Mock, if it should call another function when it's called, or what value it should return.
  - Once a Mock object has been used, it has many built-in functions for verifying how it was used, such as how many times it was called, and with what parameters.

### Mock - Initialization

- `Mock` provides many initialization parameters which can be used to control the Mock objects behavior.
- The `spec` parameter specifies the interface that the Mock object is implementing. If any attributes of the Mock object are called which are not in that interface, then the Mock will automatically generate an attribute exception.
- The `side_effect` parameters specifies a function that should be called when the Mock is called. This can be useful for more complicated test logic that returns different values depending on input parameters or generates exceptions.
- The `return_value` parameter specifies the value that should be returned when the Mock object is called. If the `side_effect` parameter is set, it's return value is used instead.

### Mock - Verification

- Mock provides many built-in functions for verifying how the Mock was called, including the following assert functions:
  - The `assert_called` function will pass if the Mock was ever called with any parameters.
  - The `assert_called_once` function will pass if the Mock was called exactly one time.
  - The `assert_called_with` function will pass if the Mock was last called with the specified parameters.
  - The `assert_called_once_with` function will pass if the Mock was called exactly once with the specified parameters.
  - The `assert_any_call` function will pass if the Mock was ever called with the specified parameters.
  - And the `assert_not_called` function will pass if the Mock was never called.

#### Mock - Additional Verification

- Mock provides these additional built-in attributes for verifying how it was called:
  - the `assert_has_calls` function passes if the Mock was called with parameters specified in each of the passed in list of Mock call objects, and optionally in the order that those call objects are put into the list.
  - The `called` attribute is a `boolean` which is true if the Mock was ever called.
  - The `call_count` attribute is an `integer` value specifying the number of times the Mock object was called. The `call_args` attribute contains the parameters that the Mock was last called with.
  - And the `call_args_list` attribute is a list with each entry containing the parameters that were used in call to the Mock object.

### Unittest.mock - MagicMock Class

- `unittest.mock` also provides the `MagicMock class`.
- MagicMock is derived from Mock and provides a default implementation of the Python magic methods. These are the methods with double underscores at the beginning and end of the name, like string, and int (i.e. \_\_str\_\_).
- The following magic names are not supported by MagicMock, due to being used by Mock for other things, or because mocking them could cause other issues:
  - \_\_get\_\_, \_\_set\_\_, \_\_init\_\_, \_\_new\_\_, \_\_prepare\_\_, \_\_instancecheck\_\_, \_\subclasscheck\_\_, and \_\delete\_\_.

When using MagicMock, you just need to keep in mind the fact that the magic methods are already created and take note of the default values that are returned from those functions to ensure they match the needs of the test that's being implemented.

## PyTest MonkeyPatch Test Fixture

PyTest provides the Monkeypatch Test Fixture to allow a test to dynamically change modules and class attributes, dictionary entries, and environment variables. Unittest provides a patch decorator which provides similar operations, but this can sometimes conflict with the PyTest Text Fixture decorators, so I'll focus on using Monkeypatch for this functionality.

Example: `In ./practicing_unittest_mock/test_mock_features.py`

## TTD best practices

- **First, you should always do the next simplest test case.** This allows you to gradually increase the complexity of the code, refactoring as you go. This helps keep your code clean and understandable.
  - If you jump to the complex cases too quickly, you can find yourself stuck writing a lot of code for one test case which breaks the short feedback cycle we look for with TDD.
  - Beyond just slowing you down, this can also lead to bad design as you can miss some simple implementations that come from the incremental approach.
- **Always try to use descriptive test names.** The code is read thousands of times more than it's written as the years go by. Making the code clear and understandable should be the top priority.
- **Unit tests are the best documentation for the developers** that come after you for how you intended the code to work. If they can't understand what the unit test is testing, that documentation value is lost.
  - Test suites should name the class or function that is under test and the test names should describe the functionality that is being tested.
- **Keep your unit test building and running fast.** One of the biggest benefits of TDD is the fast feedback on how your changes have affected things.
  - You lose this if the build and/or execution of your unit test is taking a long time, i.e., more than just a few seconds.
- **To help your test stay fast, try to keep the console output to a minimum or eliminated altogether.**
  - This output just slows down the test and clutters up the test results.
  - And also mock out any slow collaborators that are being used with test doubles that are fast.
- **Use code coverage analysis tools.** Once you've implemented all your test cases, go back and run your unit test through a code coverage tool.
  - It can be surprising. Some of the areas of your code you'll miss, especially negative test cases.
  - You should have a goal of 100% code coverage on functions with real logic. Don't waste your time on one-line getter or setter functions.
- **Make sure you run your unit tests multiple times and in a random order.**
  - Running your tests many times will help ensure that you don't have any flaky tests that are failing intermittently.
  - Running your tests in random order ensures that your tests don't have dependencies between each other.
  - You can use the `pytest-random-order` **plugin** to randomize the execution of the tests and the `pytest-repeat` **plugin** for repeating all or a subset of the unit tests as needed.
- **Using a static code analysis tool regularly** on your code base is another core requirement for ensuring code quality.
  - Pylint is an excellent open source static analysis tool for Python that can be used for detecting bugs in your code (code that meets your team's coding standard - or the PEP8 standard by default).
  - It can also verify the code is formatted to the team standard, and it can even generate UML diagrams based on its analysis of the code.
