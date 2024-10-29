from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chemin vers le WebDriver
driver = webdriver.Chrome()

# URL de départ (première page)
base_url = "https://www.avito.ma/fr/maroc/immobilier"
page_links = []
property_links = []
max_pages = 4  # Set the maximum page to 9

try:
    # Collect page links
    page_number = 1
    while page_number <= max_pages:
        # Construire l'URL pour chaque page
        url = f"{base_url}?o={page_number}"
        driver.get(url)

        # Attendre que les annonces soient visibles ou terminer si aucune annonce n'est trouvée
        try:
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='sc-1lz4h6h-0 bsvCex']"))
            )
            # Ajouter l'URL de la page actuelle à la liste des liens
            page_links.append(driver.current_url)
            print(f"Page {page_number} ajoutée : {url}")
            page_number += 1  # Passer à la page suivante
            time.sleep(2)  # Pause pour éviter de surcharger le serveur

        except:
            print("Aucune annonce trouvée ou fin des pages atteinte.")
            break

    # Boucle sur chaque page link pour extraire les liens de propriété
    for link in page_links:
        driver.get(link)
        time.sleep(2)  # Attendre que la page se charge

        try:
            # Extraire tous les liens de propriété de la page
            annonces = driver.find_elements(By.XPATH, "//div[@class='sc-1lz4h6h-0 bsvCex']//a")
            for annonce in annonces:
                property_link = annonce.get_attribute("href")
                if property_link and property_link not in property_links:
                    property_links.append(property_link)
                    print(f"Lien de propriété trouvé : {property_link}")

        except Exception as e:
            print(f"Erreur lors de l'extraction des liens de propriété: {e}")

finally:
    # Enregistrer tous les liens des propriétés dans un fichier
    with open("property_links.txt", "w", encoding="utf-8") as f:
        for link in property_links:
            f.write(link + "\n")

    # Enregistrer tous les liens des pages dans un fichier
    with open("page_links.txt", "w", encoding="utf-8") as f:
        for link in page_links:
            f.write(link + "\n")
    
    # Fermer le WebDriver
    driver.quit()

print("Collecte des liens de propriété terminée. Liens enregistrés dans 'property_links.txt'.")
