# Android 线程池ThreadPoolExecutor 的使用和封装（kotlin）

```java
// 传统开启线程方式
Thread(Runnable {
     //to do异步请求
 
}).start()
```

**1.使用new Thread()创建线程存在的问题**  

1. 如果在一个list每一个item都创建一个Thread，list量大的话会大量创建Thread，导致内存抖动，GC频繁的回收。要知道，GC的回收是在主线程的，这样会导致卡顿。

2. 线程过多，导致各个线程竞争抢夺CPU执行权，线程的频繁切换导致效率的降低。

3.  ListView的每一个item滑出窗口，线程无法停止也无法控制。
   

**2.使用线程池的好处**

1. 重用已经创建的好的线程，避免频繁创建进而导致的频繁GC
2. 控制线程并发数，合理使用系统资源，提高应用性能
3. 可以有效的控制线程的执行，比如定时执行，取消执行等

**3.创建线程池 ThreadPoolExecutor 7个参数**

- corePoolSize  线程池中核心线程的数量

- maximumPoolSize  线程池中最大线程数量，等待队列的任务塞满了之后，才会触发开启非核心线程，直到总线程数达到 maximumPoolSize  

- keepAliveTime 非核心线程的超时时长，当系统中非核心线程闲置时间超过keepAliveTime之后，则会被回收。如果ThreadPoolExecutor的allowCoreThreadTimeOut属性设置为true，则该参数也作用于核心线程的超时时长

- unit 第三个参数的单位，有纳秒、微秒、毫秒、秒、分、时、天等

- workQueue 线程池中的任务队列，该队列主要用来存储已经被提交但是尚未执行的任务。存储在这里的任务是由ThreadPoolExecutor的execute方法提交来的。这个队列任务塞满了之后，才会触发开启非核心线程

- threadFactory  为线程池提供创建新线程的功能，这个我们一般使用默认即可

- handler 拒绝策略，当线程无法执行新任务时（一般是由于线程池中的线程数量已经达到最大数或者线程池关闭导致的），默认情况下，当线程池无法处理新线程时，会抛出一个RejectedExecutionException。

**4.线程池 ThreadPoolExecutor 的方法**

1. shutDown()  关闭线程池，不影响已经提交的任务

2. shutDownNow() 关闭线程池，并尝试去终止正在执行的线程

3. allowCoreThreadTimeOut(boolean value) 允许核心线程闲置超时时被回收
   

```java
 
 
import com.orhanobut.logger.Logger
import java.util.concurrent.*
 
/***
 *      Created by LiangJingJie on 2019/5/16.
 *      线程池封装类
 * */
class ThreadPoolManager private constructor() {
 
    private var threadPoolMap = hashMapOf<String, ThreadPoolExecutor>()
 
    /**
     * cpu数量
     * */
    private val CPU_COUNT = Runtime.getRuntime().availableProcessors()
 
    /**
     * 核心线程数为手机CPU数量+1
     * */
    private val CORE_POOL_SIZE = CPU_COUNT + 1
 
    /**
     * 最大线程数为手机CPU数量×2+1
     * */
    private val MAXIMUM_POOL_SIZE = CPU_COUNT * 2 + 1
 
    /**
     * 线程活跃时间 秒，超时线程会被回收
     * */
    private val KEEP_ALIVE_TIME: Long = 3
 
    /**
     * 等待队列大小
     * */
    private val QUEUE_SIZE = 128
 
    companion object {
        fun getInstance() = SingleHolder.SINGLE_HOLDER
    }
 
    object SingleHolder {
        val SINGLE_HOLDER = ThreadPoolManager()
    }
 
 
    /**
     *   @param tag 针对每个TAG 获取对应的线程池
     *   @param corePoolSize  线程池中核心线程的数量
     *   @param maximumPoolSize  线程池中最大线程数量
     *   @param keepAliveTime 非核心线程的超时时长，
     *   当系统中非核心线程闲置时间超过keepAliveTime之后，则会被回收
     *   如果ThreadPoolExecutor的allowCoreThreadTimeOut属性设置为true，
         则该参数也作用于核心线程的超时时长
     *   @param unit 第三个参数的单位，有纳秒、微秒、毫秒、秒、分、时、天等
     *   @param queueSize 等待队列的长度 一般128 (参考 AsyncTask)
     *   workQueue 线程池中的任务队列，
        该队列主要用来存储已经被提交但是尚未执行的任务。
        存储在这里的任务是由ThreadPoolExecutor的execute方法提交来的。
     *   threadFactory  为线程池提供创建新线程的功能，这个我们一般使用默认即可
     *
     *   1.ArrayBlockingQueue：这个表示一个规定了大小的BlockingQueue，ArrayBlockingQueue的构造函数接受一个int类型的数据，
     *              该数据表示BlockingQueue的大小，存储在ArrayBlockingQueue中的元素按照FIFO（先进先出）的方式来进行存取。
     *   2.LinkedBlockingQueue：这个表示一个大小不确定的BlockingQueue，在LinkedBlockingQueue的构造方法中可以传
     *          一个int类型的数据，这样创建出来的LinkedBlockingQueue是有大小的，也可以不传，不传的话，
     *          LinkedBlockingQueue的大小就为Integer.MAX_VALUE
     * */
    private fun getThreadPool(tag: String): ThreadPoolExecutor {
        var threadPoolExecutor = threadPoolMap[tag]
        if (threadPoolExecutor == null) {
            threadPoolExecutor = ThreadPoolExecutor(
                CORE_POOL_SIZE,
                MAXIMUM_POOL_SIZE,
                KEEP_ALIVE_TIME,
                TimeUnit.SECONDS,
                ArrayBlockingQueue<Runnable>(QUEUE_SIZE),
                Executors.defaultThreadFactory(),
                RejectedExecutionHandler { _, _ ->
                    Logger.d("$ThreadPoolManager  RejectedExecutionHandler----")
                }
            )
            //允许核心线程闲置超时时被回收
            threadPoolExecutor.allowCoreThreadTimeOut(true)
            threadPoolMap[tag] = threadPoolExecutor
        }
        return threadPoolExecutor
    }
 
    /**
     *  @param tag 针对每个TAG 获取对应的线程池
     *  @param runnable 对应的 runnable 任务
     * */
    fun removeTask(tag: String, runnable: Runnable) {
        getThreadPool(tag)?.queue?.remove(runnable)
    }
 
    /**
     *  @param tag 针对每个TAG 获取对应的线程池
     *  @param runnable 对应的 runnable 任务
     * */
    fun addTask(tag: String, runnable: Runnable) {
        getThreadPool(tag).execute(runnable)
    }
 
    /**
     *   @param tag 针对每个TAG 获取对应的线程池
     *   取消 移除线程池
     * */
 
    //shutDown()：关闭线程池后不影响已经提交的任务
    //shutDownNow()：关闭线程池后会尝试去终止正在执行任务的线程
    fun exitThreadPool(tag: String) {
        var threadPoolExecutor = threadPoolMap[tag]
        if (threadPoolExecutor != null) {
            threadPoolExecutor.shutdownNow()
            threadPoolMap.remove(tag)
        }
    }
}
```

