import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.debug("Division function started")

    try:
        result = a / b
        logging.info("Division performed successfully")
        print("Result:", result)

    except ZeroDivisionError:
        logging.error("Cannot divide by zero")

    finally:
        logging.debug("Division function completed")

logging.info("Program started")

divide(10, 2)
divide(10, 0)

logging.warning("This is a warning message")

logging.info("Program ended")

print("Check app.log file for log details.")