#Функция принимает адреса в виде АДРЕС или http://АДРЕС, но всегда 
# возвращает адрес в виде https://АДРЕС. На вход функции также может поступить адрес 
# в уже нормализованном видел https://АДРЕС, в этом случае ничего менять не надо.
def normalize_url(url):
    http = 'https://'
    if url[:8] == http:
        return url
    else:
        if http[:7] == 'http://':
            return http + url[7:]
        else:
            return http + url
print(normalize_url('google.com'))
