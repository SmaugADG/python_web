import re
import urllib.request



def get_movie_links():
    '''获取列表页影片信息'''
    file_list_url="https://m.dytt8.net/html/gndy/dyzz/list_23_2.html"
    response_list=urllib.request.urlopen(file_list_url)
    response_list_data=response_list.read()
    # 解码
    response_list_text=response_list_data.decode('GBK')
    # 匹配出列表
    url_list=re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>",response_list_text)
    # print(url_list)

    # 定义一个字典保存信息
    file_dict={}

    # 获取列表中的地址和名称
    i=0
    for content_url,file_name in url_list:
        content_url="https://m.dytt8.net"+content_url
        # print("地址：",content_url,file_name)

        # 打开每一个的地址
        response_content=urllib.request.urlopen(content_url)
        response_content_data=response_content.read()
        response_content_text=response_content_data.decode('GBK')

        # 匹配列表
        result=re.search(r"<a target=\"_blank\" href=\"(.*?)\"><strong><font",response_content_text)
        file_dict[file_name]=result.group(1)
        print("获取%d条"%i)
        i+=1


    return  file_dict

def main():
    films_dict=get_movie_links()

    for film_name,film_link in films_dict.items():
        print("%s | %s"%(film_name,film_link))


if __name__ == '__main__':
    main()
