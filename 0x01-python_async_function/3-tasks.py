#!/usr/bin/env python3
""" Creating tasks """
import asyncio
from typing import AwaitableGenerator
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> AwaitableGenerator:
    """ Create and return a task"""
    return asyncio.create_task(wait_random(max_delay))