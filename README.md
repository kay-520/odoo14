####安装依赖
```shell script
pip install -r requirements.txt
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

####安装单个依赖
```shell script
pip install pywin32
pip install --user pywin32
```

####创建模块
```shell script
python odoo-bin scaffold 子级 父级
```

####数据库中保存修改
```shell script
odoo-bin -u openacademy 
```

####问题
1.pg_config问题
```shell script
pip install --user psycopg2-binary
```


