import time
import mytasks
from celery.result import AsyncResult

result = mytasks.add.delay(1, 2)
print(result)

while True:
	_result2 = AsyncResult(result.task_id)
	status = _result2.status
	print(status)
	if 'SUCCESS' in status:
		print('result after 5 sec wait is: {_result2}'.format(_result2=_result2.get()))
		break
	time.sleep(5)
