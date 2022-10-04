## 一、X-Track执行页面的Unload过程

**1.1 在PageView中不需要删除对象**

​		准确的来说，应该是通过root节点创建的对象的是不需要删除的，对于非root节点创建的对象，如动画、style是需要在delete函数中删除的，否则会造成内存泄漏。

```c
lv_obj_del_async(base->root);
base->root = nullptr;
base->priv.IsCached = false;
base->onViewDidUnload();
```

​		从上面的代码可以看出X-Track先执行root节点的删除然后再调用onViewDidUnload()函数。由于在删除父节点的时候，子节点也会被删除，所以不建议在PageView里面调用lv_obj_del()函数。

​		
$$
y=k*(x-0)+b \\= k*(x-xt)+b = k*x-k*xt+b + k*xt
$$
