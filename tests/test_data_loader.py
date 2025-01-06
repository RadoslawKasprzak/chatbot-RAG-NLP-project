import pytest
import os
from services.data_loader import DataLoader

def test_data_loader_correct_file(tmp_path):
    test_file = tmp_path / "test_data.txt"
    test_file.write_text(str([("url1", "treść1"), ("url2", "treść2")]),
    encoding="utf-8"
    )

    loader = DataLoader(str(test_file))
    data = loader.load_data()

    assert len(data) == 2
    assert data[0] == ("url1", "treść1")
    assert data[1] == ("url2", "treść2")

def test_data_loader_empty_file(tmp_path):
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")

    loader = DataLoader(str(test_file))

    with pytest.raises(Exception):
        loader.load_data()