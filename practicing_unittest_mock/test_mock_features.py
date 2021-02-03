import pytest
from pytest import raises
from unittest.mock import MagicMock
from FileReader import readFromFile

@pytest.fixture(autouse=True)
def mock_open(monkeypatch):
    mock_file = MagicMock()
    # add a line of string to a mocked file
    mock_file.readline = MagicMock(return_value="hello world!")
    # lets mock a file being opened (eg: open = os.path.)
    _mock_open = MagicMock(return_value=mock_file)
    # set attribute with monkeypatch
    monkeypatch.setattr("builtins.open", _mock_open)
    return _mock_open

# def test_canCallReadFromFile():
#     readFromFile("notes.txt")

# @pytest.mark.skip
def test_fileReturnsLineOfString(mock_open, monkeypatch):
    # mock file exists with True value
    mock_exits = MagicMock(return_value=True)
    # set os.path.exists attribute with monkeypatch
    monkeypatch.setattr("os.path.exists", mock_exits)
    # call the actual readFromFile()
    res = readFromFile(filename="notes.txt")
    # lets mock the opened file being read
    mock_open.assert_called_once_with("notes.txt", "r")
    # verify the result
    assert res == "hello world!"

def test_throwsExceptionFileNotFound(mock_open, monkeypatch):
    # mock file does not exists with False value
    mock_exits = MagicMock(return_value=False)
    # set os.path.exists attribute with monkeypatch
    monkeypatch.setattr("os.path.exists", mock_exits)
    with raises(Exception):
        # call the actual readFromFile()
        res = readFromFile(filename="notes.txt")

