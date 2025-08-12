import great_expectations as ge
import pandas as pd
import json

class SchemaValidator:
    def __init__(self, expectations_file):
        self.expectations_file = expectations_file
        with open(expectations_file, "r") as f:
            self.expectations_config = json.load(f)

    def validate(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame for validation")

        df_ge = ge.from_pandas(data)

        for exp in self.expectations_config.get("expectations", []):
            expectation_type = exp["expectation_type"]
            kwargs = exp["kwargs"]
            expectation_method = getattr(df_ge, expectation_type)
            result = expectation_method(**kwargs)
            if not result.success:
                raise ValueError(f"Data validation failed: {result}")

        print(f"✅ Validation passed for {self.expectations_file}")
