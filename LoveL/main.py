import time
import random
from LoveF import score
from LoveF import user
from LoveF import mydriver
from LoveF.mydriver import Mydriver

def user_flag(uname):
    driver_login = mydriver.Mydriver(nohead=False)
    cookies = driver_login.login()
    a_log = user.get_a_log(uname)
    v_log = user.get_v_log(uname)
    d_log = user.get_d_log(uname)
    return cookies, a_log, v_log, d_log

def show_score(cookies):
    total, each = score.get_score(cookies)
    print("当前学习总积分：" + str(total))
    print("阅读文章:{}/6,观看视频:{}/6,登陆:{}/1,文章时长:{}/6,视频时长:{}/6,每日答题:{}/6,每周答题:{}/5,专项答题:{}/10".format(*each))
    # print("阅读文章:",each[0],"/6,观看视频:",each[1],"/6,登陆:",each[2],"/1,文章时长:",each[3],"/6,视频时长:",each[4],"/6,每日答题:",each[5],"/6,每周答题:",each[6],"/5,专项答题:",each[7],"/10")
    return total, each

def article(cookies, a_log, each):
    if each[0] < 6 or each[3] < 8:
        driver_article = mydriver.Mydriver(nohead=False)
        driver_article.get_url("https://www.xuexi.cn/notFound.html")
        driver_article.set_cookies(cookies)
        links = get_links.get_article_links()
        try_count = 0
        readarticle_time = 0
        while True:
            if each[0] < 6 and try_count < 10:
                a_num = 6 - each[0]
                for i in range(a_log, a_log + a_num):
                    driver_article.get_url(links[i])
                    readarticle_time = 60 + random.randint(5, 15)
                    for j in range(readarticle_time):
                        if random.random() > 0.5:
                            driver_article.go_js('window.scrollTo(0, document.body.scrollHeight/120*{})'.format(j))
                        print("\r文章学习中，文章剩余{}篇,本篇剩余时间{}秒".format(a_log + a_num - i, readarticle_time - j), end="")
                        time.sleep(1)
                    driver_article.go_js('window.scrollTo(0, document.body.scrollHeight)')
                    total, each = show_score(cookies)
                    if each[0] >= 6:
                        print("检测到文章数量分数已满,退出学习")
                        break
                a_log += a_num
            else:
                with open("./user/{}/a_log".format(uname), "w", encoding="utf8") as fp:
                    fp.write(str(a_log))
                break
        try_count = 0
        while True:
            if each[3] < 6 and try_count < 10:
                num_time = 60
                driver_article.get_url(links[a_log - 1])
                remaining = (6 - each[3]) * 1 * num_time
                for i in range(remaining):
                    if random.random() > 0.5:
                        driver_article.go_js(
                            'window.scrollTo(0, document.body.scrollHeight/{}*{})'.format(remaining, i))
                    print("\r文章时长学习中，文章总时长剩余{}秒".format(remaining - i), end="")
                    time.sleep(1)
                    if i % (60) == 0 and i != remaining:
                        total, each = show_score(cookies)
                        if each[3] >= 6:
                            print("检测到文章时长分数已满,退出学习")
                            break
                driver_article.go_js('window.scrollTo(0, document.body.scrollHeight)')
                total, each = show_score(cookies)
            else:
                break
        if try_count < 10:
            print("文章学习完成")
        else:
            print("文章学习出现异常，请检查用户名下a_log文件记录数")
        driver_article.quit()
    else:
        print("文章之前学完了")


if __name__ == '__main__':
    #  0 读取版本信息
    start_time = time.time()
    print("=" * 120,'''
    现支持以下模式（答题时请值守电脑旁处理少部分不正常的题目）：
    1 文章+视频
    2 每日答题+每周答题+专项答题+文章+视频
      （可以根据当日已得做题积分，及是否有可得分套题，决定是否做题）
    3 每日答题+文章+视频
      （可以根据当日已得做题积分，决定是否做题）
    ''',"=" * 120)
    mode = input("请选择模式（输入对应数字）并回车： ")
    #  1 创建用户标记，区分多个用户历史纪录
    uname = user.get_user()
    cookies, a_log, v_log, d_log = user_flag(uname)
    total, each = show_score(cookies)
