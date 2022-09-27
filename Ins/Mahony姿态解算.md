# **Mahony姿态解算**

## 一、Mahony算法中载体系的重力投影到地理系

​		常见代码的写法如下图所示：

```C
// 写法1
float halfvx = q1 * q3 - q0 * q2;
float halfvy = q0 * q1 + q2 * q3;
float halfvz = q0 * q0 - 0.5f + q3 * q3;
// 写法2
float vx = 2.0f*(q1*q3 - q0*q2);														 
float vy = 2.0f*(q0*q1 + q2*q3);															 
float vz = q0*q0 - q1*q1 - q2*q2 + q3*q3;
```

​		比较有差异的主要在于vz的写法，这两种的写法其实是一样的，推导如下所示
$$
\begin{align*}
  vz &= q_0^2-0.5+q_3^2 \\
  2vz &= 2q_0^2-1+2q_3^2 \\
    &= 2q_0^2+2q_3^2-q_0^2-q_1^2-q_2^2-q_3^2 \\
    &= q_0^2-q_1^2-q_2^2+q_3^2 \\
\end{align*}
$$
