#начало. выбор языка
print('Добро пожаловать в калькулятор ИМТ (Индекс массы тела)', 'Welcome to the BMI (Body Mass Index) calculator.', sep='\n')
print('~~~~', 'Выберите язык.', 'Choose language.', '(rus, eng)', sep='\n')
language = input()

#проверка языка
if language == 'рус' or language == 'rus' or language == 'Rus' or language == 'RUS':
    height = int(input('Введите рост в сантиметрах: ')) / 100
    weight = float(input('Введите вес в килограммах: '))
    BMI = weight / height**2
    if BMI < 18.5:
        print(f'Недостаток веса ({BMI})', '~~~~', 'Хотите получить несколько советов по тому, как увеличить вес тела? (да, нет)', sep='\n')
        answer = input()
        if answer == 'ДА' or answer == 'Да' or answer == 'дА' or answer == 'да' or answer == 'lf':
            print('~~~~', '1. Обратитесь к врачу', 'Для начала вам будет необходимо посетить врача-диетолога или врача-терапевта, который правильно определит вашу массу тела и подберет необходимый и сбалансированный рацион питания.', '~~~~','Например, если вы пренебрегаете походом к врачу и едите здоровую еду, но без соблюдения баланса в рационе, то вы либо не наберете желаемый вес, либо получите излишек калорий, которые не пойдут вам на пользу.', '~~~~', 'Также врач-специалист определит причину низкого веса. Если проблем со здоровьем не будет обнаружено, то смело следуйте всем указанием врача и представленным ниже рекомендациям.', sep='\n')
            print('~~~~', '2. Увеличьте количество потребляемых полезных калорий', '~~~~', 'Самым важным при желании поправиться является: сбалансированное, регулярное и правильное для вашего организма питание.', '~~~~', 'Это касается не только полезной пищи, но и ее количества.', '~~~~', 'Точно выверенный объем калорий, который необходимо употреблять, чтобы набрать вес, зависит от таких факторов, как:', '~~~~', '- Ваш вес,', '  ', '- Обмен веществ,', '  ', '- Наследственность,', '  ', '- Возраст,', '  ', '- Пол,', '  ', '- Образ жизни', '  ', '- Гормональный фон', '~~~~', 'Если вы хотите набрать вес, то нужно употреблять больше калорий, чем их тратите в течение дня.', '~~~~', 'Для того, чтобы определить сколько калорий в день вы тратите, купите фитнес-браслет. Это устройство, которое поможет посчитать всю вашу активность в течение дня. А для того, чтобы понять сколько калорий в день вы употребляете, рекомендуем завести дневник питания. Каждый вечер записывайте туда все блюда, напитки и перекусы, которые были на вашем столе в течение дня.', '~~~~', 'Но все хорошо в меру, если потреблять сверх нормы для набора веса, то таким образом вы наберете лишнего, что уйдет в жир. Для того, чтобы это избежать занимайтесь физическими нагрузками и наращивайте мышечную массу, таким образом, вы наберете необходимый вес за ее счет.', '~~~~', 'Запомните, это просто советы!', '~~~~', 'Для большей информации, обратитесь к врачу!', sep='\n')
            print('Досвидания!')
            exit()
        else:
            print('Досвидания!')
            exit()
    elif 18.5 < BMI < 25:
        print(f'Это норма.({BMI})', '~~~~',  'Придерживайтесь своего текущего питания, не забывая пить витамины и есть полезную еду.', sep='\n')
        print('Досвидания!')
        exit()
    elif 25 < BMI < 30:
        print(f'Избыток веса.({BMI})', '~~~~', 'Вам не помешает соблюдать легкую диету, и придерживаться легкому дефициту каллорий.', '~~~~', 'Я могу порекомендовать вам список действий.(да, нет)', sep='\n')
        answer = input()
        if answer == 'Lf' or answer == 'Да' or answer == 'да' or answer == 'дА' or answer == 'lf':
            print('Установите специальное приложение на телефон, чтобы отслеживать каллории за день', '~~~~', 'Старайтесь есть больше белка и медленных углеводов', '~~~~', 'Запомните, это просто советы!', '~~~~', 'Для большей информации, обратитесь к врачу!', sep='\n')
            print('Досвидания!')
            exit()
        else:
            print('Досвидания!')
            exit()
    elif BMI >= 30:
        print(f'Ожирение.({BMI})', '~~~~', 'Вам необходимо соблюдать диету, чтобы избежать дальнейших осложнений. Вам необходимо обратиться к врачу диетологу, чтобы понять дальнейшие действия.')
        print('Досвидания!')
        exit()
elif language == 'Eng' or language == 'eng' or language == 'ENG' or language == 'eNG':
    height = float(input('Enter your height in feet through the dot: '))
    weight = float(input('Enter your weight in lbs: '))

    height_in_cm = (height * 30.48) / 100 #Конвертирование веса и роста из фунтов\футов в килограммы\сантиметры
    weight_in_cm = weight * 0.45359237 #Конвертирование веса и роста из фунтов\футов в килограммы\сантиметры

    BMI = weight_in_cm / height_in_cm ** 2
    
    if BMI < 18.5:
        print(f'Underweight ({BMI})', '~~~~', 'Would you like some tips on how to increase your body weight? (yes, no)', sep='\n')
        answer = input()
        if answer == 'YES' or answer == 'Yes' or answer == 'yES' or answer == 'yes' or answer == 'yeS':
            print('~~~~', '1. See a doctor', 'To begin with, you will need to visit a nutritionist or a general practitioner who will correctly determine your body weight and choose a proper and balanced diet.', '~~~~','For example, if you neglect going to the doctor and eat healthy foods but without balancing your diet, you will either not gain the weight you want or you will have an excess of calories that are not good for you.', '~~~~', 'The specialist will also determine the cause of the low weight. If no health problems are found, then feel free to follow all the doctors instructions and the recommendations below.', sep='\n')
            print('~~~~', '2. Increase your intake of healthy calories', '~~~~', 'The most important thing when wanting to get better is: eating a balanced, regular and proper diet for your body.', '~~~~', 'This applies not only to wholesome food, but also to the amount of it.', '~~~~', 'The exact amount of calories you should consume to gain weight depends on factors such as:', '~~~~', '- Your weight,', '  ', '- Metabolism,', '  ', '- Heredity,', '  ', '- Age,', '  ', '- Gender,', '  ', '- Lifestyle', '  ', '- Hormonal background', '~~~~', 'If you want to gain weight, you need to consume more calories than you expend during the day.', '~~~~', 'In order to determine how many calories per day you spend, buy a fitness bracelet. This is a device that will help you count all your activity during the day. And in order to understand how many calories a day you consume, it is recommended to start a food diary. Every evening, write down all the meals, drinks and snacks that were on your table during the day.', '~~~~', 'But everything is good in moderation, if you consume in excess of the norm for weight gain, then in this way you will gain extra, which will go into fat. In order to avoid this, exercise and build muscle mass, so you will gain the necessary weight at its expense.', '~~~~', 'Remember, these are just tips!', '~~~~', 'For more information, see your doctor!', sep='\n')
            exit()
        else:
            print('Goodbye!')
            exit()
    
    elif 18.5 < BMI < 25:
        print(f'Thats the norm.({BMI})', '~~~~',  'Stick to your current diet, remembering to drink vitamins and eat healthy foods.', sep='\n')
        exit()
    
    elif 25 < BMI < 30:
        print(f'Overweight.({BMI})', '~~~~', 'You could use a light diet, and stick to a light calorie deficit.', '~~~~', 'I can recommend a list of actions for you to take. (yes, no)', sep='\n')
        answer = input()
        if answer == 'YES' or answer == 'Yes' or answer == 'yES' or answer == 'yes' or answer == 'yeS':
            print('Install a special app on your phone to track your calories for the day', '~~~~', 'Try to eat more protein and slow carbohydrates', '~~~~', 'Remember, these are just tips!', '~~~~', 'For more information, see your doctor!', sep='\n')
            print('Goodbye!')
            exit()
        else:
            print('Goodbye!')
    
    elif BMI >= 30:
        print(f'Obesity.({BMI})', '~~~~', 'You need to follow a diet to avoid further complications. You should see a nutritionist to understand your next steps.')
        print('Goodbye!')
        exit()
else:
    print('Ошибка. Повторите снова, перезапустив программу.', 'Error. Repeat again by restarting the program.', sep='\n')
    exit()