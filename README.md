# replutil

A collection of utilities for running services on [repl.it](https://replit.com).

Includes utilities for getting attributes of the container, as well as keeping the container alive using [the UptimeRobot API](https://uptimerobot.com/).

### Example

```py
from replutil import *
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)

with ReplKeepAlive("token"):
    # Do your long running operations here...
    sleep(40)
```

Registering servers, ports, and watchers are extracted away from the end user.
