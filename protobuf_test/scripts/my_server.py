from  protobuf_test.protos import helloworld_pb2,helloworld_pb2_grpc
import grpc
from concurrent import futures

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"你好，{request.name}")

if __name__ == '__main__':
    #1.实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #2.注册service逻辑到server中
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    #启动server
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    # server.stop()