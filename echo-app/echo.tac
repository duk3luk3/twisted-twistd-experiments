#!/usr/bin/twistd -ny

from twisted.application import internet, service
from echo_factory import EchoFactory

port = 7001
factory = EchoFactory()

# this is the important bit
application = service.Application("echo")  # create the Application
echoService = internet.TCPServer(port, factory) # create the service
# add the service to the application
echoService.setServiceParent(application)
