from sensor import Sensor
from classifier import Classifier
from notification import NotificationSystem
from server import Server

class SmartBin:
    def __init__(self):
        self.sensor = Sensor()
        self.classifier = Classifier()
        self.notifier = NotificationSystem()
        self.server = Server()

    def receive_trash(self):
        print("[스마트빈] 쓰레기를 수거합니다.")
        material = self.sensor.detect()
        category = self.classifier.classify(material)

        if category == "unknown":
            self.notifier.notify("분류되지 않은 쓰레기입니다. 다시 확인해주세요.")
        else:
            print(f"[스마트빈] '{category}'로 분류되었습니다.")
            if self.server.log(category):
                print("[스마트빈] 수거 완료 처리됨.")
