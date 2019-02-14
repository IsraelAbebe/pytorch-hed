import grpc
from concurrent import futures
import time

import edgedetect_pb2
import edgedetect_pb2_grpc

import edgedetect


class EdgedetectServicer(edgedetect_pb2_grpc.EdgedetectServicer):
    def DetectEdge(self, request, context):
        if request.image is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Image is required")
        if request.image_type is None:
            pass
        response = edgedetect_pb2.ImageFile()
        response.image, response.image_type = edgedetect.detectedge(request.image, request.image_type)
        return response


class Server():
    def __init__(self):
        self.port = '[::]:50051'
        self.server = None

    def start_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        edgedetect_pb2_grpc.add_EdgedetectServicer_to_server(EdgedetectServicer(), self.server)
        print('Starting server. Listening on port 50051.')
        self.server.add_insecure_port(self.port)
        self.server.start()

    def stop_server(self):
        self.server.stop(0)
