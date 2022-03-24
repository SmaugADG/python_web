from gevent import monkey
monkey.patch_all()
import urllib.request
import gevent

def download_img(img_url,filename):
    try:
        # 打开URL
        response=urllib.request.urlopen(img_url)
        # 创建文件
        with open(filename,'wb') as img_file:
            # 通过循环读取数据保存到变量中
            while True:
                img_data=response.read(1024)
                # 如果读取成功，则写数据到文件中（不为空）
                if img_data:
                    img_file.write(img_data)
                else:
                    break

    except Exception as e:
        print("文件%s下载失败！ %s"%(filename,str(e)))
    else:
        print("图片%s下载完成！"%filename)


if __name__ == '__main__':
    imd_url1="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=eva%E5%A3%81%E7%BA%B8&step_word=&hs=0&pn=39&spn=0&di=7060663421280190465&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2111494824%2C1263560803&os=2227686603%2C731991126&simid=3462747125%2C272909381&adpicid=0&lpn=0&ln=1149&fr=&fmq=1648050460973_R&fm=result&ic=&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fe7ce44cf591c96d20f057e32dcce20995ed4ed71.jpg%26refer%3Dhttp%3A%2F%2Fi0.hdslb.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1650642473%26t%3D763468f0ac75834f4d64d1b6c22a546f&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bktstktst_z%26e3Bv54AzdH3F6jw1AzdH3Fvedbcbb0aAzdH3F&gsm=27&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCw2LDQsNSwzLDEsNyw4LDIsOQ%3D%3D"
    imd_url2="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=eva%E5%A3%81%E7%BA%B8&step_word=&hs=0&pn=170&spn=0&di=7060663421280190465&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1186534903%2C2128669365&os=1473791475%2C2011804515&simid=3219836145%2C3839950067&adpicid=0&lpn=0&ln=1149&fr=&fmq=1648050460973_R&fm=result&ic=&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fss1.baidu.com%2F9vo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2Fac4bd11373f08202cba3fad24bfbfbedab641b2d.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fzit1w5_z%26e3Bkwt17_z%26e3Bv54AzdH3Fq7jfpt5gAzdH3Fcaccc8lc8_z%26e3Bip4s&gsm=ad&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCw2LDQsNSwzLDEsNyw4LDIsOQ%3D%3D"
    imd_url3="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=eva%E5%A3%81%E7%BA%B8&step_word=&hs=0&pn=182&spn=0&di=7060663421280190465&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=381258162%2C1300906287&os=1964966219%2C2350044947&simid=3191566821%2C3826781904&adpicid=0&lpn=0&ln=1149&fr=&fmq=1648050460973_R&fm=result&ic=&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fgss0.baidu.com%2F94o3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2Fc995d143ad4bd1136b84519158afa40f4afb05c3.jpg%26refer%3Dhttp%3A%2F%2Fgss0.baidu.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1650642599%26t%3Daec24c47f213d14f52dadff6953dbae5&fromurl=ippr_z2C%24qAzdH3FAzdH3Fzit1w5_z%26e3Bkwt17_z%26e3Bv54AzdH3Fq7jfpt5gAzdH3F9bb9bblm8mbmcnmcnd_z%26e3Bip4s&gsm=b8&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCw2LDQsNSwzLDEsNyw4LDIsOQ%3D%3D"

    gevent.joinall([
        gevent.spawn(download_img,imd_url1,"img/1.jpg"),
        gevent.spawn(download_img,imd_url2,"img/2.jpg"),
        gevent.spawn(download_img,imd_url3,"img/3.jpg")
    ])