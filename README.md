# tor-rabbit
using tornado to recive message, and send message to rabbitmq 

use blocking client ,because the cliend can not keep connect ,so every handle must connect to rabbitmq ,

使用rabbitmq的client做全局连接，传递到request中去，会出现时间长，断开连接的情况，这里没使用异步方式，使用的是类似每个request实例化一个session连接的方式

normal computer to test,

Concurrency Level:      10

Time taken for tests:   5.854 seconds

Complete requests:      1000

Failed requests:        0

Total transferred:      144000 bytes

Total body sent:        35311000

HTML transferred:       0 bytes

Requests per second:    170.81 [#/sec] (mean)

Time per request:       58.544 [ms] (mean)

Time per request:       5.854 [ms] (mean, across all concurrent requests)

Transfer rate:          24.02 [Kbytes/sec] received

5890.15 kb/s sent
                        5914.17 kb/s total
