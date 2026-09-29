def cen_mes(name, age, cur_ye):
    hun=cur_ye + (100-age)
    return f"{name}, тебе исполнится 100 лет в {hun} году"
print(cen_mes("Any",20,2025))
