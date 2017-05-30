""" LoPy TTN LoRaWAN Nano Gateway configuration options for Australia """

# The Things Network configuration
GATEWAY_ID = '<gateway id>' # specified in when registering your gateway
SERVER = 'router.eu.thethings.network' # server address & port to forward received data to
PORT = 1700

# Configuration NTP server
NTP = "pool.ntp.org"       # NTP server for getting/setting time
NTP_PERIOD_S = 3600        # NTP server polling interval

# Wifi configuration
WIFI_SSID = '<wifi ssid>'
WIFI_PASS = '<wifi passord>'

# Lora configuration

# ... list of frequencies available for Australia
freq_list = [916800000,
             917000000,
             917200000,
             917400000,
             917600000,
             917800000,
             918000000,
             918200000]

# ... select the frequency and data rate
LORA_FREQUENCY = freq_list[6]
LORA_DR = "SF10BW125"

