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
}

service HelloService {
  rpc SayHello(HelloRequest) returns(HelloResponse)
}
'''

hello = load(define, 'hello')

@grpc(app.route, hello.HelloService.SayHello)
def say_hello(param):
    return hello.HelloResponse(reply="Hello {}".format(param.greeting), server='grpc')

if __name__ == "__main__":
    app.run(debug=True)
