import pytest
from main import connection
    
# @pytest.mark.parametrize()
# def testconnection():
#     ip = "127.0.0.1"
#     port = 8000
#     assert connection("127.0.0.1",8000) == connection(ip,port)
    
def basictest():
    assert 2+2 == 4