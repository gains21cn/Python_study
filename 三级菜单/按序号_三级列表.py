dic_china = {
    "直辖市":{
        "北京市":["东城区","西城区","崇文区","宣武区","朝阳区","海淀区","丰台区",
          "石景山区","门头沟区","房山区","通州区","顺义区","昌平区","大兴区",
          "怀柔区","平谷区","延庆县","密云县",],
           },
    "省":{
        "浙江省":{
            "杭州市":["拱墅区","上城区","下城区","江干区","西湖区","滨江区","萧山区","余杭区","建德市","富阳市",
                   "临安市","桐庐县","淳安县"],
            "宁波市":["海曙区","江东区","江北区","北仑区","镇海区","鄞州区","余姚市","慈溪市","奉化市","象山县",
                   "宁海县"],
            "温州市":["鹿城区","龙湾区","瓯海区","瑞安市","乐清市","洞头县","永嘉县","平阳县","苍南县","文成县",
                   "泰顺县"],
            "嘉兴市":["南湖区","秀洲区","海宁市","平湖市","桐乡市","嘉善县","海盐县"],
            "湖州市":["吴兴区","南浔区","德清县","长兴县","安吉县"],
            "绍兴市":["越城区","诸暨市","上虞市","嵊州市","绍兴县","新昌县"],
            "金华市":["婺城区","金东区","兰溪市","义乌市","东阳市","永康市","武义县","浦江县","磐安县"],
        },
        "上海":{
                "黄埔区":{
                    "黄河路",
                    "人民广场",
                    "南京路",
                },
                "静安区":{
                    "静安寺",
                    "北京西路",
                },
                "虹口区":{
                    "大连路":{},
                    "飞虹路":{},
                    "公平路":{},
                },
                "杨浦区":{
                    "控江路",
                    "周家嘴路",
                    "军工路",
                },
            },
    }
}

print('欢迎使用中国省市查询工具'.center(30,'-'))
while True:
#---------遍历字典china，并编号输出城市分类信息------
    for i,j in enumerate(dic_china,1):
        print(i,j)
    choice = input('请选择想要查看的城市分类的编号[退出：q]：')
#---------判断输入编号是否正确----------
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(dic_china):
            #---------将客户选择的类别的城市信息存入新的字典中----------
            city_list = list(dic_china.keys())
            #---------判断客户是选择额直辖市类-------
            if city_list[choice-1] == '直辖市':
                dic_city = dic_china[city_list[choice-1]]
                print(''.center(50, '-'))
                for i, j in enumerate(dic_city, 1):
                    print(i, j)
                municipality_num = input('请选择想要查看的直辖市的编号[返回上一级菜单：q]：')
                #---------判断输入编号是否正确----------
                if municipality_num.isdigit():
                    municipality_num = int(municipality_num)
                    if 1 <= municipality_num <= len(dic_city):
                        municipality_list = list(dic_city.keys())
                        county_list = dic_city[municipality_list[municipality_num-1]]
                        print('以下是该直辖市下所有区的信息：')
                        print(county_list)
                elif municipality_num.upper() == 'Q':
                    print(''.center(50,'-'))
                else:
                    print('输入错误，请重新输入！！')
            else:
                dic_province = dic_china[city_list[choice-1]]
                print(''.center(50, '-'))
                #---------遍历字典dic_Province，并编号输出省级城市信息---------
                for i, j in enumerate(dic_province, 1):
                    print(i, j)
                province_num = input('请选择想要查看的省的编号[返回上一级菜单：q]：')
                # ---------判断输入编号是否正确----------
                if province_num.isdigit():
                    province_num = int(province_num)
                    if 1<= province_num <= len(dic_province):
                        # ---------将客户选择的市信息存入新的字典中----------
                        province_list = list(dic_province.keys())
                        dic_city = dic_province[province_list[province_num-1]]
                        print(''.center(50, '-'))
                        for i, j in enumerate(dic_city, 1):
                            print(i, j)
                        city_num = input('请选择想要查看的市的编号[返回上一级菜单：q]：')
                        if city_num.isdigit():
                            city_num = int(city_num)
                            if 1 <= city_num <= len(dic_city):
                                city_list = list(dic_city.keys())

                elif province_num.upper() == 'Q':
                    print(''.center(50,'-'))
                else:
                    print('输入错误，请重新输入！！')
        else:
            print('输入的编号不在城市分类的编号范围内，请重新输入！！')
    elif choice.upper() == 'Q':
        print('感谢您的使用！！')
    else:
        print('输入错误，请重新输入！！')