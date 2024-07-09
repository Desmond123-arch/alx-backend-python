#!/usr/bin/env python3
""" Execute multiple coroutines"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """ Calls wait_random n times"""
    vals = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        vals.append(await task)
    return vals