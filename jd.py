from JD_Product import product_spider
import os

if __name__ == '__main__':
    keyword = input("请输入要采集商品的关键字：")
    path = input("请输入存储路径：")
    path += "//%s" % keyword
    try:
        os.mkdir(path)
    except:
        pass
    spider = product_spider(keyword, path)
    spider.Get_Product_Data()
