import protopy

define = '''
message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;
}
message HelloRequest {
  optional string greeting = 1;
}

message HelloResponse {
  optional string reply = 1;
}

service HelloService {
  rpc SayHello(HelloRequest) returns(HelloResponse)
}
'''

m = protopy.load(define, 'test')
print(m)
