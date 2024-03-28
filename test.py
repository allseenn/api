import undetected_chromedriver as uc
 
# Define a custom user agent
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
 
# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"user-agent={my_user_agent}")
options.binary_location = ("/opt/chrome-linux64/chrome") 
# Initialize Chrome WebDriver with the specified options
driver = uc.Chrome(options=options)
 
# Make a request to your target website.
driver.get("https://www.nowsecure.nl/")

# Close the driver
driver.quit()

