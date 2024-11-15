from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import json

def configurarDriver():
    #service = Service()
    options = webdriver.ChromeOptions()
    #maximizar la pagina
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def llamarUsuarios():
    #llamar al json con credenciales
    with open('credenciales.json') as file:
        return json.load(file)
    
def llamarDatosSelect():
    with open('options.json') as file:
        return json.load(file)

def procesoVotar(votante, opcion):
    try: 
        driver = configurarDriver()

        driver.get("https://elecciones.cnn.cl/")

        try:
            email = driver.find_element(By.XPATH, "/html/body/app-root/main/app-login-page/form/div/div[2]/input")
            email.send_keys(votante['correo'])
            password = driver.find_element(By.XPATH, "/html/body/app-root/main/app-login-page/form/div/div[3]/input")
            password.send_keys(votante['clave'])

            # Clic en el botón de inicio de sesión
            login_button = driver.find_element(By.XPATH, "/html/body/app-root/main/app-login-page/form/div/div[4]/button")
            login_button.click()
            
            #Interaccion con el menu
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sideNav']/ul/li[2]/a")))
            voto_nav = driver.find_element(By.XPATH, "//*[@id='sideNav']/ul/li[2]/a")
            voto_nav.click()

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submenuVotos']/div/ul/li/a")))
            voto_button = driver.find_element(By.XPATH, "//*[@id='submenuVotos']/div/ul/li/a")
            voto_button.click()
            time.sleep(2)

            #Selecionar tipo eleccion
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[1]/div/select")))
            select_eleccion = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[1]/div/select")
            select_eleccion.click()
            
            opcion_eleccion = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[1]/div/select/option")
            opcion_eleccion.click() 

            #Selecionar comuna
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[2]/div/select")))
            select_comuna = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[2]/div/select")
            select_comuna.click()
            
            opcion_comuna = driver.find_element(By.XPATH, f"/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[2]/div/select/option[{opcion['comuna']}]")
            opcion_comuna.click()

            #Selecionar local
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[3]/div/select")))
            select_local = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[3]/div/select")
            select_local.click()
            time.sleep(2)
            
            opcion_local = driver.find_element(By.XPATH, f"/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[3]/div/select/option[{opcion['local']}]")
            opcion_local.click()

            #Ingresar numero de mesa
            nro_mesa = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[4]/div/input")
            nro_mesa.send_keys(opcion['nroMesa'])

            #Abrir mesa
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[5]/button")))
            mesa_button = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/form/div/div[5]/button")
            mesa_button.click()

            time.sleep(4)

            try:
                if votante['id'] % 2 == 0:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[1]/div/div/article/div[2]/button[2]")))
                    input_field_1 = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[1]/div/div/article/div[2]/input")
                    #input_field_1.clear()
                    suma_voto_button_1 = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[1]/div/div/article/div[2]/button[2]")
                    for i in range(100):
                        suma_voto_button_1.click()
                        time.sleep(1)
                else:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[2]/div/div/article/div[2]/button[2]")))
                    input_field_2 = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[2]/div/div/article/div[2]/input")
                    #input_field_2.clear()
                    suma_voto_button_2 = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[2]/div/div/article/div[2]/button[2]")
                    for i in range(100):
                        suma_voto_button_2.click()
                        time.sleep(1)
            except Exception as e:
                print(f"Error al seleccionar candidato para el usuario {votante['correo']}: {e}")


            #volver a la mesa
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[4]/div/button[1]")))
            cerrar_button = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-voto-a-voto-page/div/div[2]/div/div/div/div[4]/div/button[1]")
            cerrar_button.click()

            time.sleep(3)

        except Exception as e:
            print(f"Error con el usuario {votante['correo']}: {e}")

    finally:
        driver.quit()

def ejecutar():
    # Obtener los votantes del json
    votantes = llamarUsuarios()
    print(f"Usuarios cargados: {votantes}")

    opciones = llamarDatosSelect()

    # Ejecutar el proceso de votación por cada usuario en paralelo
    with ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(procesoVotar, votantes, opciones)

    print("Todos los usuarios han terminado sus acciones.")

# Ejecutar la función principal
if __name__ == "__main__":
    ejecutar()





