# tor-rabbit
using tornado to recive message, and send message to rabbitmq 

use blocking client ,because the cliend can not keep connect ,so every handle must connect to rabbitmq ,

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
