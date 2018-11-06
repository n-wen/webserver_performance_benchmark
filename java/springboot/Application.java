package server;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import javax.annotation.PostConstruct;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;

@Controller
class ResponseController {
    private String constStr = "";
    @PostConstruct
    public void init(){
        final String constStrUnit = "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket";
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 200; i++){
            sb.append(constStrUnit);
        }
        this.constStr = sb.toString();
    }
    @RequestMapping("/")
    @ResponseBody
    @Async
    public CompletableFuture<String> index(@RequestParam(value="length", defaultValue = "1024") String lengthStr ){
        int length = Integer.parseInt(lengthStr);
        return CompletableFuture.completedFuture(this.constStr.substring(0, length));
    }
}

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args){
        SpringApplication.run(Application.class, args);
    }
    @Bean
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(4);
        executor.setMaxPoolSize(4);
        executor.initialize();
        return executor;
    }
}
