from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

print('\t\t========= AGUARDE =========')

driver = webdriver.Chrome(options=options)

driver.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

nome_time = driver.find_elements(By.CLASS_NAME, 'classificacao__equipes--nome')

pos_time = driver.find_elements(By.CLASS_NAME, 'classificacao__equipes--posicao')

pon_time = driver.find_elements(By.CLASS_NAME, 'classificacao__pontos--ponto')

nome_list = []
for e in nome_time:
    nome_list.append(e.text)

pos_list = []
for e in pos_time:
    pos_list.append(e.text)

pon_list = []
for e in pon_time:
    pon_list.append(e.text)

driver.quit()

list_time = []
for i, tim in enumerate(pos_list):
    list_time.append({'pos': pos_list[i], 'nome': nome_list[i], 'pont': pon_list[i]})

print('='*60)
print('\t\tEscolha o time:')
print('='*60)
for i, item in enumerate(list_time):
    print(f'{i} \t{item["nome"]}')
print('='*60)

tim = int(input('Digite o número do seu time? '))

print('='*60)
print(f"O clube {list_time[tim]['nome']} esta em {list_time[tim]['pos']}º lugar com {list_time[tim]['pont']} pontos no BRASILEIRÃO SÉRIE A 2023")
print('='*60)

