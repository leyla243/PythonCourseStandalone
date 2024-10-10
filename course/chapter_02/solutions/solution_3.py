temperature = int(input())

if temperature >= 25:
    print("Сегодня жарко, наденьте легкую одежду.")
elif 25 > temperature >= 15:
    print("На улице тепло, наденьте что-то удобное.")
elif 15 > temperature >= 0:
    print("На улице прохладно, возьмите с собой куртку.")
else:
    print("Очень холодно, одевайтесь теплее.")