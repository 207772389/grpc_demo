from protobuf_test import hello_pb2

request = hello_pb2.HelloRequest(name="Bobby")
rep_str = request.SerializeToString()
print(rep_str)

request2=hello_pb2.HelloRequest()
request2.ParseFromString(rep_str)
print(request2.name)