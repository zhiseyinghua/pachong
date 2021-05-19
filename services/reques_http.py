import requests
class RequestHandler:
    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url, params=params, headers=headers)
            return result
        except Exception as e:
            print("get请求错误: %s" % e)
    def post(self, url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        headers = kwargs.get("headers")
        # print(data,headers,url)
        try:
            result = requests.post(url, headers=headers, params=params, data=data)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
    def put(self, url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        headers = kwargs.get("headers")
        # print(data,headers)
        try:
            result = requests.post(url, headers=headers, params=params, data=data)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
    def run_main(self, method, **kwargs):
        """
        判断请求类型
        :param method: 请求接口类型
        :param kwargs: 选填参数
        :return: 接口返回内容
        """
        if method == 'get':
            result = self.get(**kwargs)
            return result
        elif method == 'post':
            result = self.post(**kwargs)
            return result
        else:
            print('请求接口类型错误')