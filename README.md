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

Registering servers, ports, and watchers are abstracted away from the end user.

When used as a context manager, the library will automatically handle registering and deregistering watchers as well as staring and keeping open webservers.

If this is used in a larger project, like, say, a Discord bot, you should do any asyncio event loop logic (including `Client.run`) in the context manager scoping block.

### Install

You can install this package via pip:

```
pip install git+https://github.com/regulad/replutil.git
```
