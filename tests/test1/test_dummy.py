from unittest import mock
import numpy as np
import pandas as pd


def test_dummy():
    assert 1 == 1


def test_dummy2(tmpdir, make_csv_file):
    test_data_path = tmpdir.join("test_data.csv")
    make_csv_file(5, 100, test_data_path)
    with mock.patch("joblib.load") as load_model:
        load_model.return_value.predict.return_value = np.array(0.42 * 100)
    assert test_data_path.exists()
    df = pd.read_csv(test_data_path)
    assert df.shape[0] == 100
