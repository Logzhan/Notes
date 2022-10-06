# C++笔记

**一、C++字符串的本质**

​		对于char*类型的字符串而言，其字符串的内容都在程序的静态存储区。其指针指向这篇内存的首地址。

```C
    const char* str1 = "this is str1";
    const char* str2 = "this is str2";
    char* str = str1;
    printf("%s\n", str);
    str = str2;
    printf("%s\n", str);
```

**二、字符串的拷贝**

​		字符串在拷贝的时候，其实本质就是内存的复制过程。 字符串名其实是一个指针，所以无法知道字符串的长度，所以一般C语言里面都是用'\0'符号表示字符串的结尾，如果没有'\0'可能会导致strlen等函数无法取得正确的结果。

```C
    char  OldSSID[32] = { 0 };
    char* NewSSID     = "MySSID";
    /*Copy the string content. */
    strcpy(OldSSID, NewSSID);
    /* Output the result. */
    printf("wifi ssid = %s\n", OldSSID);
```

​		其实，上述的本质就是按照每一位进行复制直到复制到'\0'结束，所以使用memcpy函数也可以实现同样的效果。值得注意的是，strlen只能计算非'\0'部分的长度，所以在memcpy的时候需要多拷贝一位，printf才能正确的打印函数。'\0'对于编译器判断字符串的结尾位置非常的重要，如果没有'\0'结束标志位可能会导致越界读取内存从而导致出错问题。

```c
    char  OldSSID[32] = { 'O','r','i','g','i','n','P','a'};
    char* NewSSID     = "MySSID";
    /*Copy the string content. */
    memcpy(OldSSID, NewSSID, strlen(NewSSID) + 1);
    /* Output the result. */
    printf("wifi ssid = %s\n", OldSSID);
```

