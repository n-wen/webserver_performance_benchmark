webserver性能测试
====

受http-kit [600k concurrent HTTP connections, with Clojure & http-kit](http://www.http-kit.org/600k-concurrent-connection-http-kit.html)启发，
利用[ConcurrencyBench](https://github.com/http-kit/scale-clojure-web-app/blob/master/ConcurrencyBench.java) 进行性能测试，尽可能加大并发。

![benchmark](./static/bench.png)