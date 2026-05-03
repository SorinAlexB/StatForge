import pytest

from statforge.__main__ import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from statforge!\n"
