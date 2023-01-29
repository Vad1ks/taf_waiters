def move_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});",
                          element)
