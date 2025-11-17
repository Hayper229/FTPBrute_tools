# Импортируем необходимые библиотеки
import pandas as pd

# Читаем данные из файла
data = pd.read_csv('FTP_results.txt', sep='\t', header=None, names=['FTP'])

# Создаем HTML страницу
html_content = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты тестирования FTP</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #006400;
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #006400;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #004d00;
        }
    </style>
</head>
<body>
    <h1>Результаты тестирования FTP</h1>
    <table>
        <tr>
            <th>FTP</th>
        </tr>
'''

# Добавляем данные в таблицу
for index, row in data.iterrows():
    html_content += f'''
        <tr>
            <td>{row['FTP']}</td>
        </tr>
    '''

# Закрываем HTML теги
html_content += '''
    </table>
</body>
</html>
'''

# Записываем HTML в файл
with open('FTP_results.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
