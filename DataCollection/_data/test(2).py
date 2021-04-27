string = ['Motley Fool', "Why AMD Stock Didn't Fall in March", 'AMD (NASDAQ:AMD) shareholders outperformed the market by a wide margin last month. Shares ended up exactly where they started even as the S&P 500 ...', 'Apr 8, 2020']


# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

assert not isEnglish('slabiky, ale liší se podle významu')
assert isEnglish('English')
assert not isEnglish('ގެ ފުރަތަމަ ދެ އަކުރު ކަ')
assert not isEnglish('how about this one : 通 asfަ')
assert isEnglish('?fd4))45s&')

print(isEnglish(""))
