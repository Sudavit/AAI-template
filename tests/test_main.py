import pytest

from AAI.main import main


def test_main_outputs_correct_greeting(capsys):
    """
    RED/GREEN TEST: Validates that main() prints the specific AAI greeting.
    Verification status: PENDING -> PASSED
    """
    # Act
    main()

    # Assert
    captured = capsys.readouterr()
    assert captured.out == "hello from AAI\n"


def test_main_accepts_optional_args():
    """
    Ensures the function signature handles list inputs without crashing,
    maintaining Repository Pattern stability.
    """
    try:
        main(["--test-mode"])
    except TypeError as e:
        pytest.fail(f"main() failed to handle args list: {e}")
