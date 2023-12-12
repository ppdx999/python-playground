import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


class HttpRequest():
    pass

class HttpResponse():
    def __init__(self, data=None, status=200):
        self.data = data
        self.status = status

def errorable_task_A():
    try:
        1/0
    except Exception as e:
        logger.exception("errorable_task_Aが原因不明で復旧不能なエラーをだしました", stack_info=True)

class SomeService():
    def do_something(self):
        try:
            errorable_task_A()
            return "success"
        except Exception as e:
            logger.error(f"do_somethingが原因不明で復旧不能なエラーをだしました: {e}", stack_info=True)

# HttpRequestを受け取ってResponseを返す役割を担う
class Server():
    def __init__(self, service):
        self.service = service

    def handle_request(self, http_request):
        try:
            data = self.service.do_something()
            return HttpResponse({"data": data})
        except Exception as e:
            logger.exception("handle_request原因不明で復旧不能なエラーをだしました", stack_info=True)
            return HttpResponse(status=500)

# APIっぽい処理をする
server = Server(service=SomeService())
http_request = HttpRequest()
server.handle_request(http_request)
