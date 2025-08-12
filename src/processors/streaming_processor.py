import pandas as pd
from validation.schema_validator import SchemaValidator

class StreamingProcessor:
    def __init__(self, eventhouse_client, validator: SchemaValidator):
        self.eventhouse_client = eventhouse_client
        self.validator = validator

    def process_event(self, event_data):
        df = pd.DataFrame([event_data])
        self.validator.validate(df)

        self.eventhouse_client.append_event(event_data)
        print(f"📡 Event processed and sent to Eventhouse: {event_data}")
