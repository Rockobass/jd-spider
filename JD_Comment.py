import csv
import requests
import time


class comment_spider():
    def __init__(self, prod_ids, path):
        self.prod_ids = prod_ids
        self.path = path

    def Get_Comment_Data(self):
        for index, prod_id in enumerate(self.prod_ids):
            print("开始爬取第" + str(index) + "个商品评论")
            for i in range(1, 10000):
                params = {
                    "productId": prod_id,
                    "score": 0,
                    "sortType": 5,
                    "page": i,
                    "pageSize": 10
                }
                success = self.Parser_Comment_Data(params)
                print("获取了第" + str(i) + "页评论")
                if not success:
                    break

    def Parser_Comment_Data(self, params):
        print("等待三秒....")
        time.sleep(3)
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        }
        url = "https://club.jd.com/comment/productPageComments.action?"
        text = requests.get(url=url, headers=head, params=params).json()

        if not text.keys().__contains__("comments"):
            return False
        if len(text["comments"]) < 1:
            return False
        data = text["comments"]

        with open("%s//%s_comments.csv" % (self.path, params['productId']), "a", encoding="utf-8") as f:
            dic = {"nickname": "", "productColor": "", "productSize": "", "replyCount": "", "usefulVoteCount": "",
                   "content": "", "creationTime": ""}
            writer = csv.DictWriter(f, dic.keys())
            writer.writeheader()
            for da in data:
                dic = {}
                dic["nickname"] = da["nickname"]
                dic["productColor"] = da["productColor"]
                dic["productSize"] = da["productSize"]
                dic["replyCount"] = da["replyCount"]
                dic["usefulVoteCount"] = da["usefulVoteCount"]
                dic["content"] = da["content"]
                dic["creationTime"] = da["creationTime"]
                writer.writerow(dic)
            return True
