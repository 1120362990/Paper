import sys
# 01 未知异常拦截
try:
    print("ssss"+2222)
except Exception as e:
    print("未知问题!")
    print(e)
    print(e.with_traceback())
else:
    print("try 执行成功，我就会执行")
finally:
    print("我肯定会执行的")

# 02 手工抛出异常
# raise + 异常类
# raise ValueError