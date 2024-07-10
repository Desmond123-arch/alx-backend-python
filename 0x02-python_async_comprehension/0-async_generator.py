#!/usr/bin/env python3
""" An async generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ An async function that yields a random value"""
    for _ in range(10):
        yield (random.uniform(0, 10))
        await asyncio.sleep(1)
