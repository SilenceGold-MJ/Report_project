
from pyecharts import options as opts
from pyecharts.charts import Page, Pie
from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Liquid

width='1100px'
height='500px'

def Fanchart_1(dic):#扇形
        # key = ['哈哈1', '哈2', '哈3', '哈4', '哈5', ]
        # values = ['53', '56', '57', '36', '76', ]

        # dic={
        #         "key":key,
        #           "values":values,
        #             'titlename':titlename,
        #         "htmlname":htmlname,
        # }
        #

        pie = (
                Pie(init_opts = opts.InitOpts(width=width,height=height))
                        .add("", [list(z) for z in zip(dic['key'], dic['values'])])
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title=dic['titlename']),
                        legend_opts=opts.LegendOpts(
                                orient="vertical", pos_top="2%", pos_left="80%"
                                # orient="vertical"设置图例垂直
                        ),
                )
        )
        pie.render("./static/html/%s" % dic['htmlname'])  # 保存图片为HTML网页

def Fanchart(dic):#扇形
    key_new=[]
    for i in range(len(dic['values'])):


        share=str(round((dic['values'][i] / sum(dic['values']) if sum(dic['values'])!=0 else 0.0)* 100, 2) ) + '%'
        key_new.append("%s %s "%(dic['key'][i],share))

    pie = (
        Pie(init_opts = opts.InitOpts(width=width,height=height))
            .add("", [list(z) for z in zip(key_new, dic['values'])])  # 加入数据
            .set_global_opts(title_opts=opts.TitleOpts(title=dic['titlename']),legend_opts=opts.LegendOpts(orient="vertical", pos_top="2%", pos_left="81%"))  # 全局设置项



            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {c}")))  # 样式设置项
    pie.render("./static/html/%s" % dic['htmlname'])  # 保存图片为HTML网页







def Bar_chart_1(dic):#条线


        # key = ['哈哈1', '哈2', '哈3', '哈4', '哈5', ]
        # values = ['53', '56', '57', '36', '76', ]
        # dic={
        #         "key":key,
        #         "values":values,
        #         'titlename':"7天来BUG增量",
        #         'htmlname':"htmlname.html"
        #
        # }


        bar = (
                Bar(init_opts = opts.InitOpts(width=width,height=height))
                        .add_xaxis(dic['key'])
                        .add_yaxis(dic["legend"], dic['values'])
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title=dic["titlename"]),
                        datazoom_opts=opts.DataZoomOpts(),
                )
        )

        bar.render("./static/html/%s" % dic['htmlname'])

def Bar_chart(dic):#条线
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    bar = (
        Bar(init_opts = opts.InitOpts(width=width,height=height))
            .add_xaxis(dic['key'])
            .add_yaxis(dic["legend"], dic['values'])
            .set_global_opts(title_opts=opts.TitleOpts(title=dic["titlename"]),

                yaxis_opts=opts.AxisOpts(name="bug数"),
                xaxis_opts=opts.AxisOpts(name="时间"))

        #, datazoom_opts=opts.DataZoomOpts(type_="inside")

            # .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            #                  title_opts=opts.TitleOpts(title=dic["titlename"], subtitle=""))

        #     .set_global_opts(title_opts=opts.TitleOpts(title=dic["titlename"]))
        #     .set_series_opts(
        #     label_opts=opts.LabelOpts(is_show=False),
        #     markline_opts=opts.MarkLineOpts(
        #         data=[
        #             opts.MarkLineItem(type_="min", name="最小值"),
        #             opts.MarkLineItem(type_="max", name="最大值"),
        #             opts.MarkLineItem(type_="average", name="平均值"),
        #         ]
        #     ),
        # )
    )
    bar.render("./static/html/%s" % dic['htmlname'])
def Bar_chart_vertical(dic):#条形图竖
    bar = (
        Bar(init_opts = opts.InitOpts(width=width,height=height))
            .add_xaxis(dic['key'])
            .add_yaxis(dic["legend"], dic['values'])
            #.add_yaxis("商家B", Faker.values())
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title=dic["titlename"]))
    )

    bar.render("./static/html/%s" % dic['htmlname'])




def Line_chart(dic):#折现图
    # key = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期七', '星期日']
    # values = [100, 200, 300, 400, 100, 400, 300]
    # values2 = [200, 300, 200, 100, 200, 300, 400]
    # dic = {
    #     "key": key,
    #     "values": values,
    #     'series_name': "series_name",  # 图例名
    #     'titlename': "7天来BUG增量",
    #     'htmlname': "htmlname.html"
    # }
    # Line_chart(dic)

    line = (
        Line(init_opts = opts.InitOpts(width=width,height=height))
            .add_xaxis(xaxis_data=dic["key"])
            .add_yaxis(series_name=dic['series_name'], y_axis=dic['values'], is_smooth=True)
            # .add_yaxis(series_name="y2线",y_axis=y2, is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title=dic["titlename"]))
    )
    line.render_notebook()
    line.render("./static/html/%s" % dic['htmlname'])  # 保存图片为HTML网页

def progress_chart(dic):#进度图


    c = (
        Liquid(init_opts = opts.InitOpts(width=width,height=height))
            .add("", [dic['share'], dic['share']])
            .set_global_opts(title_opts=opts.TitleOpts(title=dic["titlename"]))
            .render("./static/html/%s" % dic['htmlname'])
            #.render_embed()
    )
    return c
