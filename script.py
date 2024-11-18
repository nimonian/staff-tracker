import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import logging

matplotlib.use("Agg")

# configure logging
logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # log to the console
        logging.FileHandler("log.txt"),
    ],
)


def extract(file_path):
    logging.info(f"Attempting to read data from {file_path}")
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Successfully read data.")
        return data
    except Exception as e:
        logging.error(f"Error reading file: {e}")


def transform(data):
    data["Salary_USD"] = data["Salary_GBP"] * 1.25
    data["Years_to_Retirement"] = data["Age"].apply(lambda x: max(0, 65 - x))

    return data


def create_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Age"], data["Salary_USD"], alpha=0.7, edgecolors="k")
    plt.title("Age vs Salary (USD)", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Salary (USD)", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    plt.savefig("age_salary.png")


def main():
    file_path = "input.csv"
    data = extract(file_path)

    transformed_data = transform(data)
    create_plot(transformed_data)

    logging.debug(transformed_data)


if __name__ == "__main__":
    main()
