from threading import Thread

from src.rabbitmq.producer import RabbitMQProducer
from src.rabbitmq.subscriber import RabbitMQSubscriber, example_callback
from src.webapi.api_request_handler import APIRequestHandler


class Package:
    def __init__(self) -> None:
        self._rabbitmq_producer = RabbitMQProducer("test_queue")
        self._rabbitmq_subscriber = RabbitMQSubscriber("test_queue", example_callback)
        self._api = APIRequestHandler()

    def start_services(self) -> None:
        self._rabbitmq_producer.start()
        self._rabbitmq_subscriber.start()

        # self._rabbitmq_producer.publish({"message": "Hello, world!"})

    def start_api(self) -> None:
        self._api.start()

    def stop(self) -> None:
        self._api.stop()
        self._rabbitmq_producer.stop()
        self._rabbitmq_subscriber.stop()


if __name__ == "__main__":
    main = Package()
    worker_thread = Thread(target=main.start_services, daemon=True)
    worker_thread.start()

    main.start_api()