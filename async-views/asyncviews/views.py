import asyncio
import time

import httpx
from django.http import JsonResponse, HttpResponse


def api(request):
    time.sleep(1)
    payload = {'message': 'Hello from Here!'}

    if 'task_id' in request.GET:
        payload['task_id'] = request.GET['task_id']
    return JsonResponse(payload)


async def httpio_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient as client:
        r = await client.get('https://httpbin.org')


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(httpio_call_async())
    return HttpResponse('Non-blocking HTTP request')
