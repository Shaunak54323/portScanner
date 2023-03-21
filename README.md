# portScanner

This code is a basic port scanner written in Python that scans a target IP address for open ports within the range of 11300 to 11500.

Here is a brief explanation of the code:

The script takes an IP address as an argument and translates the hostname to its IPv4 address using the socket.gethostbyname() function. If there are no arguments or an invalid number of arguments, the script will exit.

The portCount variable is initialized to 0, which will keep track of the number of open ports found.

A banner is printed to the console with the target IP address and the time the scan started.

A for loop is used to iterate over the range of ports to be scanned.

A socket is created using socket.socket() with AF_INET (address family) and SOCK_STREAM (socket type) arguments. socket.setdefaulttimeout(1) sets the timeout period to 1 second.

The s.connect_ex() function is used to attempt to connect to the target IP address and port. It returns an error indicator, which is checked to see if the port is open (error indicator 0) or closed (any other value).

If the port is open, the port number is printed to the console and the portCount variable is incremented.

The socket is closed using s.close().

The except statements handle various exceptions that may occur during the scan, such as a keyboard interrupt, a hostname resolution error, or a socket error.

If no open ports were found, a message is printed to the console to indicate this.

A banner is printed to the console with the time the scan completed and the total number of open ports found.
