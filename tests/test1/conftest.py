import pytest
import pandas as pd
import numpy as np


@pytest.fixture(scope="session")
def make_csv_file():
    def _make_csv_file(n_features, n_rows, output_path):
        columns = ["label"] + [f"feature{x}" for x in range(n_features)]
        df = pd.DataFrame(np.random.rand(n_rows, n_features + 1), columns=columns)
        df.to_csv(output_path, index=False)

    return _make_csv_file
