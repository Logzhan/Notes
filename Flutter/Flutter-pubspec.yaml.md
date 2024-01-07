#### 依赖 git repository

依赖 Github 上的一个插件：

```text
dependencies:
  bloc:
    git:
      url: https://github.com/felangel/bloc.git
      ref: bloc_fixes_issue_110
      path: packages/bloc
```

- url：github 地址
- ref：表示git引用，可以是 **commit hash, tag** 或者 **branch**
- path：如果 git 仓库中有多个软件包，则可以使用此属性指定软件包