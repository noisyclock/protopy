from flask import Flask

app = Flask(__name__)
from protopy import decorator
from protopy import load
grpc = decorator.get_flask_decorator()
define = '''
message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;
}
message HelloRequest {
  string greeting = 1;
}

message HelloResponse {
  string reply = 1;
  singular string server = 2;
  repeated string test = 3;
  enum Beauty {
      GAOYUANYUAN = 1;
      LINZHILING = 2;
  }
  singular Beauty beauty = 4;
}

service HelloService {
  rpc SayHello(HelloRequest) returns(HelloResponse)
}
'''

hello = load(define, 'hello')

@grpc(app.route, hello.HelloService.SayHello)
def say_hello(param):
    return hello.HelloResponse(reply="Hello {}".format(param.greeting), server='grpc', test=['a', 'b', 'c'], beauty='GAOYUANYUAN')

if __name__ == "__main__":
    app.run(debug=True)
