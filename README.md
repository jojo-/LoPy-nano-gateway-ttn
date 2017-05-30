# A nano gateway for The Things Networks with a LoPy 

This code allows to use the [LoPy 1.0](https://www.pycom.io/product/lopy/) board from Pycom as a single channel nano gateway for The Things Network.

The Things Network is a LoraWan-based communautary network for the internet of things (see [here](https://www.thethingsnetwork.org/) for more information). This code is powering the nano-gateway gateway of the [Wollongong Community](https://www.thethingsnetwork.org/community/wollongong/).

The original code can be found [here](https://github.com/pycom/pycom-libraries/tree/master/examples/lorawan-nano-gateway).

The parameters of the gateway are defined in the `config.py` file. You must also register the gateway in TTN and set it up as a legacy packet forwarder.

If you have some issue to connect a Multitech MTDOT node with AT commands, you probably need to set `AT+JD=5` so that the node is waiting 5 seconds before starting listening for a response from the gateway. Have a look [here](https://forum.pycom.io/topic/1262/nodes-unable-to-join-ttn-via-lopy-nano-gateway/) for more details.
