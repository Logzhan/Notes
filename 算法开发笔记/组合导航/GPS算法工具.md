## GPS 算法Python工具

一、距离的计算

```python
#--------------------------------------------------------------------------
# Function    : cal_distance
# Descripiton : 给定经纬度, 计算两点之间距离m
# Author      : zhanli@vivo.com
# Date        : 2022-07-06
#--------------------------------------------------------------------------
def cal_distance(lat1,lon1,lat2,lon2):
	dis = 0
	# WGS-84椭球体长半轴
	WGS84_RE = 6378136.49				        
	# 第一偏向率的平方，e^2(WGS-84)
	WGS84_ECCENTR2 = 6.69437999014e-3
	# 角度转弧度系数
	DEG2RAD = 0.017453292                      

	lat = lat1 * DEG2RAD

	sinLat = math.sin(lat)
	p = 1 - WGS84_ECCENTR2 * (sinLat * sinLat)
	temp =  math.sqrt(p)

	rmh = WGS84_RE * (1 - WGS84_ECCENTR2) / (p*temp)
	rnh = WGS84_RE * math.cos(lat) / temp

	rmh *= DEG2RAD
	rnh *= DEG2RAD

	latDiff = rmh*(lat1 - lat2)
	lonDiff = rnh*(lon1 - lon2)

	dis = math.sqrt(latDiff*latDiff + lonDiff*lonDiff)
	
	return dis
```

