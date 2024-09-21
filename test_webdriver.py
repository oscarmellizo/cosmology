from selenium import webdriver

# No es necesario especificar la ruta completa si ChromeDriver está en el PATH
driver = webdriver.Chrome()

# Abrir una página
driver.get("https://astro.ucla.edu/")

# Realiza tus acciones aquí, por ejemplo, encontrar elementos y hacer clic en ellos

# Cerrar el navegador al terminar
driver.quit()
