from selenium import webdriver

browser = webdriver.Firefox()

# Barry has heard about a cool new online to-do app. She goes to 
# Check out its homepage.

browser.get('http://localhost:8000')

# She notices the page title and header mention "to-do lists"
assert 'To-Do' in browser.title, 'Browser Title does not include "To-Do", it was: ' + browser.title

# She is invited to enter a to-do item staright away

# She types "Kidnap a peacock and discover its favorite food" into a text box (Barry's hobby is delighting animals)

# When she hits enter, the page updates, and now the page lists
# "1: Kidnap a peacock and disvoer its favorite food"

# There is still a text box inviting her to add another item. She
# enters "Use peacock to fly to the moon"

# The page updates again, and now shows both items on her list.

# Barry wonders whether the site will remember her list -- Then she sees
# that the site has generated a unique URL for her -- there is some explanatory text to that effect.  

# Satisfied, she goes back to sleep, dreaming of the fun times she will have with a new friend. 

browser.quit()
