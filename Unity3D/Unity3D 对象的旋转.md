Unity3D 对象的旋转

```C#
Debug.Log("position " + transform.position); //世界坐标的位置
Debug.Log("localPosition " + transform.localPosition); //相对于父位置的坐标 即把父物体当作自己的中心
Debug.Log("eulerAngles " + transform.eulerAngles);//世界坐标欧拉⾓度
Debug.Log("localEulerAngles " + transform.localEulerAngles);//相对于⽗级的变换的旋转欧拉⾓度
Debug.Log("localScale " + transform.localScale);//相对于父位置的缩放
Debug.Log("localRotation " + transform.localRotation);//相对于父位置的旋转
Debug.Log("rotation " + transform.rotation);//世界坐标的旋转
```