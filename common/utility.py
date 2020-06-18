# 验证码 pillow  
import random, string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from io import BytesIO

class ImageCode:
    # 生产用于绘制字符串的随机颜色
    def rand_color(self):
        red = random.randint(32,200)
        green = random.randint(22,255)
        blue = random.randint(0,200)
        return red, green, blue

    # 生产4位随机字符
    def gen_text(self, length):
        # sample用于从一个大的列表或者字符串中，随机取得N个字符，来构建出一个列表
        list = random.sample(string.ascii_letters+string.digits, length)
        return ''.join(list)

    def draw_lines(self, draw, num, width, height):
        for n in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width )
            y2 = random.randint(height / 2, height)
            draw.line(((x1,y1),(x2,y2)), fill=self.rand_color(), width=2)

    # 绘制验证码图片
    def draw_verify_code(self):
        length = 4
        width, height = 120, 50 # 图片大小
        #创建Image对象
        image = Image.new('RGB',(width,height),'white')
        #创建Font对象,选择字体
        font = ImageFont.truetype(font='arial.ttf', size=40)
        #创建Draw对象
        draw = ImageDraw.Draw(image)
        #验证码
        code = self.gen_text(length)
        #随机颜色验证码写到图片上
        for t in range(length):
            draw.text((random.randint(-3,3) + 23*t+5,5 + random.randint(-3,3)),text=code[t],font=font,fill=self.rand_color())
        
        # 绘制干扰线
        self.draw_lines(draw, 4, width, height)
        # image.show()  # 临时调试，可以显示出图片
        return code,image

    # 生成图片验证码并返回给控制器
    def get_code(self):
        code, image = self.draw_verify_code()
        buf =BytesIO()
        image.save(buf, 'jpeg')
        bstring = buf.getvalue()
        return code, bstring

    
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import smtplib
    
# 发送邮件验证码，参数为收件箱地址和随机生成的验证码
def send_email(receiver, ecode):
    sender = 'woniunote<1197498865@qq.com>'
    content = '感谢注册! 你的验证码为：' + ecode + '，请复制到注册窗口完成注册'
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = sender   # 发送者
    message['To'] =  receiver        # 接收者
    
    subject = '蜗牛笔记注册码'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = SMTP_SSL('smtp.qq.com')
    smtpObj.login(user='1197498865@qq.com',password='uuletrnpjzarfdha')
    smtpObj.sendmail(sender, receiver, str(message))
    smtpObj.quit()


# 生成6为随机字符串作为邮箱验证码
def gen_email_code():
    str = random.sample(string.ascii_letters + string.digits, 6)
    return ''.join(str)

# code = gen_email_code()
# print(code)
# send_email('1197498865@qq.com', code)