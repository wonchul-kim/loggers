## logging


### Log levels

|Level|	설명|
|-----|-----|
|DEBUG|	간단히 문제를 진단하고 싶을 때 필요한 자세한 정보를 기록함|
|INFO|	계획대로 작동하고 있음을 알리는 확인 메시지|
|WARNING|	소프트웨어가 작동은 하고 있지만, 예상치 못한 일이 발생했거나 할 것으로 예측된다는 것을 알림|
|ERROR|	중대한 문제로 인해 소프트웨어가 몇몇 기능들을 수행하지 못함을 알림|
|CRITICAL|	작동이 불가능한 수준의 심각한 에러가 발생함을 알림|


### LogRecord 

```python
logging.LogRecord(name, level, pathname, lineno, msg, …)
```

LogRecord 객체는 Logger에 의해 자동적으로 생성되며, 수동으로 생성하려면 makeLogRecord 메서드를 이용하면 된다.

여기서 pathname은 logging call이 만들어지는 소스 파일의 전체 pathname을 의미한다.
lineno는 logging call이 만들어지는 소스파일의 라인 번호를 말한다.
msg는 event description 메시지를 의미한다.

이 LogRecord는 여러 속성(attribute)을 갖고 있는데, 이 속성들은 format을 정의하는데 활용된다.
그 리스트와 설명은 아래와 같다.

|속성 이름|format |설명|
|-------|-------|----|
|asctime|%(asctime)s|인간이 읽을 수 있는 시간 표시|
|created|%(created)f|logRecord가 만들어진 시간|
|filename|%(filename)s|pathname의 file 이름 부분|
|funcName|%(funcName)s|logging call을 포함하는 function의 이름|
|levelname|%(levelname)s|메시지의 Text logging level: 예) INFO|
|lineno|%(lineno)d|logging call이 발생한 코드의 line 숫자|
|module|%(module)s|filename의 모듈 이름 부분|
|message|%(message)s|메시지|
|name|%(name)s|logger의 이름|
|pathname|%(pathname)s|full pathname|
|thread|%(thread)d|thread ID|
|threadName|%(threadName)s|thread 이름|


#### References
- https://greeksharifa.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/2019/12/13/logging/