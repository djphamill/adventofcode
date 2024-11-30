"""
Tests for make command, and associated functions
"""

from pathlib import Path

import pytest
from unittest.mock import MagicMock, patch

from aoc.commands.make import make
from aoc.commands.utils.day import Day
from aoc.commands.utils.errors import DirAlreadyExists
from aoc.commands.utils.year import Year
from aoc.run import set_up_argument_parser, Day, Year

@pytest.mark.xfail
def test_make_throws_error_when_day_directory_exists(tmp_path: Path, mocker):
    year = "1066"
    day = "2"
    
    mocked_project_path = MagicMock
    mocker.patch('aoc.commands.utils.paths.get_project_path', mocked_project_path)
    mocked_project_path.return_value = tmp_path

    year_path = tmp_path / f"_{year}"
    year_path.mkdir()
    day_path = year_path / f"day_{day}"
    day_path.mkdir()

    args_parser = set_up_argument_parser()
    args = args_parser.parse_args(["make", day, "-y", year])
    with pytest.raises(DirAlreadyExists):
        make(args)

def test_writes_test_file():
    pass