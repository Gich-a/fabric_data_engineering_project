# IoT Hub uses Event Hub-compatible endpoint
from azure.eventhub import EventHubConsumerClient

class IoTHubSourceConnector:
    def __init__(self, connection_str, consumer_group='$Default'):
        self.client = EventHubConsumerClient.from_connection_string(
            connection_str,
            consumer_group=consumer_group
        )

    def receive_events(self, on_event):
        with self.client:
            self.client.receive(on_event=on_event, starting_position="-1")
