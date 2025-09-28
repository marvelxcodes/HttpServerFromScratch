import os
import sys
import logging
from socket import socket
from concurrent import futures

from utils import test
from request import Request

IP_ADDRESS = sys.argv[1] or '127.0.0.1'
PORT = sys.argv[2] or 8080
MAX_WORKERS = sys.argv[3] or 10
MAX_PAYLOAD_SIZE = 8192

class HTTPServer:
    def __init__(self, max_workers: int, max_payload_size: int):
        self._logger = logging.getLogger(HTTPServer.__name__)
        self.max_payload_size = max_payload_size

        self._socket = socket()
        self._logger.info('Socket created')

        self._pool = futures.ThreadPoolExecutor(max_workers=max_workers)

    def _handle_connection(self):
        request = Request()
        pass

    def listen(self, ip: str, port: int):
        self._socket.bind((ip, port))
        self._logger.info(f'Socket binded to port: {PORT}')

        self._socket.listen(self.max_payload_size)
        


    def close(self):
        self._socket.close()
        self._logger.info('Socket closed')

if __name__ == '__main__':
    server = HTTPServer(MAX_WORKERS, MAX_PAYLOAD_SIZE)
    server.listen(IP_ADDRESS, PORT)

