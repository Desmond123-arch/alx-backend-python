#!/usr/bin/env python3
""" Basic async function """

import asyncio
from typing import Coroutine
import random


async def wait_random(max_delay: int = 10) -> float:
    """ A simple async corroutine """
    wait_val = random.uniform(0, max_delay)
    await asyncio.sleep(wait_val)
    return wait_val
