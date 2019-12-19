import ipaddress, socket, sys


class SocketScan(object):
    """
    Open a socket on a remote endpoint
    Parameters:
        target      The target IP of the remote endpoint
        port        The port to connect to on the remote target
    """
    connection = None
    message = None
    target_data = None
    data = None

    def make_connection(self):
        """
        Makes the connection to the target and port
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if self.target_data is not None:
                s.connect(self.target_data)
                s.sendall(bytes(self.message, 'utf8'))
                print('Sent', repr(self.message))
                print('Recieved', repr(s.recv(1024)))
            else:
                raise TypeError('No target data received')

    def __init__(self, target, port, message=None):
        """
        Sets the local target and port variables
        """
        try:
            ipaddress.ip_address(target)
        except ValueError as msg:
            raise

        if message is not None:
            self.message = message
        else:
            self.message = "Hello, there!"

        self.target_data = (target, int(port))
        self.make_connection()


def main(target, port, message=None):
    """
    Main
    """
    try:
        SocketScan(target, port, message)
    except ValueError as verr:
        print(verr)
    except TypeError as terr:
        print(terr)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1], sys.argv[2])
